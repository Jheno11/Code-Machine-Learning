# Code-Machine-Learning

Dataset Title :

- Gene Expression : HTSeq - Counts gene expression

- Phenotype : GDC TCGA-PRAD phenotype

Code/Dataset Description :

- Race file is a code for grouping the sample to white race

- DEGdeseq2 file is a feature selection method where this study use to find outlier gene base on basemean, padj and log2foldchange

- ROC analysis file is a feature selection method where this study use to find outlier gene by finding significant value

- Combine dataset is a file where this study used to combine the dataset value from deseq2 based on the Ensembl_ID

- ResultsWhiteRace is a file where this study used to check the result by using naive bayes

- ResultsBlackRace is a file this study used to validate the model by using different race

- Gene Expression Dataset consist of the gene data from various samples, link provided below

- Phenotype Dataset consist of numerous clinical information about the patient, link provided below

- Link Raw Data for gene expression data set : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.star_counts.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

- Link Raw Data for phenotype : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.clinical.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

Usage Instruction :

- The code can be used using python with pandas library to load dataset

Requirement :

- Pandas Library

- Numpy Library

- scikit-learn Library

- imbalance-learn Library

Methodology for Code Usage :

1. Use race ipynb file to separate the race using raw data

2. next step do DEGdeseq2 to find the outlier gene for further analysis

3. next use Combine file to combine the DEG dataset with raw data to get the value

4. for some feature use ROC analysis to find more significant gene

5. lastly use ResultsWhiteRace and ResultsBlackRace to find the model for white race and validate using black race
