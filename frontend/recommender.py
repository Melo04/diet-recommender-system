import json
import requests

class Recommender:
    def __init__(self, nutrition:list, ingredients:list=[], params:dict={'n_neighbors':5, 'return_distance':False}):
        self.nutrition=nutrition
        self.ingredients=ingredients
        self.params=params
    
    def request(self, nutrition:list, ingredients:list, params:dict):
        self.nutrition=nutrition
        self.ingredients=ingredients
        self.params=params
    
    def recommend(self,):
        request={
            'nutrition':self.nutrition,
            'ingredients':self.ingredients,
            'params':self.params
        }
        response=requests.post(url='http://backend:8080/predict/', data=json.dumps(request))
        return response