import os
# import urllib
# params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=CHAMPION\SQLEXPRESS;DATABASE=Xclutel_XT;UID=sa;PWD=Foosball1")

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
