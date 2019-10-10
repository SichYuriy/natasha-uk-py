from pymongo import MongoClient
import os

mongoDbHost = ('NATASHA_MONGO_DB_HOST_URL' in os.environ and os.environ['NATASHA_MONGO_DB_HOST_URL']) or 'localhost'
mongoDbPort = ('NATASHA_MONGO_DB_PORT' in os.environ and int(os.environ['NATASHA_MONGO_DB_PORT'])) or 27017
client = MongoClient(mongoDbHost, mongoDbPort, maxPoolSize=20)


class VesumService():
    def findByWordForm(self, wordForm):
        return client['natasha-uk-database']['vesum-entry'].find({'word': wordForm})


vesum_service = VesumService()