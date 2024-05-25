import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

# perform feature scaling
def scale(df):
    scaler=StandardScaler()
    data=scaler.fit_transform(df.iloc[:,7:18].to_numpy())
    return data, scaler

# utilizes the K-nearest neighbors algorithm to identify the nearest neighbors
def knn_algo(data):
    knn = NearestNeighbors(metric='cosine',algorithm='brute')
    knn.fit(data)
    return knn

# construct a pipeline model
def build_pipeline(knn,scaler,params):
    transformer = FunctionTransformer(knn.kneighbors,kw_args=params)
    pipeline=Pipeline([('std_scaler',scaler),('NN',transformer)])
    return pipeline

# filter data according to user requirements
def filter_data(df, ingredient_filter, max_nutrition, food_type):
    data=df.copy()
    for column,maximum in zip(data.columns[7:13],max_nutrition):
        data = data[data[column]<maximum]
    if food_type != None:
        data = data[data[food_type]==True]
    if ingredient_filter!=None:
        for ingredient in ingredient_filter:
            data = data[data['RecipeIngredientParts'].str.contains(ingredient,regex=False)] 
    return data

# apply pipeline model on input data
def model_pipeline(pipeline, input, data):
    input = np.array(input).reshape(1,-1)
    return data.iloc[pipeline.transform(input)[0]]

# recommend user based on their input requirements
def recommend(df, input, max_nutritional_values, food_type, ingredient_filter=None, params={'return_distance':False}):
    extract_data=filter_data(df, ingredient_filter, max_nutritional_values, food_type)
    prep_data,scaler=scale(extract_data)
    neigh=knn_algo(prep_data)
    pipeline=build_pipeline(neigh, scaler,params)
    return model_pipeline(pipeline, input, extract_data)