#!/usr/bin/env bash

# If any command fails (non-zero exit status), the script will exit immediately.
set -o errexit

# If any command in the pipeline fails (non-zero exit status), the script will exit with an error.
set -o pipefail

# If an attempt to expand an unset variable occurs, the script will exit immediately.
set -o nounset

# This is commonly used for debugging and understanding how a script is executing,
# as it shows the actual commands with their arguments after any expansions and substitutions have taken place.
set -o xtrace

# make required migrations
python backend/manage.py migrate --noinput
python backend/manage.py create_first_admin_user
# add this in the production
#python manage.py collectstatic --noinput
python backend/manage.py runserver 0.0.0.0:8000