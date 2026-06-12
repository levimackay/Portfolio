USE `baseball`;

-- 1. Rolling average batting performance (last 5 games)
SELECT 
    p.firstName,
    p.lastName,
    g.gameDate,
    ps.hits,
    ps.atBats,
    ROUND(
        SUM(ps.hits) OVER (PARTITION BY p.playerID ORDER BY g.gameDate ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) / 
        NULLIF(SUM(ps.atBats) OVER (PARTITION BY p.playerID ORDER BY g.gameDate ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 0), 
        3
    ) AS rolling_5game_avg
FROM player p
JOIN playerStats ps ON p.playerID = ps.playerID
JOIN game g ON ps.gameID = g.gameID
ORDER BY p.lastName, g.gameDate DESC;


-- 2. Ballpark run averages
SELECT 
    bp.ballparkName,
    bp.city,
    COUNT(g.gameID) AS total_games_played,
    ROUND(AVG(g.homeTeamScore + g.awayTeamScore), 2) AS avg_total_runs
FROM ballpark bp
LEFT JOIN game g ON bp.ballparkID = g.ballparkID
GROUP BY bp.ballparkID
HAVING total_games_played > 0
ORDER BY avg_total_runs DESC;


-- 3. RBI efficiency per hit
SELECT 
    p.firstName, 
    p.lastName,
    SUM(ps.hits) AS total_hits,
    SUM(ps.rbi) AS total_rbis,
    ROUND(SUM(ps.rbi) / NULLIF(SUM(ps.hits), 0), 2) AS rbis_per_hit
FROM player p
JOIN playerStats ps ON p.playerID = ps.playerID
GROUP BY p.playerID
HAVING total_hits > 10
ORDER BY rbis_per_hit DESC
LIMIT 10;


-- 4. Team win rankings
WITH TeamWins AS (
    SELECT 
        teamID,
        COUNT(*) AS wins
    FROM (
        SELECT homeTeamID AS teamID FROM game WHERE homeTeamScore > awayTeamScore
        UNION ALL
        SELECT awayTeamID AS teamID FROM game WHERE awayTeamScore > homeTeamScore
    ) all_wins
    GROUP BY teamID
)
SELECT 
    t.teamName,
    t.city,
    COALESCE(tw.wins, 0) AS total_wins,
    RANK() OVER (ORDER BY COALESCE(tw.wins, 0) DESC) AS league_rank
FROM team t
LEFT JOIN TeamWins tw ON t.teamID = tw.teamID
ORDER BY league_rank ASC;
