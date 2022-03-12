import configparser
import psycopg2
from sql_queries import *

config = configparser.ConfigParser()
config.read('credentials.cfg')

conn = psycopg2.connect(
            host=config["DB"]["HOST"],
            port=config["DB"]["PORT"],
            database=config["DB"]["DATABASE"],
            user=config["DB"]["USER"],
            password=config["DB"]["PASSWORD"])
    
conn.set_session(autocommit=True)
curr = conn.cursor()

curr.execute(DROP_ANIME_SCORE)
curr.execute(DROP_ANIME_META)
curr.execute(DROP_ANIME_LIST)
curr.execute(DROP_ANIME_WATCHING_STATUS)
curr.execute(DROP_ANIME_MASTER)

curr.execute(CREATE_TABLE_ANIME)
curr.execute(CREATE_TABLE_ANIME_WATCHING_STATUS)
curr.execute(CREATE_TABLE_ANIME_LIST)
curr.execute(CREATE_TABLE_ANIME_META)
curr.execute(CREATE_TABLE_ANIME_SCORE)

curr.close()
conn.close()