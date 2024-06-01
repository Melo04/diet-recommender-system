import json
import requests

class Recommender:
    def __init__(self, nutrition_input:list, ingredients:list=[], food_type:str="", params:dict={'n_neighbors':5, 'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.food_type=food_type
        self.params=params
    
    def request(self, nutrition_input:list, ingredients:list, food_type:str, params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.food_type=food_type
        self.params=params
    
    def recommend(self,):
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'food_type':self.food_type,
            'params':self.params
        }
        response=requests.post(url='http://backend:8000/recommend/', data=json.dumps(request))
        return response