# authors: Tejas Phaterpekar, Matthew Connell, Thomas Pin

'''This script concatenates 3 separate ASD dataframes, relating to children, adolescents and adults. 
It then splits the data into training and test sets, before proceeding to clean missing values and erroneous column/values.

Usage: python split_and_clean.py --child_path=<child_path> --adult_path=<adult_path> --adol_path=<adol_path>

Options: 
--child_path=<child_path>  Relative file path for the child_autism file
--adult_path=<adult_path>  Relative file path for the adult_autism file
--adol_path=<adol_path>   Relative file path for the adolescent autism file

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
def main(child_path, adult_path, adol_path):
    # code for "guts" of script goes here

# code for other functions & tests goes here

# call main function
if __name__ == "__main__":
    main()