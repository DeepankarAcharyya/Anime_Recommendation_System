#drop tables
DROP_ANIME_MASTER = """ DROP TABLE IF EXISTS anime_master;"""
DROP_ANIME_META = """ DROP TABLE IF EXISTS anime_meta;"""
DROP_ANIME_SCORE = """ DROP TABLE IF EXISTS anime_score;"""
DROP_ANIME_WATCHING_STATUS = """ DROP TABLE IF EXISTS anime_watching_status;"""
DROP_ANIME_LIST = """ DROP TABLE IF EXISTS anime_list;"""

#create tables
CREATE_TABLE_ANIME = """ 
                            CREATE TABLE IF NOT EXISTS anime_master (
                                MAL_ID INTEGER PRIMARY KEY,
                                Name TEXT,
                                Score FLOAT,
                                Genres TEXT
                            );
                     """

CREATE_TABLE_ANIME_META = """ 
                            CREATE TABLE IF NOT EXISTS anime_meta (
                                MAL_ID INTEGER PRIMARY KEY,
                                Type TEXT,
                                Episodes INTEGER,
                                Aired TEXT,
                                Licensors TEXT,
                                Premiered TEXT,
                                Studios TEXT,
                                Duration TEXT,
                                Audience_Age_Rating TEXT,
                                Ranked FLOAT,
                                Popularity INTEGER,
                                FOREIGN KEY(MAL_ID) REFERENCES anime_master(MAL_ID)
                            );
                          """

CREATE_TABLE_ANIME_SCORE = """ 
                            CREATE TABLE IF NOT EXISTS anime_score (
                                MAL_ID INTEGER PRIMARY KEY,
                                Score_10 INTEGER,
                                Score_9 INTEGER,
                                Score_8 INTEGER,
                                Score_7 INTEGER,
                                Score_6 INTEGER,
                                Score_5 INTEGER,
                                Score_4 INTEGER,
                                Score_3 INTEGER,
                                Score_2 INTEGER,
                                Score_1 INTEGER,
                                FOREIGN KEY(MAL_ID) REFERENCES anime_master(MAL_ID)
                            );
                           """

CREATE_TABLE_ANIME_WATCHING_STATUS = """ 
                                        CREATE TABLE IF NOT EXISTS anime_watching_status (
                                            status INTEGER PRIMARY KEY,
                                            description TEXT
                                        );
                                     """

CREATE_TABLE_ANIME_LIST = """ 
                                CREATE TABLE IF NOT EXISTS anime_list (
                                    s_no SERIAL PRIMARY KEY,
                                    user_id  INTEGER,
                                    anime_id INTEGER,
                                    watching_status INTEGER,
                                    watched_episodes INTEGER,
                                    FOREIGN KEY(watching_status) REFERENCES anime_watching_status(status),
                                    FOREIGN KEY(anime_id) REFERENCES anime_master(MAL_ID)
                                );
                           """

#inserting data
INSERT_ANIME_MASTER = """ INSERT INTO anime_master (MAL_ID, Name, Score, Genres) VALUES (%s, %s, %s, %s) ; """

INSERT_ANIME_META = """ INSERT INTO anime_meta (MAL_ID, Type, Episodes, Aired, Licensors, Premiered, Studios, Duration, Audience_Age_Rating, Ranked, Popularity) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ; """

INSERT_ANIME_SCORE = """ INSERT INTO anime_score (MAL_ID, Score_10,Score_9, Score_8, Score_7, Score_6, Score_5, Score_4, Score_3, Score_2, Score_1)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ; """

INSERT_ANIME_LIST = """ INSERT INTO anime_list (user_id, anime_id, watching_status, watched_episodes) VALUES (%s, %s, %s, %s) ; """

INSERT_ANIME_WATCHING_STATUS = """ INSERT INTO anime_watching_status (status, description) VALUES (%s, %s) ; """

#data quality checks
DC_ANIME_MASTER = """ SELECT COUNT(*) FROM anime_master ;  """
DC_ANIME_SCORE = """ SELECT COUNT(*) FROM anime_score;  """
DC_ANIME_META = """ SELECT COUNT(*) FROM anime_meta;  """
DC_ANIME_LIST = """ SELECT COUNT(*) FROM anime_list;  """
DC_ANIME_WATCHING_STATUS = """ SELECT COUNT(*) FROM anime_watching_status; """
