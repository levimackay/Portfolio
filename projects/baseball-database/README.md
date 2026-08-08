# Baseball Analytics Engine

This started as a database design assignment and turned into something I actually care about. The schema is MySQL and covers players, teams, games, per-game stats, ballparks, seasons, coaches, umpires, injuries, sponsors, and ticket and concession sales, all connected through a normalized relational structure.

The interesting part is the queries in `SQL/baseballdbcode.sql`. There are four:

* rolling batting average over a player's last five games, using a windowed `SUM` with `ROWS BETWEEN 4 PRECEDING AND CURRENT ROW`
* ballpark run averages, grouped by venue
* RBI efficiency per hit, for players with more than ten hits
* team win rankings, with a CTE that unions home and away wins and `RANK()` over the totals

Load the dump first, then run the query file against it. `SQL/baseballdata2.sql` is a full `mysqldump` — schema plus sample data — for a database named `baseball`. The `.mwb` file in the same folder is the MySQL Workbench model if you want to see the schema laid out visually.

Built with MySQL.
