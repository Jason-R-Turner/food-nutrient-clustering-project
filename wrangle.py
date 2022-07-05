# Libraries
import pandas as pd
import os

# Pre-processing Data
import sklearn.preprocessing

# Visualizing
import matplotlib.pyplot as plt


def get_food_data():
    '''
    Function allows user to access "Food and Nutrient Database for Dietary Studies"
    from USDA.gov website and write it to an excel file then return a dataframe.
    '''
    
# Read excel file into pandas DataFrame.
    file = "https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2017-2018%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx"
    df = pd.read_excel(file)
        
# Cache data for local use
    df.to_excel('2017-2018 FNDDS At A Glance - FNDDS Nutrient Values.xlsx')

# Returns requested df
    return df

def first_row_to_col_header(df):
    '''
    Returns a dataframe that takes the first row from the original dataframe and makes them the names of their respective columns
    '''
    # Assign row as column headers
    df.columns = df.iloc[0]

    # Using DataFrame.rename()
    df1 = df.rename(columns=df.iloc[1])

    # Convert row to header and remove the row
    df1 = df.rename(columns=df.iloc[0]).loc[1:]

    # Using DataFrame.rename() to convert row to column header
    df.rename(columns=df.iloc[1], inplace = True)

    # Using DataFrame.values[]
    header_row = df.iloc[0]
    df1 = pd.DataFrame(df.values[1:], columns=header_row)
    return df1

def drop_cols(df):
    '''
    Drops columns with unwanted variables for the purposes of this project
    '''
    cols_to_drop = [ 'WWEIA Category number',
                     'Fatty acids, total saturated (g)',
                     'Fatty acids, total monounsaturated (g)',
                     'Fatty acids, total polyunsaturated (g)',
                     'Cholesterol (mg)',
                     'Retinol (mcg)',
                     'Vitamin A, RAE (mcg_RAE)',
                     'Carotene, alpha (mcg)',
                     'Carotene, beta (mcg)',
                     'Cryptoxanthin, beta (mcg)',
                     'Lycopene (mcg)',
                     'Lutein + zeaxanthin (mcg)',
                     'Thiamin (mg)',
                     'Riboflavin (mg)',
                     'Niacin (mg)',
                     'Vitamin B-6 (mg)',
                     'Folic acid (mcg)',
                     'Folate, food (mcg)',
                     'Folate, DFE (mcg_DFE)',
                     'Folate, total (mcg)',
                     'Choline, total (mg)',
                     'Vitamin B-12 (mcg)',
                     'Vitamin B-12, added\n(mcg)',
                     'Vitamin C (mg)',
                     'Vitamin D (D2 + D3) (mcg)',
                     'Vitamin E (alpha-tocopherol) (mg)',
                     'Vitamin E, added\n(mg)',
                     'Vitamin K (phylloquinone) (mcg)',
                     'Calcium (mg)',
                     'Phosphorus (mg)',
                     'Magnesium (mg)',
                     'Iron\n(mg)',
                     'Zinc\n(mg)',
                     'Copper (mg)',
                     'Selenium (mcg)',
                     'Potassium (mg)',
                     'Sodium (mg)',
                     'Caffeine (mg)',
                     'Theobromine (mg)',
                     'Alcohol (g)',
                     '4:0\n(g)',
                     '6:0\n(g)',
                     '8:0\n(g)',
                     '10:0\n(g)',
                     '12:0\n(g)',
                     '14:0\n(g)',
                     '16:0\n(g)',
                     '18:0\n(g)',
                     '16:1\n(g)',
                     '18:1\n(g)',
                     '20:1\n(g)',
                     '22:1\n(g)',
                     '18:2\n(g)',
                     '18:3\n(g)',
                     '18:4\n(g)',
                     '20:4\n(g)',
                     '20:5 n-3\n(g)',
                     '22:5 n-3\n(g)',
                     '22:6 n-3\n(g)']
    df = df.drop(columns=cols_to_drop, axis=1)
    return df


def object_to_float(df):
    '''
    Converts 'Energy (kcal)',
             'Protein (g)',
             'Carbohydrate (g)',
             'Sugars, total\n(g)',
             'Fiber, total dietary (g)',
             'Total Fat (g)',
             'Water\n(g)'
             from objects to floats
    '''
    df["Energy (kcal)"] = df["Energy (kcal)"].astype(float, errors = 'raise')
    df["Protein (g)"] = df["Protein (g)"].astype(float, errors = 'raise')
    df["Carbohydrate (g)"] = df["Carbohydrate (g)"].astype(float, errors = 'raise')
    df["Sugars, total\n(g)"] = df["Sugars, total\n(g)"].astype(float, errors = 'raise')
    df["Fiber, total dietary (g)"] = df["Fiber, total dietary (g)"].astype(float, errors = 'raise')
    df["Total Fat (g)"] = df["Total Fat (g)"].astype(float, errors = 'raise')
    df["Water\n(g)"] = df["Water\n(g)"].astype(float, errors = 'raise')
    
    return df

def wrangle_food():
    '''
    Combines get_food_data, first_row_to_col_head, drop_cols, and object_to_int functions to acquire and return a prepared dataframe.
    '''
    df = get_food_data()
    df = first_row_to_col_header(df)
    df = drop_cols(df)
    df = object_to_float(df)
    return df

def scale_food(train, validate, test,
                 cols_to_scale = ['Energy (kcal)', 
                                  'Protein (g)', 
                                  'Carbohydrate (g)', 
                                  'Sugars, total\n(g)', 
                                  'Fiber, total dietary (g)', 
                                  'Total Fat (g)', 
                                  'Water\n(g)']):
    
    '''
    Accepts train, validate, and test as inputs from split data then returns scaled versions for each one using MinMaxScaler.
    '''
    
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    scaler = sklearn.preprocessing.MinMaxScaler()

    scaler.fit(train[cols_to_scale])
    
    train_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(train[cols_to_scale]), columns=train[cols_to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(validate[cols_to_scale]), columns=validate[cols_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(test[cols_to_scale]), columns=test[cols_to_scale].columns.values).set_index([test.index.values])
    
    plt.figure(figsize=(13, 6))
    plt.subplot(121)
    plt.hist(train[cols_to_scale], bins=25, ec='black')
    plt.title('Original')
    plt.subplot(122)
    plt.hist(train_scaled[cols_to_scale], bins=25, ec='black')
    plt.title('Scaled')
    
    return train_scaled, validate_scaled, test_scaled