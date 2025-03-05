#!/bin/sh

cd ../db
alembic upgrade head

cd ../app
exec "$@"
