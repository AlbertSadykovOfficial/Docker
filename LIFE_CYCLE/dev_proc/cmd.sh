#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
	echo "Running Development Server"
	exec python "identidock.py"
else
	echo "Running Product Server"
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:919191