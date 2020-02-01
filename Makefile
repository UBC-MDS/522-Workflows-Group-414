# ASD data pipe
# author: Matthew Connell, Thomas Pin and Tejas Phaterpekar
# date: 2020-01-29

#download
all: data/Autism-Adult-Data.csv data/clean-data/Xtest-clean-autism-screening.csv data/clean-data/Xtrain-clean-autism-screening.csv data/clean-data/ytest-clean-autism-screening.csv data/clean-data/ytrain-clean-autism-screening.csv img/01_corr_heatmap.png img/02_confusion_matrix.png img/03_prop_result.png img/ROC.png data/conf1 data/conf2 doc/ASD_screening_ml_analysis_report.html doc/ASD_screening_ml_analysis_report.md 
	rm -rf Rplots.pdf 
	rm -rf Autism-Adult-Data.arff 


data/Autism-Adult-Data.csv: src/download.py
	python src/download.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/00426/Autism-Adult-Data%20Plus%20Description%20File.zip --zip_folder=data/autism_screening.zip --data_name=Autism-Adult-Data

#preprocessing
data/clean-data/Xtest-clean-autism-screening.csv data/clean-data/Xtrain-clean-autism-screening.csv data/clean-data/ytest-clean-autism-screening.csv data/clean-data/ytrain-clean-autism-screening.csv: src/split_and_clean.py
	python src/split_and_clean.py --adult_path=data/Autism-Adult-Data.csv
	
#run eda 
img/01_corr_heatmap.png img/02_confusion_matrix.png img/03_prop_result.png: src/eda_vis.r
	Rscript src/eda_vis.r --X_train_path=data/clean-data/Xtrain-clean-autism-screening.csv --y_train_path=data/clean-data/ytrain-clean-autism-screening.csv

# Machine learning analysis
img/ROC.png img/all-features-classification-report.png img/final_confusion_matrix.png img/ten-questions-classification-report.png top-five-classification-report.png data/conf1 data/conf2: src/analysis.py
	python src/analysis.py --train_X=data/clean-data/Xtrain-clean-autism-screening.csv --test_X=data/clean-data/Xtest-clean-autism-screening.csv --train_y=data/clean-data/ytrain-clean-autism-screening.csv --test_y=data/clean-data/ytest-clean-autism-screening.csv --conf1=data/conf1 --conf2=data/conf2 --roc_path=img/ROC.png
	
#report 
doc/ASD_screening_ml_analysis_report.html doc/ASD_screening_ml_analysis_report.md: doc/ASD_screening_ml_analysis_report.Rmd doc/asd_refs.bib
	Rscript -e "rmarkdown::render('doc/ASD_screening_ml_analysis_report.Rmd')"
	
clean:
	rm -rf data/Autism-Adult-Data.csv
	rm -rf data/clean-data/Xtest-clean-autism-screening.csv 
	rm -rf data/clean-data/Xtrain-clean-autism-screening.csv 
	rm -rf data/clean-data/ytest-clean-autism-screening.csv 
	rm -rf data/clean-data/ytrain-clean-autism-screening.csv
	rm -rf img/01_corr_heatmap.png 
	rm -rf img/02_confusion_matrix.png 
	rm -rf img/03_prop_result.png
	rm -rf img/ROC.png
	rm -rf data/conf1 
	rm -rf data/conf2
	rm -rf doc/ASD_screening_ml_analysis_report.html
	rm -rf doc/ASD_screening_ml_analysis_report.md
	rm -rf Autism-Adult-Data.arff
	rm -rf Rplots.pdf
	
	
	
