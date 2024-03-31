import os
from pymongo import MongoClient

class Database:
    
    def __init__(self):
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        cert_dir = os.path.join(current_script_dir, '..', 'access.pem')
        
        uri = "mongodb+srv://cluster0.vxnl1pi.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri,
                            tls=True,
                            tlsCertificateKeyFile=cert_dir)

        self.db = client['jot']
        self.collection = self.db['notes']
        
    def get_collection(self):
        return self.collection
    
    def next_index(self):
        number_collection = self.db['number']
        latest_id = number_collection.find_one()
        if latest_id is None:
            new_id = 1
            number_collection.insert_one({'latest_id': new_id})
        else:
            new_id = latest_id['latest_id'] + 1
            number_collection.update_one({}, {'$set': {'latest_id': new_id}})
            
        return new_id