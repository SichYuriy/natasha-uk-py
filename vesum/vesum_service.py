from pymongo import MongoClient

client = MongoClient('localhost', 27017, maxPoolSize=20)


class VesumService():
    def findByWordForm(self, wordForm):
        return client['diploma-sb-database']['vesumentry'].find({'word': wordForm})


vesum_service = VesumService()