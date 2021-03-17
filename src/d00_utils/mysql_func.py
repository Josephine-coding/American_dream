import sqlalchemy
import mysql.connector

# Creation of the mysql functions

def mysql_connect():
    ''' Allow the connection to the mysql database '''
    from conf.conf_connect import mysql_pseudo, mysql_pw
    mysql_username = mysql_pseudo
    mysql_password = mysql_pw
    database_name = 'american_dream'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()
    return database_connection

def save_to_mysql(db_connect,df_to_save,df_name):
    ''' To save a dataframe into a mysql table '''
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')