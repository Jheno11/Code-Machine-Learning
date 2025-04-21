# Code-Machine-Learning

# 1. Title :

- Project Name : Designing AI system to diagnose prostate cancer in race specific patients

- Gene Expression : HTSeq - Counts gene expression

- Phenotype : GDC TCGA-PRAD phenotype

# 2. Code/Dataset Description :

- This paper used 5 different codes for separating race, DEG analysis, ROC analysis, White race model and Black race model

- This paper used gene expression and phenotype dataset for prostate cancer detection

# 3. Dataset Information :

- Gene Expression Dataset consist of the gene data from various samples, link : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.star_counts.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

- Phenotype Dataset consist of numerous clinical information about the patient, link : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.clinical.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

# 4. Code Infromation :

- Race.ipynb file is a code for grouping the sample to white race

- DEGdeseq2.ipynb file is a data preprocessing and feature selection method where this study use to find outlier gene base on basemean, padj and log2foldchange

- ROC analysis.ipynb file is a feature selection method where this study use to find outlier gene by finding significant value

- Combine dataset.ipynb is a file where this study used to combine the dataset value from deseq2 based on the Ensembl_ID

- ResultsWhiteRace.py is a file where this study used to check the result by using naive bayes

- ResultsBlackRace.py is a file this study used to validate the model by using different race

# 5. Usage Instruction :

- Load gene expression and phenotype dataset using pandas library and separate the data by race using Race.ipynb file

- Load the specific race dataset from Race file to perform data preprocessing and DEG to find outlier gene using DEGdeseq2.ipynb file

- Load data139.csv to perform ROC analysis using ROC analysis.ipynb file

- load data13.csv, data139.csv, data4.csv and data7.csv using ResultsWhiteRace.py dataset to perform white race modelling with Gaussian Naive Bayes Algorithm

- load Datablack13.csv, Datablack13.csv, Datablack7.csv and Datablack4.csv using ResultsBlackRace.py to perform validation on another race

# 6. Requirement :

- Pandas Library

- Numpy Library

- scikit-learn Library

- imbalance-learn Library

# 7. Methodology for Code Usage :

- Use race.ipynb file to separate the race using gene expression and phenotype dataset

- next step do DEGdeseq2 to find the outlier gene for further analysis

- next use Combine file to combine the DEG dataset with raw data to get the value

- for 139 features use ROC analysis to find more significant gene

- lastly use ResultsWhiteRace and ResultsBlackRace to find the model for white race and validate using black race

# 8. Citation - Not Applicable

# 9. License & Contribution Guidelines - Not Applicable
