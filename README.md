## __Diet Recommender System__
CDS6214 Data Science Fundamentals Assignment ( Trimester 2, 23/34 )

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
5. Test that the installation worked by launching the Streamlit app:
```bash
streamlit run home.py
```
6. Go to your browser and type ```localhost:8501```, the app should be running now