url = input("URL to be downloaded: ")
filename = input("Desired filename: ")

import zipfile
import pandas as pd
import urllib
import requests
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.io import arff

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00419/Autism-Screening-Child-Data%20Plus%20Description.zip"
# filename = "autism_screening.zip"

# send request and save object
r = requests.get(url)

# extract content of response object 'r' and write to specified filename
with open(filename, 'wb') as f:
    f.write(r.content)

# Extract the arff file located in the zipped folder using python library zipfile
with zipfile.ZipFile(filename, 'r') as myzip:
    myzip.extract('Autism-Child-Data.arff')

# Use 'scipy.io.arff' library to read in arff file
data = arff.loadarff("Autism-Child-Data.arff")

# The arff file contains a csv in element 0 and a description of the variables in element 1
df = pd.DataFrame(data[0], dtype='str')

# Change dtypes of columns
for col in df.columns[0:10]:
    df[col] = df[col].astype('int')
df['age'] = df['age'].astype('float')
df['result'] = df['result'].astype('float')

# Replace question marks with NAs
for col in df.columns:
    df[col] = df[col].replace('?', 'NA')


#split the data
X = df.drop(['Class/ASD'], axis = 1)
y = df['Class/ASD']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.2,
                                                    random_state=100)

# Write to csv on hard drive
df.to_csv("../data/raw_autism_screening_children.csv", index=False)
X_train.to_csv("../data/raw_autism_screening_children_X_train.csv", index=False)
X_test.to_csv("../data/raw_autism_screening_children_X_test.csv", index=False)

# Adding header=False to suppress warning messages
y_train.to_csv("../data/raw_autism_screening_children_y_train.csv", index=False, header=False)
y_test.to_csv("../data/raw_autism_screening_children_y_test.csv", index=False, header=False)

# Attribution:
# https://stackoverflow.com/questions/3451111/unzipping-files-in-python
# https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
# https://discuss.analyticsvidhya.com/t/loading-arff-type-files-in-python/27419
# https://www.geeksforgeeks.org/get-post-requests-using-python/
