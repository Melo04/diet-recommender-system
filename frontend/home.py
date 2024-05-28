import streamlit as st
import numpy as np
import pandas as pd
from recommender import Recommender

st.set_page_config(
    page_title="Diet Recommender System",
    page_icon=":green_salad:",
)

st.write(
    """
    # Diet Recommender System :green_salad:
    This web application is designed to recommend a diet plan based on the user's preferences including calories, protein, fat, and carbohydrates.
    Besides that, it could also show the nutritional information of the food items, as well as the recipes.
    """
)

nutritions = ['Calories', 'TotalFat', 'Sugar', 'Sodium', 'Protein', 'SaturatedFat', 'Carbohydrates']
if 'recommended' not in st.session_state:
    st.session_state.recommended = False
    st.session_state.recommendations = None

class Recommendation:
    def __init__(self, nutrition_list, recommendations, ingredient):
        self.nutrition_list=nutrition_list
        self.recommendations=recommendations
        self.ingredient=ingredient
        pass

    def generate(self,):
        params = {'n_neighbors':self.recommendations, 'return_distance':False}
        ingredients = self.ingredient.split(',')
        generator = Recommender(self.nutrition_list, ingredients, params)
        recommend = generator.recommend()
        recommend=recommend.json()['output']
        ## 
        return recommend
    
class Recipes:
    def __init__(self):
        self.nutritions=nutritions
    
    def recommend_recipes(self, recommendations):
        st.subheader('Recommended recipes:')
        if recommendations != None:
            rows=len(recommendations)//5
            for column, row in zip(st.columns(5), range(5)):
                with column:
                    for recipe in recommendations[rows*row:rows*(row+1)]:
                        recipe_name = recipe['Name']
                        expander = st.expander(recipe_name)
                        recipe_link = recipe['image_link']
                        recipe_img = f'<div><center><img src={recipe_link} alt={recipe_name}></center></div>'
                        nutritions_df = pd.DataFrame({value:[recipe[value]] for value in nutritions})

                        expander.markdown(recipe_img, unsafe_allow_html=True)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values (g):</h5>', unsafe_allow_html=True)                   
                        expander.dataframe(nutritions_df)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Ingredients:</h5>', unsafe_allow_html=True)
                        for ingredient in recipe['RecipeIngredientParts']:
                            expander.markdown(f"""
                                - {ingredient}
                            """)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Recipe Instructions:</h5>', unsafe_allow_html=True)    
                        for instruction in recipe['RecipeInstructions']:
                            expander.markdown(f"""
                                - {instruction}
                            """)
                        expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Cooking and Preparation Time:</h5>', unsafe_allow_html=True)   
                        expander.markdown(f"""
                            - Cook Time       : {recipe['CookTime']}min
                            - Preparation Time: {recipe['PrepTime']}min
                            - Total Time      : {recipe['TotalTime']}min
                        """)
        else:
            st.info('Couldn\'t find any recipes with the specified ingredients')

recipes = Recipes()

# recommendation form for user to input preferred nutrition values
with st.form("recommend_form"):
    st.write("#### Enter your nutritional values below: ")
    calories = st.slider("Calories", 0, 434360, 368)
    total_fat = st.slider("Total fat", 0, 17183, 17)
    sugar = st.slider("Sugar", 0, 362729, 10)
    sodium = st.slider("Sodium", 0, 29338, 2)
    protein = st.slider("Protein", 0, 6552, 14)
    saturated_fat = st.slider("Saturated fat", 0, 10395, 8)
    carbohydrates = st.slider("Carbohydrates", 0, 36098, 20)
    st.write("#### Recommendation Options (Optional)")
    ingredient = st.text_input('Specify the ingredients that you would like to include in the recommendations separated by "," :', placeholder='Eggs, Milk')

    nutritions_values = [calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrates]
    recommendations = st.slider("Number of recommendations", 1, 20, 5)
    recommended = st.form_submit_button("Recommend Me")

# display loading spinner and update session state with generated recommendations
if recommended:
    with st.spinner('Generating recommendations...'):
        recommendations = Recommendation(nutritions_values, recommendations, ingredient)
        recommendations = recommendations.generate()
        st.session_state.recommendations=recommendations
    st.session_state.recommended=True 

if st.session_state.recommended:
    with st.container():
        recipes.recommend_recipes(st.session_state.recommendations)