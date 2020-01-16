# An Autism Spectrum Disorder Screening Analysis
##### *522 Workflows: Group \#414*

## Data Description

Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition that impairs social interpretation/communication ability, as well as the prescence of repetitive behaviors. Current diagnostic procedures are lengthy and inefficient. Affecting 1.5% of the population, with many more cases going undetected, a easy-to-implement, effective screening method is warranted. ASDTest, a mobile app, has been introduced to provide an accessible screening method that tells the user whether they should seek formal healthcare opinions, based on a 10 question survey. 

### Variable Definitions

1. Age Number Age in years

2. Gender String Male or Female

3. Ethnicity String List of common ethnicities in text format

4. Born with jaundice Boolean (yes or no) Whether the case was born with jaundice

5. Family member with PDD Boolean (yes or no) Whether any immediate family member has a PDD

6. Who is completing the test String Parent, self, caregiver, medical staff, clinician ,etc.

7. Country of residence String List of countries in text format

8. Used the screening app before Boolean (yes or no) Whether the user has used a screening app

9. Screening Method Type Integer (0,1,2,3) The type of screening methods chosen based on age category (0=toddler, 1=child, 2= adolescent, 3= adult)

10. Question 1 Answer Binary (0, 1) The answer code of the question based on the screening method used

11. Question 2 Answer Binary (0, 1) The answer code of the question based on the screening method used

12. Question 3 Answer Binary (0, 1) The answer code of the question based on the screening method used

13. Question 4 Answer Binary (0, 1) The answer code of the question based on the screening method used

14. Question 5 Answer Binary (0, 1) The answer code of the question based on the screening method used

15. Question 6 Answer Binary (0, 1) The answer code of the question based on the screening method used

16. Question 7 Answer Binary (0, 1) The answer code of the question based on the screening method used

17. Question 8 Answer Binary (0, 1) The answer code of the question based on the screening method used

18. Question 9 Answer Binary (0, 1) The answer code of the question based on the screening method used

19. Question 10 Answer Binary (0, 1) The answer code of the question based on the screening method used

20. Screening Score Integer The final score obtained based on the scoring algorithm of the screening method used. This was computed in an automated manner.

Target - ASD Classification (yes if final score > 6; no if final score <= 6)

## Research Questions

## Plan of Action



References: 

(https://journals.sagepub.com/doi/full/10.1177/1460458218796636?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub%3Dpubmed)

(https://www-sciencedirect-com.proxy.lib.sfu.ca/science/article/pii/S0890856711010331#!)

(https://micmrc.org/system/files/webinars/AQ10-Child.pdf)
