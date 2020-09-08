#!/bin/bash
set -e
exec gunicorn --config ./docker/gunicorn.config.py wsgi:hello