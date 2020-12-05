#!/bin/sh

gunicorn -w 2 --threads 8 -b :8080 main:app
