#!/usr/bin/env bash

# If any command fails (non-zero exit status), the script will exit immediately.
set -o errexit

# If any command in the pipeline fails (non-zero exit status), the script will exit with an error.
set -o pipefail

cmd="$@"

function environment_configured(){
python << END
from pathlib import Path
from dj_database_url import parse as db_url
from decouple import config

db = config("DATABASE_URL", cast=db_url)
END
}

function postgres_ready(){
python << END
import sys
import psycopg2
from pathlib import Path
from dj_database_url import parse as db_url
from decouple import config

db = config("DATABASE_URL", cast=db_url)

try:
    conn = psycopg2.connect(dbname=db["NAME"], user=db["USER"], password=db["PASSWORD"], host=db["HOST"], port=db["PORT"])
except psycopg2.OperationalError as e:
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}

environment_configured || { echo 'Environment configuration check failed' ; exit 1; }

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd
