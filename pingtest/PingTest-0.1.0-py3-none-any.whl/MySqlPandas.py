from sqlalchemy import create_engine
import pymysql
import pandas as pd



sqlEngine       = create_engine('mysql+pymysql://colin:colin@127.0.0.1/colin', pool_recycle=3600)

dbConnection    = sqlEngine.connect()

frame           = pd.read_sql("select downloadspeed,uploadspeed from colin.downloadtest", dbConnection);



pd.set_option('display.expand_frame_repr', False)

print(frame)



dbConnection.close()
