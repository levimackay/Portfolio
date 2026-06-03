-- -----------------------------------------------------
-- LEVI'S BASEBALL ANALYTICS ENGINE
--
-- Why am I building a baseball database? Because flat Excel files 
-- are where sports data goes to die. I wanted a way to actually 
-- query performance trends—like "who is hitting better in the 
-- second half of the season?" or "which parks are hitters' paradises?"
--
-- This script handles some of the more "galaxy brain" queries 
-- that actually provide useful insights for a team or a scout.
-- -----------------------------------------------------

USE `baseball`;

-- -----------------------------------------------------
-- 1. THE "SWING TREND" REPORT
-- This query uses window functions to show a player's 
-- rolling batting average over their last 5 games.
-- This is how you catch a hot streak before it's over.
-- -----------------------------------------------------

SELECT 
    p.firstName,
    p.lastName,
    g.gameDate,
    ps.hits,
    ps.atBats,
    -- Rolling AVG: Sum of hits / Sum of atBats for the last 5 games
    ROUND(
        SUM(ps.hits) OVER (PARTITION BY p.playerID ORDER BY g.gameDate ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) / 
        NULLIF(SUM(ps.atBats) OVER (PARTITION BY p.playerID ORDER BY g.gameDate ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 0), 
        3
    ) AS rolling_5game_avg
FROM player p
JOIN playerStats ps ON p.playerID = ps.playerID
JOIN game g ON ps.gameID = g.gameID
ORDER BY p.lastName, g.gameDate DESC;


-- -----------------------------------------------------
-- 2. PARK FACTORS ANALYSIS
-- Some stadiums are just easier to hit in. This query 
-- calculates the average runs scored per game at each ballpark
-- to see which ones are "Pitcher Friendly" vs "Hitter Friendly".
-- -----------------------------------------------------

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


-- -----------------------------------------------------
-- 3. THE "CLUTCH" FACTOR
-- Who is performing best under pressure? 
-- (Assuming we have a 'isClutchSituation' flag or just looking at late innings)
-- For now, let's just find players with the most RBI's per hit.
-- -----------------------------------------------------

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


-- -----------------------------------------------------
-- 4. TEAM EFFICIENCY
-- This query ranks teams by their "Winning Efficiency"—
-- basically, who is winning the most games relative to their 
-- total team salary (if we had a salary table) or just raw wins.
-- -----------------------------------------------------

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

-- -----------------------------------------------------
-- This is just the start. SQL is honestly like a superpower 
-- for sports. You can find patterns that nobody else sees.
-- -----------------------------------------------------
