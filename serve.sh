#!/bin/bash

exec gunicorn --chdir src  -b :5000 api:app
