import os
import urllib

import sqlalchemy


password = os.environ.get('DB_PASSWORD')

connection_string = urllib.parse.quote_plus(
    'DSN=MSSQLServerDatabase;'
    'UID=sa;'
    'PWD={}'.format(password)
)

engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(
    connection_string
))
