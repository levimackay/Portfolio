# Baseball Analytics Engine

This started as a database design assignment and turned into something I actually care about. The schema is built in MySQL and tracks players, teams, games, stats, and ballparks all connected through a normalized relational structure.

The interesting part is the queries. I wrote window functions for rolling batting averages over the last 5 games, RBI efficiency per hit, team win rankings using CTEs with RANK(), and ballpark run averages grouped by venue. It is the kind of analysis you would actually see behind a real sports platform.

The .mwb file in the SQL folder is the full MySQL Workbench model if you want to see the schema laid out visually.

Built with MySQL.
