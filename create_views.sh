psql news -c "CREATE VIEW proc as SELECT RIGHT(path, -9) AS \
		log_slug, count(*) from log \
		WHERE status = '200 OK' and path != '/' \
		GROUP BY log_slug \
		ORDER BY count desc;"
