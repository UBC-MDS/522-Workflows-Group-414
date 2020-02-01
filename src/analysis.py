# analysis.py : take train/test csvs and fit a Decision tree model. Output ROC curve and confusion matrices.
# author: Matthew Connell, Thomas Pin and Tejas Phaterpekar
# date: 2020-01-22

"""Import .csv in data folder to be split and analyzed by machine learning models. Outputs 2 .csv files which are confusion matrices. Outputs ROC chart with final model.

Usage: analysis.py --train_X=<train> --test_X=<test> --train_y=<train_y> --test_y=<test_y>  --conf1=<conf1> --conf2=<conf2> --roc_path=<roc_path>

Options:
--train_X=<train>                 path for the X-train set
--test_X=<test>                   path for the X-test set
--train_y=<train>                 path for the y-train set
--test_y=<test>                   path for the y-test set
--conf1=<conf1>                 path for the first confusion matrix
--conf2=<conf2>                 path for the second confusion matrix
--roc_path=<roc_path>           path for the roc chart matrix
"""

### In the terminal, in your root directory for the project, type:
### python src/analysis.py --train_X=data/clean-data/Xtrain-clean-autism-screening.csv --test_X=data/clean-data/Xtest-clean-autism-screening.csv --train_y=data/clean-data/ytrain-clean-autism-screening.csv --test_y=data/clean-data/ytest-clean-autism-screening.csv --conf1=data/conf1 --conf2=data/conf2 --roc_path=img/ROC.png

from docopt import docopt
import pandas as pd
import numpy as np

# Preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer

# Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Metrics
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report, roc_curve

# Model selection
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.pipeline import Pipeline

# Feature selection
from sklearn.feature_selection import RFE

# Plotting
import altair as alt

# Suppress warnings
import warnings
from sklearn.exceptions import FitFailedWarning

opt = docopt(__doc__) 

