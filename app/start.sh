#!/bin/bash

exec pip install -r /app/requirements.txt \
    && mod_wsgi-express start-server --working-directory /app/homestarter/ /app/homestarter/homestarter/wsgi.py"