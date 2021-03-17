import pandas as pd
from src.d00_utils.mysql_func import mysql_connect, save_to_mysql

#Import data from Professional_Salary_Survey
database1 = pd.read_excel("../../Data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx", skiprows=3)

# Import data from the Kaggle csv
database2 = pd.read_csv("../../Data/01_raw/DataAnalyst.csv")

# Create connection with mysql
connect = mysql_connect()

# Save the data into mysql tables
save_to_mysql(db_connect=connect, df_to_save=database1, df_name='survey_1')
save_to_mysql(db_connect=connect, df_to_save=database2, df_name='survey_k')