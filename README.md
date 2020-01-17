# An Autism Spectrum Disorder Screening Analysis
##### *522 Workflows: Group \#414*

## Data Description

Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition that impairs social interpretation/communication ability, as well as the prescence of repetitive behaviors. Current diagnostic procedures are lengthy and inefficient. Affecting 1.5% of the population, with many more cases going undetected, a easy-to-implement, effective screening method is warranted. ASDTest, a mobile app, has been introduced to provide an accessible screening method that tells the user whether they should seek formal healthcare opinions, based on a 10 question survey. 

The Autism Spectrum Quotient-10 (AQ-10) consists of 10 questions intended to differentiate characteristics of autism in children aged 4-11. Each questions has four possible answers: "Definitely Agree", "Slightly Agree, "Slightly Disagree", and "Definitely Disagree". For questions 1, 5, 7, and 10, a value of 1 is assigned for either a "slightly agree" or a "definitely agree" response. For questions 2, 3, 4, 6, 8, and 9, a value of 1 is assigned for either a "slightly disagree" or a "definitely. disagree" response. A cumulative score is calculated for each individual, which is then used to reccommend a healthcare opinion. Any total score with a value greater than 6 is classified as potential autism and that individual is recommended for a specialist diagnostic assessment.

### Variable Definitions

1. **A1_score** (Int; 0, 1) Prompt: S/he often notices small sounds when others do not

2. **A2_score** (Int; 0, 1) Prompt: S/he usually concentrates more on the whole picture, rather than the small details

3. **A3_score** (Int; 0, 1) Prompt: In a social group, s/he can easily keep track of several different people’s conversations

4. **A4_score** (Int; 0, 1) Prompt: S/he finds it easy to go back and forth between different activities

5. **A5_score** (Int; 0, 1) Prompt: S/he doesn’t know how to keep a conversation going with his/her peers

6. **A6_score** (Int; 0, 1) Prompt: S/he is good at social chit-chat

7. **A7_score** (Int; 0, 1) Prompt: When s/he is read a story, s/he finds it difficult to work out the character’s intentions or feelings

8. **A8_score** (Int; 0, 1) Prompt: When s/he was in preschool, s/he used to enjoy playing games involving pretending with other children

9. **A9_score** (Int; 0, 1) Prompt: S/he finds it easy to work out what someone is thinking or feeling just by looking at their face

10. **A10_score** (Int; 0, 1) Prompt: S/he finds it hard to make new friends

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

- If a parent takes the test for their child, are there more incorrect ASD classifications/miss-classifications? (Descriptive)

- Do AQ-score features matter more than background features (sex, ethnicity, relation) when classifying for ASD? (predictive)

- What is the proportion of females that are diagnosed with Autism Spectrum Disorder? (Descriptive)


- Is gender or age affect the diagnoses of individuals with Autism Spectrum Disorder in a set of data? (Exploratory)

- Is age correlate with the diagnoses of Autism Spectrum Disorder?(Inferential )

- Is using screening app before the diagnoses correlate with the diagnoses of Autism Spectrum Disorder? (Inferential)

- What Autism Spectrum Disorder Classification will be assigned to an individual who takes the Autism Spectrum Quotient-10?
(Predictive)

- What score from the Autism Spectrum Quotient-10 is the strongest predictor of an individual being diagnoses with Autism Spectrum Disorder? (Predictive)

## Plan of Action

After splitting the data into training and test sets, we plan to conduct an exploratory analysis to detect interesting trends in the data, and determine whether any preprocessing will be required. We will proceed to train multiple classifier models such as KNN and RandomForest. GridSearchCV will be used to optimize hyperparameters for all models. Additionally, we hope to implement a pipeline to make our machine learning methodology as reproducible as possible. We will assess each model's performance on the training data and extract information about what features are considered important to the classification results. We will also place a strong emphasis on determining the types of error we encounter with out models, using confusion matrices. 

To address reproducibility, we plan to implement an analysis pipeline that will streamline all relevant scripts within one file that can be run from the command line.

### Scripts 
- download_data.py
- tidy_data.py
- exploritory_plot.R
- machine_learning_predict.py
  - confusion matrix (diagnostic TP, FN, FP, TN are important)

## Sharing the Results

A final report will be written in markdown to summarize the problem, question, and our findings. We will have tables containing the different models we trained and their performance on the training and test datasets. We will display confusion matrices for each model to understand differences between precision and recall across the different models. To also want to provide the readers a visual on feature importance in our models. Currently, we are looking to create a heatmap that will have model type on the x-axis and feature name on the y-axis, with a color gradient representing importance. The metric that will determine importance will be confirmed after we finalize our EDA and model selection, but before we start training the models.  

References: 

1. [An accessible and efficient autism screening method for behavioural data and predictive analyses by Fadi Thabtah](https://journals.sagepub.com/doi/full/10.1177/1460458218796636?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub%3Dpubmed)

2. [Toward brief “Red Flags” for autism screening: The Short Autism Spectrum Quotient and the Short Quantitative Checklist for Autism in toddlers in 1,000 cases and 3,000 controls by Allison C. et. al.](https://www-sciencedirect-com.proxy.lib.sfu.ca/science/article/pii/S0890856711010331#!)

3. [Autism Spectrum Quotient-Child Version (AQ-10)](https://micmrc.org/system/files/webinars/AQ10-Child.pdf)
