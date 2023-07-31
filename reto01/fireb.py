import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseAdmin:
    
    def __init__(self):
        cred = credentials.Certificate('token.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        
    def get_proyectos(self):
        return self.get_collection('proyectos')
    
    def get_education(self):
        return self.get_collection('education')
    
    def get_experiencia_laboral(self):
        return self.get_collection('experiencia laboral')
    
    def get_collection(self, collection_name):
        list_collection = []
        collection_values = self.db.collection(collection_name)
        doc_values = collection_values.get()
        for doc in doc_values:
            dic_collection = doc.to_dict()
            dic_collection.update({'codigo': doc.id})
            list_collection.append(dic_collection)
            
        return list_collection

