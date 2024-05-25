import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel,conlist
from typing import List, Optional
from model import recommend

df = pd.read_csv('./data/RAW_recipes.csv', compression='gzip')

app = FastAPI()

class params(BaseModel):
    n_neighbors:int=5
    return_distance:bool=False

class PredictionInput(BaseModel):
    nutrition_input: conlist(float, min_items=9, max_items=9)
    ingredients: list[str]=[]
    params:Optional[params]