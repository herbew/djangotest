#!/bin/bash


# environment directory is '/root/env'
# project directory is '/root/djangotest'

source /root/env/bin/activate
/root/env/bin/python /root/djangotest/manage.py collectstatic --settings=config.settings.local --noinput
/root/env/bin/gunicorn config.wsgi -w 5 -b 127.0.0.1:5000 --chdir=/root/djangotest
