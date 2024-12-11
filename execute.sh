#!/usr/bin/env bash

source /home/owen/Indego/.venv/bin/activate

echo $DB_NAME

python3 bikes_and_docks_data_fetch.py
