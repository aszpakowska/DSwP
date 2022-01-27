from datetime import *
import sqlalchemy
import pandas as pd
import cx_Oracle
import requests
import datetime
import numpy as np

import urllib.request
import json
import mysql.connector
from pandas import json_normalize


cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_9")
engine = sqlalchemy.create_engine(
    'oracle+cx_oracle://szpakowskaa:aleksandraxxx@213.184.8.44:1521/orcl')

conn = engine.connect()


# conn.execute("TRUNCATE TABLE weather")

def getData(city):
    ApiKey = '629ec0cc680d21f0f37557a165f0f329'
    BaseURL = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = BaseURL + "appid=" + ApiKey + "&q=" + city
    res = requests.get(complete_url)
    data = res.json()

    timestamp = data['dt']
    value = datetime.datetime.fromtimestamp(timestamp)

    country = data['sys']['country']
    city = data['name']
    condition = data['weather'][0]['main']
    temp = int(data['main']['temp'] - 273.15)
    MINTEMP = int(data['main']['temp_min'] - 273.15)
    MAXTEMP = int(data['main']['temp_max'] - 273.15)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    WINDSPEED = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    TIMEOFLASTCHECK = value
    CITY_ID = data['sys']['id']

    df = pd.DataFrame([[country, city, condition, temp, MINTEMP, MAXTEMP, pressure, humidity, WINDSPEED, latitude,
                        longitude, TIMEOFLASTCHECK, CITY_ID]], columns=[
        'country', 'city', 'condition', 'temp', 'MINTEMP', 'MAXTEMP', 'pressure', 'humidity', 'WINDSPEED', 'latitude',
        'longitude', 'TIMEOFLASTCHECK', 'CITY_ID'])

    return df


cities_pl = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz',
             'Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora']
cities_ger = ['Berlin', 'Bremen', 'Dresden', 'Düsseldorf', 'Erfurt', 'Hamburg', 'Hanover', 'Kiel',
              'magdeburg', 'Mainz', 'Munich', 'Potsdam', 'Saarbrücken', 'Schwerin', 'Stuttgart', 'Wiesbaden']
cities_slov = ['Banska Bystrica', 'Bratislava',
               'Kosice', 'Presov', 'Trencin', 'Trnava', 'Zilina']
cities_hu = ['Budapest', 'Debrecen', 'Dunaujvaros', 'Eger', 'Gyor', 'Kaposvar', 'Kecskemet', 'Nagykanizsa',
             'Nyiregyhaza', 'Sopron', 'Szekesfehervar', 'Szolnok', 'Szombathely', 'Tatabanya', 'Veszprem',
             'Zalaegerszeg']
cities_nor = ['Bergen', 'Bodo', 'Oslo', 'Hamar', 'Kristiansand',
              'Molde', 'Skien', 'Stavanger', 'Trondheim', 'Tromso']
countries = [cities_pl, cities_ger, cities_slov, cities_hu, cities_nor]

data = pd.DataFrame()

for country in countries:
    for city in country:
        data = data.append(getData(city))

print(data)

df = data.replace({np.nan: None})

print(df)

with cx_Oracle.connect(user='szpsdhuaa', password='alensdwqwdcra', dsn='213.11521/orcl') as conn:
    cursor = conn.cursor()
    cursor.callproc("dbms_output.enable")
    status = cursor.var(cx_Oracle.NUMBER)
    var = cursor.var(cx_Oracle.STRING)

    cursor.executemany(
        """INSERT INTO view_weather (country, city, condition, temp, MINTEMP, MAXTEMP, pressure,humidity, WINDSPEED, latitude, longitude, TIMEOFLASTCHECK, CITY_ID) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)""",
        list(
            df.itertuples(index=False, name=None)))

    while True:
        cursor.callproc("dbms_output.get_line", (var, status))
        if status.getvalue() != 0:
            break
        print(var.getvalue())

    conn.commit()

df = pd.read_sql("SELECT * FROM weather", engine)
df.to_csv('CSV/plik.csv')