def main(train_X, test_X, train_y, test_y, conf1, conf2, roc_path):

    np.random.RandomState(414)

    warnings.filterwarnings(action='ignore', category=FitFailedWarning)

    # import the already split datasets
    X_train = pd.read_csv(train_X, index_col=0)
    y_train = pd.read_csv(train_y, index_col=0)
    X_test = pd.read_csv(test_X, index_col=0)
    y_test = pd.read_csv(test_y, index_col=0)


    # Test that X_train has more rows the X_test
    try:
        assert(X_train.shape[0] > X_test.shape[0])
    except Exception as bad_size:
        print("X_train should have more rows than X_test.\nDid you put them in the wrong order?")

    # Make validation set 
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=414)

    numeric_features = ["age", 
                        "result"]

    one_hot_features = ["gender", 
                        "ethnicity", 
                        "jaundice", 
                        "country_of_res", 
                        "used_app_before", 
                        "age_desc", 
                        "relation",
                        "Class/ASD"]

    other_columns = list(X_train.columns[0:10])

    preprocessor = ColumnTransformer(sparse_threshold=0,
        transformers=[
            ("scale", 
            StandardScaler(), 
            numeric_features),
            ("one_hot", 
            OneHotEncoder(drop=None, 
                        handle_unknown="ignore"), 
            one_hot_features)
        ])

    X_train_temp = pd.DataFrame(preprocessor.fit_transform(X_train), 
                index = X_train.index,
                columns = (numeric_features + 
                        list(preprocessor
                            .named_transformers_["one_hot"]
                            .get_feature_names(one_hot_features)))
                        )

    X_test_temp = pd.DataFrame(preprocessor.transform(X_test),
                        index = X_test.index,
                        columns = X_train_temp.columns)

    X_valid_temp = pd.DataFrame(preprocessor.transform(X_valid),
                        index = X_valid.index,
                        columns = X_train_temp.columns)

    X_train = X_train_temp.join(X_train[other_columns])
    X_test = X_test_temp.join(X_test[other_columns])
    X_valid = X_valid_temp.join(X_valid[other_columns])

    le = LabelEncoder()

    y_train = le.fit_transform(y_train.to_numpy().ravel())
    y_test = le.transform(y_test.to_numpy().ravel())
    y_valid = le.transform(y_valid.to_numpy().ravel())

    ## Trying Gridsearch on different models to find best

    ## Initialize models
    # lr = LogisticRegression()
    dt = DecisionTreeClassifier(random_state=414)
    rf = RandomForestClassifier(random_state=414)
    svm = SVC(random_state=414)
    knn = KNeighborsClassifier()

    # Make list for models and a list to store their values
    estimators = [dt, rf, svm, knn]
    best_parameters = []
    best_precision_scores = []

    # Make list of dictionaries for parameters
    params = [#{'C':[0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
            #'penalty': ['l1', 'l2']},
            {'max_depth': [1, 5, 10, 15, 20, 25, None],
            'max_features': [3, 5, 10, 15, 20, 50, None]},
            {'min_impurity_decrease': [0, 0.25, 0.5],
            'max_features': [3, 5, 10, 20, 50, 'auto']},
            {'C':[0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
            'gamma':[0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]},
            {'n_neighbors': [2, 5, 10, 15, 20, 50, 100],
            'algorithm': ['auto', 'brute']}]

    # Run for loop to best parameters for each model
    # Scoring = recall to reduce false positives
    for i in range(len(estimators)):
        search = GridSearchCV(estimator=estimators[i], 
                            param_grid=params[i],
                            cv = 10,
                            n_jobs=-1,
                            scoring='recall')
        
        search_object = search.fit(X_train, y_train)
        
        # Store the output on each iteration
        best_parameters.append(search_object.best_params_)
        best_precision_scores.append(search_object.best_score_)

    best_parameters[np.argmax(best_precision_scores)]


    # the best precision score comes from a decision tree classifier with max_depth=15 and max_features=50
    # and precision = 0.46

    dt = DecisionTreeClassifier(max_depth=15, max_features=50)
    dt.fit(X_train, y_train).score(X_train, y_train)


    # It gets almost perfect on the train set

    dt.score(X_valid, y_valid)

    # and ~81% on the validation set

    prelim_matrix = pd.DataFrame(confusion_matrix(y_valid, dt.predict(X_valid)))


    preliminary_matrix = prelim_matrix.rename(columns={0:"Predicted no autism", 1:'Predicted autism'}, 
                index={0:"Does not have autism", 1:'Has autism'})

    preliminary_matrix.to_csv(conf1)

    #print(classification_report(y_test, dt.predict(X_test)))

    ## Subset just the questions:

    questions = ['A1_Score',
        'A2_Score',
        'A3_Score',
        'A4_Score',
        'A5_Score',
        'A6_Score',
        'A7_Score',
        'A8_Score',
        'A9_Score',
        'A10_Score']

    questions_train_df = X_train[questions]

    questions_valid_df = X_valid[questions]

    questions_test_df = X_test[questions]



    # Attribution: Varada Kolhatkar

    class ForwardSelection:
        def __init__(self, 
                    model, 
                    min_features=None, 
                    max_features=None, 
                    scoring=None, 
                    cv=None):
            """
            Initialize a Forward selection model
            """
            self.max_features = max_features
            if min_features is None:
                self.min_features = 1
            else:
                self.min_features = min_features

            self.model = model
            self.scoring = scoring
            self.cv = cv
            self.ftr_ = []
            return
        
        def fit(self, X, y):
            """
            Fit a forward selection model        
            """
            
            error = np.inf
            best = None
            feature_index = list(range(0, (X.shape[1])))
            errors = []
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=514)

            X_temp = X_train

            while error > 0.0:
                if best is not None:
                    if best not in feature_index:
                        del feature_index[-2]
                        break
                    feature_index.remove(best)

                for i in feature_index:
                    self.model.fit(X_temp[:, self.ftr_ + [i]], y_train)
                    temp_error = 1-np.mean(cross_val_score(self.model, X[:, self.ftr_ + [i]], y, scoring='f1'))

                    if temp_error < error:
                        error = temp_error
                        best = i

                errors.append(round(error, 3))

                if len(errors) > 2:
                    if errors[-1] >= errors[-2]:
                        break

                if self.max_features is not None:
                    if len(errors) > self.max_features:
                        break

                self.ftr_.append(best)


        def transform(self, X, y=None):
            """
            Transform a test set        
            """
            return X[:, self.ftr_]
        

    fs = ForwardSelection(DecisionTreeClassifier(), max_features=None)

    fs.fit(questions_train_df.to_numpy(), y_train)

    fs.ftr_

    # No single one question is better than any other one question so forward selection won't work
    # Or it just won't work with a decision tree


    rfe =RFE(DecisionTreeClassifier(), n_features_to_select=5)

    rfe.fit(questions_train_df, y_train)

    # The top 5 questions:

    top_five = np.where(rfe.ranking_ == 1)[0]

    X_train_best_5 = questions_train_df.to_numpy()[:,top_five]
    X_test_best_5 = questions_test_df.to_numpy()[:,top_five]
    X_valid_best_5 = questions_valid_df.to_numpy()[:,top_five]

    dt2 = DecisionTreeClassifier()

    dt2.fit(X_train_best_5, y_train)

    pd.DataFrame(confusion_matrix(y_valid, dt2.predict(X_valid_best_5)))

    # Using just the top 5 questions gets a much worse result than using all the features


    # Try all questions:
    dt3 = DecisionTreeClassifier()

    dt3.fit(questions_train_df, y_train)

    conf_matrix = pd.DataFrame(confusion_matrix(y_test, dt.predict(X_test)))

    final_matrix = conf_matrix.rename(columns={0:"Predicted no autism", 1:'Predicted autism'}, 
                index={0:"Does not have autism", 1:'Has autism'})

    final_matrix.to_csv(conf2)

    # ROC curve

    fpr, tpr, _ = roc_curve(y_test, dt.predict_proba(X_test)[:,1])

    roc_df = pd.DataFrame({"fpr":fpr, "tpr":tpr})

    line_df = pd.DataFrame({"start":[0,1], "end":[0,1]})

    roc = alt.Chart(roc_df).mark_line().encode(
        x = alt.X("fpr:Q"),
        y = alt.Y("tpr:Q")
    )
        
    line = alt.Chart(line_df).mark_line(strokeDash=[5,5], color="orange").encode(
        x = alt.X("start:Q", axis=alt.Axis(title="False Positive Rate")),
        y = alt.Y("end:Q", axis=alt.Axis(title="True Positive Rate"))
    )
        
    chart = (roc + line).configure_axis(titleFontSize=20).properties(title="ROC Curve").configure_title(fontSize=20)

    chart

    chart.save(roc_path)

if __name__ == "__main__":
  main(opt["--train_X"], opt["--test_X"],opt["--train_y"], opt["--test_y"], opt["--conf1"], opt["--conf2"], opt["--roc_path"])