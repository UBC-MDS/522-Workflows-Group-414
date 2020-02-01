# download.py : download am arff file from within a zipped file from a given url
# author: Matthew Connell, Thomas Pin and Tejas Phaterpekar
# date: 2020-01-15

"""Downloads .zip url to current folder, unzips arff file, loads data, splits data and saves original CSV, as well as train/test splits into a data folder. Currently supports only .zip URLs with a .arff file inside.

Usage: download.py --url=<url> --zip_folder=<zip_folder> --data_name=<data_name>

Options:
--url=<url>                 URL for the .zip file to be downloaded
--zip_folder=<zip_folder>   name of the zip folder at the url
--data_name=<data_name>     name of the file within the zip folder
"""

from docopt import docopt
import zipfile
import pandas as pd
import urllib
import requests
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.io import arff
import os
import _io

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00426/Autism-Adult-Data%20Plus%20Description%20File.zip"
# zip_folder = "../data/autism_screening.zip"
# data_name = Austism-Adult-Data


opt = docopt(__doc__) 

def main(url, zip_folder, data_name):

    # send request and save object
    # Test
    # Throw error if URL is incorrect
    try:
        r = requests.get(url)
        assert(r.status_code == 200)
    except Exception as req:
        print("You have entered an invalid URL")
        print(req)

    # extract content of response object 'r' and write to specified filename
    new_directory = zip_folder.split('/')
    new_directory = new_directory[0]
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    
    # open the zip folder and write binary content to disk
    # Test to make sure file is a zipfile, raise comprehensable exception
    try:
        with open(zip_folder, 'wb') as f:
            assert(type(f) == _io.BufferedWriter)
            f.write(r.content)
    except Exception as bad_zip:
        print("This is not a zip file")

    # Extract the arff file located in the zipped folder using python library zipfile
    arff_file = data_name+".arff"
    with zipfile.ZipFile(zip_folder, 'r') as myzip:
        myzip.extract(arff_file)

    # Use 'scipy.io.arff' library to read in arff file
    data = arff.loadarff(arff_file)

    # The arff file contains a csv in element 0 and a description of the variables in element 1
    df = pd.DataFrame(data[0], dtype='str')

    # Write uncleaned csv to disk
    df.to_csv("data/"+data_name+".csv", index=False)


    # Attribution:
    # https://stackoverflow.com/questions/29754980/basic-docopt-example-does-not-work
    # https://stackoverflow.com/questions/3451111/unzipping-files-in-python
    # https://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    # https://discuss.analyticsvidhya.com/t/loading-arff-type-files-in-python/27419
    # https://www.geeksforgeeks.org/get-post-requests-using-python/
    # https://github.com/ttimbers/breast_cancer_predictor/blob/master/src/download_data.py

if __name__ == "__main__":
  main(opt["--url"], opt["--zip_folder"], opt["--data_name"])