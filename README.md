## __Diet Recommender System__
CDS6214 Data Science Fundamentals Assignment ( Trimester 2, 23/34 )<br>
Web application: [https://diet-recommender-system.streamlit.app/](https://diet-recommender-system.streamlit.app/)

## __Tech Stack__
- Frontend - Streamlit
- Backend - FastAPI
- Containerization - Docker

## __Overview__
This web application utilized content-based filtering to recommend a diet plan based on the user's preferences such as calories, protein, fat, sodium and carbohydrates. Besides that, it could also show the nutritional information for each food items, as well as the recipes to make them. The frontend is made with Steamlit and the backend is built with FastAPI framework. The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv) which consists of 180K+ recipes covering user interactions and uploads on Food.com.

## __Content-based Filtering__
Content-based filtering is a recommendation system that suggests items based on the user's preferences. In this case, the user can input the amount of calories, protein, fat, sodium and carbohydrates they want in their diet. The recommendation engine will then suggest food items that meet the user's requirements. One of the main benefits of a content-based approach is its consideration of individual dietary restrictions and preferences, including allergies and food choices. By offering personalized recommendations, a content-based food recommendation engine assists users in making healthier eating decisions and enhancing their overall well-being.

## __Model development__
The recommendation engine utilizes Nearest Neighbors algorithm, an unsupervised learning approach to recommend similar food items based on the user's input. In our scenario, we opted for the brute-force method with cosine similarity because it offers quick computation for small datasets.

## __Compile and Run Instructions__
1. In your terminal, clone the repository by typing 
```bash
git clone https://github.com/Melo04/diet-recommender-system.git
```
2. Make sure you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/products/docker-desktop). Next, run the following command to build the Docker image:
```bash
docker-compose up -d --build
```
3. Once the image is built, you can access the web application by typing `http://localhost:8501` in your browser.