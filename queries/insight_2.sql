-- How the three-point shot changed in the regular season.
-- The available three-point attempt fields begin in the 1981-82 season.
SELECT
    season_id,
    CAST(SUBSTR(season_id, 2, 4) AS INTEGER) AS season_start_year,
    COUNT(*) AS games,
    AVG((fg3a_home + fg3a_away) / 2.0) AS avg_three_pa_per_team_game,
    100.0 * SUM(fg3a_home + fg3a_away)
        / SUM(fga_home + fga_away) AS three_pa_share_pct,
    AVG((pts_home + pts_away) / 2.0) AS avg_points_per_team_game
FROM game
WHERE season_id GLOB '2[0-9][0-9][0-9][0-9]'
  AND CAST(SUBSTR(season_id, 2, 4) AS INTEGER) >= 1979
  AND fg3a_home IS NOT NULL
  AND fg3a_away IS NOT NULL
GROUP BY season_id
ORDER BY season_start_year;
