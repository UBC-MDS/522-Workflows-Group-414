# authors: Tejas Phaterpekar
# Date written: 01-25-2020
# This script takes in the ASD adults dataset.It then splits the data into training and test sets, 
# before proceeding to clean missing values and erroneous column/values.

'''This script takes in the ASD adults dataset. 
It then splits the data into training and test sets, before proceeding to clean missing values and erroneous column/values.

Usage: split_and_clean.py --adult_path=<adult_path> 


Options: 
--adult_path=<adult_path>   :   Relative file path for the adult_autism csv

'''

# import libraries/packages
from docopt import docopt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.io import arff


# parse/define command line arguments here
opt = docopt(__doc__)

# define main function
def main(adult_path):
    print("working")
    autism_df = pd.read_csv(adult_path)

    # Introduce nan values for any nonsense values; then remove any rows containing these
    autism_df = autism_df.replace("?", np.nan)
    autism_df = autism_df.replace("[Oo]thers", np.nan, regex = True)
    autism_df = autism_df.dropna(axis = 0)

    # we filter out the 1 row that has an extreme age value of 380
    autism_df = autism_df.query("age < 120")

    # split the data (used random state for reproducibility)
    X_train, X_test, y_train, y_test = train_test_split(autism_df.drop(columns = ['austim']), autism_df['austim'], test_size = 0.2, random_state = 55)

    X_train = clean_feature_data(X_train)
    X_test = clean_feature_data(X_test)

    y_train = clean_target_data(pd.DataFrame(y_train))
    y_test = clean_target_data(pd.DataFrame(y_test))

    check_compatability(X_train, y_train)
    check_compatability(X_test, y_test)

    X_train.to_csv("data/clean-data/Xtrain-clean-autism-screening.csv", index = True)
    y_train.to_csv("data/clean-data/ytrain-clean-autism-screening.csv", index = True, header = True)

    X_test.to_csv("data/clean-data/Xtest-clean-autism-screening.csv", index = True)
    y_test.to_csv("data/clean-data/ytest-clean-autism-screening.csv", index = True, header = True)


# code for other functions & tests goes here
def clean_feature_data(feature_df):
    '''
    Takes in a feature df and cleans column names, value types, and corrects erroenous values

    Arguments:

    feature_df - (DataFrame) Feature dataframe

    Returns Cleaned Dataframe
    '''

    # Clean up column names
    feature_df.rename(columns = {'jundice':'jaundice', 'austim': 'autism', 'contry_of_res':"country_of_res"}, inplace = True)

    # Drop unecessary columns (will move this to a future script)
    feature_df.drop(columns = ['age_desc', 'result', 'Class/ASD'])

    # AQ had 4 unique values which didn't make sense; this loop restricts unique values to 0 and 1 integers
    # loop goes over the AQ-score columns corrects type formatting
    for column in feature_df:

        if "Score" in column:
            feature_df[column] = pd.to_numeric(feature_df[column])
            print(feature_df[column].value_counts())
            print("")


    # Changing appropriate columns from strings to numeric form
    feature_df['age'] = pd.to_numeric(feature_df['age'], downcast = 'integer')
    feature_df['result'] = pd.to_numeric(feature_df['result'], downcast = 'integer')
  


    # Correcting any string errors
    feature_df['relation'] = feature_df['relation'].replace("self", "Self")
    feature_df['relation'] = feature_df['relation'].str.replace("'","")

    feature_df['ethnicity'] = feature_df['ethnicity'].replace("'Middle Eastern '", "Middle Eastern")
    feature_df['ethnicity'] = feature_df['ethnicity'].replace("'South Asian'", "South Asian")
    
    feature_df['age_desc'] = feature_df['age_desc'].replace("'4-11 years'", "4-11 years")
    feature_df['age_desc'] = feature_df['age_desc'].replace("12-15 years", "12-16 years")
    
    feature_df['country_of_res'] = feature_df['country_of_res'].str.replace("'","")
    feature_df['country_of_res'] = feature_df['country_of_res'].replace("Viet Nam", "Vietnam")

    # Removing age outlier
 

    return feature_df

def clean_target_data(target_df):
    '''
    Takes in a target df and cleans column names, value types, and corrects erroenous values

    Arguments:

    target_df - (DataFrame) Target dataframe

    Returns Cleaned Dataframe
    '''

    # Clean up column names
    target_df.rename(columns = {'austim': 'autism'}, inplace = True)

    return target_df

def check_compatability(feature_df, target_df):
    '''
    Takes in X and y dataframes and makes sure their shape is compatible

    Arguments:

    feature_df - (DataFrame) Feature dataframe
    target_df - (DataFrame) Target dataframe

    Returns an error if incompatible

    '''

    assert feature_df.shape[0] == target_df.shape[0], "X and y shapes don't match!"
    return
    
# call main function
if __name__ == "__main__":
    main(opt["--adult_path"])