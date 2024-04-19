import os 


CWD = os.getcwd()
DB_URL = 'mongodb://%s:%s@127.0.0.1' % ('moonshot', 'moonshot')
# The DBURL is now hardcoded into the code but can be fetched from OS env variables instead or 
# other authentication methods can be used which are much secure. 
DB_NAME = "moonshot"
COLLECTION_NAME = "assignment"
