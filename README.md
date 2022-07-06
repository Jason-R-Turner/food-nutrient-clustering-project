# USDA Macronutrient Profile Analysis Using Clustering and Regression: Food for Thought

### Project Goals
 - To construct a ML classification model that uses clustering to identify different groups of food based on the distribution of their main nutritional components.
 - To analyze the strength of the relationships between the different major variable categories
 - To be able to categorize what kind of food an item is based on its nutritional profile

--------------------

## Project Summary
 - Classification using a clustering model to see if I can classify foods based on their nutrition profiles.
 - To see if it's possible to classify food based solely on its macronutrients
 - To see if the major food groups that we classify by other means neatly matches a nutrient profile
 - To see if any other patterns emerge from amongst the data
 
a link to the data source
 - https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2017-2018%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx
 
 - https://trello.com/b/Fp62Bo21/food-for-thought

Target variable
 - Food groupings
 
 - An observation represents a unique individual food item with its nutrition information
 
--------------------

### Data Science Pipeline
- Planning
 - Scoured the internet for data I could use
 - Reevaluated plan and scoured web again
- Acquisition
 - Acquired JSON data from USDA API link
 - Downloaded excel files to local environment
 - Linked directly to source file on USDA site
- Preparation
 - Reassigned first row as new column headers
 - Dropped unnecessary columns
 - Convert dataframe objects to floats
- Exploration
 - Performed univariate analysis of each dataframe column
 - Performed statistical tests for different column pairs
 - Preprocessed datasets for modeling
- Modeling
 - Determined suitable k value using elbow graphs method
 - Fit dataset to K-Means model
 - Created n clusters from dataset
 - Added cluster predictions to unscaled dataset
 - Determined centroid values for each cluster
- Delivery
 - Github Repo w/ Final Notebook and README
 - All necessary modules to make my project reproducible
 - Project summary and writeup for your resume or other professional portfolio pieces 
 
--------------------

### Project Objectives
- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report for colleague review.

--------------------
### Audience
- Immediately, fellow Codeup cohort Data Science students
- Going forward, recruiters for data science aligned roles

--------------------

### Deliverables
- Github Repo w/ Final Notebook and README
- All necessary modules to make my project reproducible
- Project summary and writeup for your resume or other professional portfolio pieces

--------------------

### Data Dictionary:
| Module Functions        | Definitions                                             |
| ------------------------|:----------------------------------------------------:|
| get_food_data           | Creates datafram from FNDDS excel file               |
| first_row_to_col_header | Returns a dataframe with first row as column headers |
| drop_cols               | Drops columns with unwanted variables                |
| object_to_float         | Converts objects to floats                           |
| wrangle_food            | Returns a prepared dataframe                         |
| scale_food              | Scales train, validate, and test dataframes          |
| find_k                  | Shows different elbow graphs for values of k         |
| cluster_maker           | Fits scaled data to K-Means model                    |
| get_centroids           | Gets the centroids for each distinct cluster         |
| assign_clusters         | Labels clusters for scaled data                      |
| metrics                 | Gives number of nulls, rows, columns, and description|
| get_numbers             | Returns descending order of total unique value counts|

| Dataframe Columns         | Definitions                                          
| --------------------------|:----------------------------------------------------:
| Food code                 | Individual USDA number identifying each food
| Main food description     | Individual name for describing each food 
| WWEIA Category description| Category name for describing groups of food
| Energy (kcal)             | Energy content expressed in units of kilocalories 
| Protein (g)               | Protein by weight in grams
| Carbohydrate (g)          | Carbohydrates by weight in grams
| Sugars, total\n(g)        | Total sugars by weight in grams 
| Fiber, total dietary (g)  | Total fiber by weight in grams
| Total Fat (g)             | Total fat by weight in grams
| Water\n(g)                | Water in grams
| cluster                   | Numbered K-Means model clusters
                         

## Project Reproduction
[ ] Read the README.md file
[ ] Download the wrangle.py file into working directory for acquire and prepare functions 
[ ] Also download the model.py and util.py files to local directory
[ ] Then run final_report_food_project jupyter notebook
