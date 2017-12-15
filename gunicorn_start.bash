#!/bin/bash

NAME="django_app"
DJANGODIR=/home/webapps/operations
SOCKFILE=/home/webapps/operations/venv/run/gunicorn.sock

USER=jaap
GROUP=jaap
NUM_WORKERS=3

DJANGO_SETTINGS_MODULE=t_mc_apps.settings_test
DJANGO_WSGI_MODULE=t_mc_apps.wsgi

echo "Staring $NAME as `whoami`"

cd $DJANGODIR
source /home/webapps/operations/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

