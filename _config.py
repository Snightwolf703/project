import os



# grabs the folder where this scripts lives
basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = 'Flasktasker.db'

USERNAME = 'admin'

PASSWORD = 'admin'

# Creates a request forgery prevention
WTF_CSRF_ENABLED = True
# used in conjunction with WTF_CSRF_ENABLED to create a cruptographic token (validate form)
SECRET_KEY = 'myprecious'

# deine the full path for the DATABASE

DATABASE_PATH =  os.path.join(basedir, DATABASE)
