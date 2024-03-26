# Tornado Damage and Casualties

![tornado](images/tornado.jpg)

Tornado damage since 1950 has been significant, with numerous destructive tornadoes causing 
extensive damage to crops and infrastructure as well as resulting in many casualties and injuries.

## Objective

The objective of this project is to analyze and present data on tornado occurrences in the United
States since 1950, showing the extent of damage inflicted on both crops and infrastructure.
Additionally, the project aims to present the number of injuries and fatalities resulting from
these disasters.

Questions:

- What is the impact on crop damage compared to property damage caused by tornadoes in the United 
  States? 
- How many injuries and fatalities do tornadoes typically inflict upon the United States annually?

## Project Requirements
  
1. Read TWO data files (JSON, CSV, Excel, etc.):
   - 1950-23 damage_fatal_injury.csv
   - 1950-2023_tor_fatalities.csv


2. Clean your data and perform a pandas merge with your two data sets, then calculate some new
   values based on the new data set.
     - Data was cleaned in clean.ipynb
     - Pandas merge was performed in Main.ipynb


3. Make a Tableau dashboard to display your data.

![fatalities](images/fatvsinj.PNG)
   Tableau dashboard can be viewed [here](https://public.tableau.com/app/profile/timothy.holbrook/vizzes).


4. Utilize a virtual environment and include instructions in your README on how the user should set
   one up.


5. Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a
   well-written README.md


## Running the Project

1. Python 3 is required. Project was created with version 3.11.7. Python can be downloaded [here](https://www.python.org/downloads/).
2. Clone the repo from GitHub.
   - You can create a GitHub account [here](https://github.com/) if needed.
   - To learn how to clone a repo on GitHub, please click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
3. Setup virtual enviorment. Please type the following into terminal of your choice inside main folder once cloned.
   - On macOS/Linux: python3 -m venv venv
   - On Windows: python -m venv venv
4. Activate virtual enviorment
   - on macOS/Linux: source venv/bin/activate
   - on Windows: venv\Scripts\activate
5. Install dependencies: pip install -r requirements.txt
6. After installation completes, you can verify what was installed with: pip list 



