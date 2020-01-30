# An Autism Spectrum Disorder Screening Machine Learning Analysis
##### *522 Workflows: Group \#414*
Members: Tejas Phaterpekar, Matthew Connell, Thomas Pin

## Data Description

Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition that impairs social interpretation/communication ability, as well as the presence of repetitive behaviors. Current diagnostic procedures are lengthy and inefficient. Affecting 1.5% of the population, with many more cases going undetected, an easy-to-implement, effective screening method is warranted. ASDTest, a mobile app, has been introduced to provide an accessible screening method that tells the user whether they should seek formal healthcare opinions, based on a 10 question survey<sup>1,2</sup>. The ability to recognize and diagnose ASD at an early age can allow the affected to access the healthcare resources and support they will need, in a timely manner. 



The Autism Spectrum Quotient-10<sup>3</sup> (AQ-10) consists of 10 questions intended to differentiate characteristics of autism in adults. Each question has four possible answers: "Definitely Agree", "Slightly Agree, "Slightly Disagree", and "Definitely Disagree". For questions 1, 7, 8, and 10, a value of 1 is assigned for either a "slightly agree" or a "definitely agree" response. For questions 2, 3, 4, 5, 6, and 9, a value of 1 is assigned for either a "slightly disagree" or a "definitely. disagree" response. A cumulative score is calculated for each individual, which is then used to recommend a healthcare opinion. An individual who receives a total score of greater than 6 is recommended for a specialist diagnostic assessment.

The dataset contains survey results and background information for 704 adults. The [data<sup>4</sup>](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult) was obtained from the University of California Irvine Machine learning Repository<sup>5</sup>.

### Variable Definitions

1. **A1_score** (Int; 0, 1) Prompt: I often notice small sounds when others do not

2. **A2_score** (Int; 0, 1) Prompt: I usually concentrate more on the whole picture, rather than the small details

3. **A3_score** (Int; 0, 1) Prompt: I find it easy to do more than one thing at once

4. **A4_score** (Int; 0, 1) Prompt: If there is an interruption, I can switch back to what I was doing very quickly

5. **A5_score** (Int; 0, 1) Prompt: I find it easy to 'read between the lines' when someone is talking to me

6. **A6_score** (Int; 0, 1) Prompt: I know how to tell if someone listening to me is getting bored

7. **A7_score** (Int; 0, 1) Prompt: When I'm reading a story I find it difficult to work out the characters' intentions

8. **A8_score** (Int; 0, 1) Prompt: I like to collect information about categories of things(e.g. types of car, types of bird, types of train, types of plant etc)

9. **A9_score** (Int; 0, 1) Prompt: I find it easy to work out what someone is thinking or feeling just by looking at their face

10. **A10_score** (Int; 0, 1) Prompt: I find it difficult to work out people's intentions

11. **Age** - (int) Age in years

12. **Gender** - (String) M or F

13. **Ethnicity** (String)  Common Ethnicities defined for each individual

14. **Born with jaundice?** (String; yes or no) Was individual born with jaundice?

15. **Autism** (String; yes or no) Was individual diagnosed with autism? 

16. **Country of residence** (String) 

17. **Used the screening app before?** Boolean (yes or no) Whether the user has used a screening app

18. **Result** (Int) The final score obtained based on the scoring algorithm of the screening method used. This was computed in an automated manner.

19. **age_desc** (String) Age group
20. **relation** (String) Parent, self, caregiver, medical staff, clinician ,etc.


**Target** - ASD Classification (yes if final score > 6; no if final score <= 6)

## Research Questions

**Main Question: What top three feature most strongly predict whether an individual will be diagnosed with Autism Spectrum Disorder? (Predictive)**

*Sub-Questions:*

- Does predictor importance change if we separate the data based on gender? (predictive)

- Do AQ-score features matter more than background features (sex, ethnicity, relation) when classifying for ASD? (predictive)

- What is the proportion of females that are diagnosed with Autism Spectrum Disorder? (Descriptive)

- Is gender or age a factor that affects the diagnoses of individuals with Autism Spectrum Disorder in a set of data? (Exploratory)

- Is age correlated with the diagnoses of Autism Spectrum Disorder? (Inferential)

- Is using screening apps before the diagnoses correlated with the diagnoses of Autism Spectrum Disorder? (Inferential)

- What Autism Spectrum Disorder Classification will be assigned to an individual who takes the Autism Spectrum Quotient-10?
(Predictive)

- What score from the Autism Spectrum Quotient-10 is the strongest predictor of an individual being diagnosed with Autism Spectrum Disorder? (Predictive)

## Plan of Action

After splitting the data into training and test sets, we plan to conduct an exploratory analysis to detect interesting trends in the data, and determine whether any preprocessing will be required. We will proceed to train multiple classifier models such as KNN and RandomForest. GridSearchCV will be used to optimize hyperparameters for all models and Cross-Validation. Additionally, we hope to implement a pipeline to make our machine learning methodology as reproducible as possible. We will assess each model's performance on the training data and extract information about what features are considered important to the classification results. We will also place a strong emphasis on determining the types of error we encounter with our models, using confusion matrices. 

To address reproducibility, we plan to implement an analysis pipeline that will streamline all relevant scripts within one file that can be run from the command line.

### Planned Scripts 
- download_data.py -> downloads data with a command line executable
- tidy_data.py -> tidies data 
- exploratory_plot.R -> contains code for exploratory analysis/plots
- machine_learning_predict.py -> contains code for our machine learning procedures

## EDA Discussion

We plan to create a summary table of all the columns to identify the ranges for each feature and discover any potential outliers. We can also take advantage of the binomial nature of our AQ-10 question features to find the proportion of each question that was answered with a 'yes' (using the mean from the table). One exploratory plot that will be created is a correlational heatmap which will give us insight into potential relationships between predictors and the target variable, as well as any multicolinearity. 

[EDA](https://github.com/UBC-MDS/522-Workflows-Group-414/blob/master/src/EDA_autism-screening.ipynb)

## Sharing the Results

A final report will be written in markdown to summarize the problem, question, and our findings. We will have tables containing the different models we trained and their performance on the training and test datasets. We will display confusion matrices for each model to understand differences between precision and recall across the different models. We also want to provide the readers a visual on feature importance in our models. Currently, we are looking to create a heatmap that will have model type on the x-axis and feature name on the y-axis, with a color gradient representing importance. The metric that will determine importance will be confirmed after we finalize our EDA and model selection, but before we start training the models.  


## References: 

1. Thabtah, F. 2018. "An accessible and efficient autism screening method for behavioural data and predictive analyses". 25(4):1739-1755. Health Informatics Journal.[https://doi.org/10.1177/1460458218796636](https://journals.sagepub.com/doi/full/10.1177/1460458218796636?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub%3Dpubmed)

2. Allison, C., Auyeung, B., and Baron-Cohen, S. 2012. "Toward brief 'Red Flags' for autism screening: The Short Autism Spectrum Quotient and the Short Quantitative Checklist for Autism in toddlers in 1,000 cases and 3,000 controls". 51(2):202-212. J Am Acad Child Adolesc Psychiatry.[https://doi.org/10.1016/j.jaac.2011.11.003](https://www-sciencedirect-com.proxy.lib.sfu.ca/science/article/pii/S0890856711010331#!)

3. [Autism Spectrum Quotient-10 Survey (AQ-10)](https://www.nice.org.uk/guidance/cg142/resources/autism-spectrum-quotient-aq10-test-pdf-186582493).

4. [UCI Dataset Respository](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult).

5. Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences.[http://archive.ics.uci.edu/ml/index.php](http://archive.ics.uci.edu/ml).
