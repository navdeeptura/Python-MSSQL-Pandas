# Python-MSSQL-Pandas

Create a new file at config\db_config.ini \
Update following details in db_config.ini

[database]\
server = DB_NAME\INSTANCE \
database = DATABASE_NAME\
user = USERNAME\
password = PASSWORD

**Command to run the tests**:\
go to root directory:\
pytest --html=report.html -m current -s
