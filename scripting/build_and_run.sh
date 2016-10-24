#!/bin/bash

sudo ./setup.sh -d /tmp/database.db -c services.json && sudo python server.py
