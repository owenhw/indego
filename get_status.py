# imports
import civis
from indego import Indego
import pandas as pd
from datetime import datetime as dt

# initialize an indego object
ind = Indego()

#get the stations and put them in a dataframe
data = ind.get_stations()

df=pd.DataFrame(data).T

# keep only the data we want
df = df.loc[:, ['id', 'docksAvailable',
       'bikesAvailable', 'classicBikesAvailable', 'smartBikesAvailable',
       'electricBikesAvailable', 'kioskPublicStatus']]

# add a timestamp
df['timestamp'] = dt.now()
df['timestamp'] = df['timestamp'].astype9=('datetime64')
       

# import the station data into civis
civis.io.dataframe_to_civis(df, database = 'redshift-general'
                      , table='oharringtonwoodard.indego_stations_status'
                      , existing_table_rows='drop')
