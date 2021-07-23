# imports
import civis
from indego import Indego
import pandas as pd

# initialize an indego object
ind = Indego()

#get the stations and put them in a dataframe
data = ind.get_stations()

df=pd.DataFrame(data).T

df = df.loc[:, ['id', 'name', 'totalDocks', 'kioskType', 'addressStreet', 'addressCity',
       'addressState', 'addressZipCode', 'closeTime', 'eventEnd',
       'eventStart', 'isEventBased', 'isVirtual', 'timeZone', 'latitude',
       'longitude']]
       

# import the station data into civis
civis.io.dataframe_to_civis(df2, database = 'redshift-general'
                      , table='oharringtonwoodard.indego_stations'
                      , existing_table_rows='drop')
