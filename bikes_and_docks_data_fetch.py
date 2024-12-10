import os
import json
from datetime import datetime

from indego import Indego
import psycopg2
from psycopg2.extras import execute_batch


def return_only_some_keys(raw_dict: dict, keys_to_fetch: list) -> dict:
    return {key: raw_dict[key] for key in keys_to_fetch}


def fetch_data(timestamp=None) -> list:
    keys_to_fetch = [
        'id',
        'name',
        'totalDocks', 
        'docksAvailable', 
        'bikesAvailable', 
        'classicBikesAvailable', 
        'smartBikesAvailable', 
        'electricBikesAvailable',
        'rewardBikesAvailable',
        'rewardDocksAvailable',
        'bikes',
        #'timestamp',
        ]

    all_stations = Indego().get_stations()
    
    
    list_of_station_dicts = [
        return_only_some_keys(station_dict, keys_to_fetch=keys_to_fetch) 
        for station_dict in all_stations.values()
        ]
    
    for station in list_of_station_dicts:
        station['bikes'] = json.dumps({"bikes": [bike for bike in station['bikes']]})

        station['timestamp'] = timestamp

    return list_of_station_dicts


def insert_data(data):
    conn = psycopg2.connect(
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT']
    )

    cursor = conn.cursor()

    insert_sql = """INSERT INTO raw.bikes_and_docks 
            VALUES (
                %(id)s, 
                %(docksAvailable)s, 
                %(bikesAvailable)s, 
                %(classicBikesAvailable)s, 
                %(smartBikesAvailable)s, 
                %(electricBikesAvailable)s, 
                %(rewardBikesAvailable)s, 
                %(rewardDocksAvailable)s,
                %(bikes)s,
                %(timestamp)s)"""

    execute_batch(cursor, insert_sql, data)

    conn.commit()
    conn.close()


def main():

    timestamp = datetime.now().isoformat()

    data = fetch_data(timestamp)

    insert_data(data)


if __name__ == '__main__':
    main()
