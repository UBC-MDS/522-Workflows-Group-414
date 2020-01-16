# An Autism Spectrum Disorder Screening Analysis
##### *522 Workflows: Group \#414*

## Data Description

Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition that impairs social interpretation/communication ability, as well as the prescence of repetitive behaviors. Current diagnostic procedures are lengthy and inefficient. Affecting 1.5% of the population, with many more cases going undetected, a easy-to-implement, effective screening method is warranted. ASDTest, a mobile app, has been introduced to provide an accessible screening method that tells the user whether they should seek formal healthcare opinions, based on a 10 question survey. 

### Variable Definitions

1. **A1_score** (Int; 0, 1) Prompt: S/he often notices small sounds when others do not

11. **A2_score** (Int; 0, 1) Prompt: S/he usually concentrates more on the whole picture, rather than the small details

12. **A3_score** (Int; 0, 1) Prompt: In a social group, s/he can easily keep track of several different people’s conversations

13. **A4_score** (Int; 0, 1) Prompt: S/he finds it easy to go back and forth between different activities

14. **A5_score** (Int; 0, 1) Prompt: S/he doesn’t know how to keep a conversation going with his/her peers

15. **A6_score** (Int; 0, 1) Prompt: S/he is good at social chit-chat

16. **A7_score** (Int; 0, 1) Prompt: When s/he is read a story, s/he finds it difficult to work out the character’s intentions or feelings

17. **A8_score** (Int; 0, 1) Prompt: When s/he was in preschool, s/he used to enjoy playing games involving pretending with other children

18. **A9_score** (Int; 0, 1) Prompt: S/he finds it easy to work out what someone is thinking or feeling just by looking at their face

19. **A10_score** (Int; 0, 1) Prompt: S/he finds it hard to make new friends

1. **Age** - (int) Age in years

2. **Gender** - (String) M or F

3. **Ethnicity** (String)  Common Ethnicities defined for each individual

4. **Born with jaundice?** (String; yes or no) Was individual born with jaundice?

9. **Autism** (String; yes or no) Was individual diagnosed with autism? (need to confirm this?)

7. **Country of residence** (String) 

8. **Used the screening app before?** Boolean (yes or no) Whether the user has used a screening app

20. **Result** (Int) The final score obtained based on the scoring algorithm of the screening method used. This was computed in an automated manner.

7. **age_desc** (String)

6. **relation** (String) Parent, self, caregiver, medical staff, clinician ,etc.



Target - ASD Classification (yes if final score > 6; no if final score <= 6)

## Research Questions

## Plan of Action



References: 

(https://journals.sagepub.com/doi/full/10.1177/1460458218796636?url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org&rfr_dat=cr_pub%3Dpubmed)

(https://www-sciencedirect-com.proxy.lib.sfu.ca/science/article/pii/S0890856711010331#!)

(https://micmrc.org/system/files/webinars/AQ10-Child.pdf)
