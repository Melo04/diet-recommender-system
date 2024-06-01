## __Diet Recommender System__
CDS6214 Data Science Fundamentals Assignment ( Trimester 2, 23/34 )

## __Overview__
This web application is designed to recommend a diet plan based on the user's preferences such as calories, protein, fat, sodium and carbohydrates. Besides that, it could also show the nutritional information for each food items, as well as the recipes to make them. The frontend is made with Steamlit and the backend is built with FastAPI framework. The dataset is obtained from [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv) which consists of 180K+ recipes covering user interactions and uploads on Food.com.

## __Model development__
The recommendation engine utilizes Nearest Neighbors algorithm, an unsupervised learning approach to recommend similar food items based on the user's input. In our scenario, we opted for the brute-force method with cosine similarity because it offers quick computation for small datasets.

## __Compile and Run Instructions__
1. In your terminal, clone the repository by typing 
```bash
git clone https://github.com/Melo04/diet-recommender-system.git
```
2. After that, type the below command. This directory is where your virtual environment and its dependencies are installed.
```bash
python -m venv .venv
```
3. In your terminal, activate your environment with one of the following commands, depending on your operating system.
```
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```
4. Type in the below command to install all the required packages
```bash
pip install -r requirements.txt
```
5. After that, go to the frontend folder and type in the below command
```bash
cd frontend
```
6. Test that the installation worked by launching the Streamlit app:
```bash
streamlit run home.py
```
7. Go to your browser and type ```localhost:8501```, the app should be running now
8. For running backend, cd into backend folder and type the command below to start the server.
```bash
uvicorn main:app --reload
``` 