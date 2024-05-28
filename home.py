import streamlit as st
import time

st.set_page_config(
    page_title="Diet Recommender System",
    page_icon=":green_salad:",
)

st.write(
    """
    # Diet Recommender System :green_salad:
    """
)

# slider for user to input all 7 types of nutrition
# min, max, default value
calories = st.slider("Calories", 0, 434360, 368)
total_fat = st.slider("Total fat", 0, 17183, 17)
sugar = st.slider("Sugar", 0, 362729, 10)
sodium = st.slider("Sodium", 0, 29338, 2)
protein = st.slider("Protein", 0, 6552, 14)
saturated_fat = st.slider("Saturated fat", 0, 10395, 8)
carbohydrates = st.slider("Carbohydrates", 0, 36098, 20)

# recommend button
st.button("Recommend", type="primary")
