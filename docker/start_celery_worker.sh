#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

cd backend

celery -A ciaglo worker -Q default --without-gossip --without-mingle --without-heartbeat --concurrency 8 --loglevel=info