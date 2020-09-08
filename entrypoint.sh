#!/bin/bash
set -x
exec gunicorn --config ./docker/gunicorn.config.py wsgi:hello