#!/bin/sh

gunicorn -w 4 --threads 12 -b :8080 main:app
