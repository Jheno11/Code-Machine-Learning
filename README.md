# Code-Machine-Learning

1. DEGdeseq2 file is a festure selection method where this study use to find outlier gene base on basemean, padj and log2foldchange

2. ROC analysis file is a feature selection method where this study use to find outlier gene by finding significant value

3. Combine dataset is a file where this study used to combine the dataset value from deseq2 based on the Ensembl_ID

4. ResultsWhiteRace is a file where this study used to check the result by using naive bayes

5. ResultsBlackRace is a file this study used to validate the model by using different race

6. The implementation used is DEGdeseq2, ROC analysis, Combine dataset, ResultsWhiteRace and lastly ResultsBlackRace

7. Link Raw Data for gene expression data set : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.star_counts.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

8. Link Raw Data for phenotype : https://xenabrowser.net/datapages/?dataset=TCGA-PRAD.clinical.tsv&host=https%3A%2F%2Fgdc.xenahubs.net&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443

Step Implementation

1. Use race ipynb file to separate the race using raw data

2. next step do DEGdeseq2 to find the outlier gene for further analysis

3. next use Combine file to combine the DEG dataset with raw data to get the value

4. for some feature use ROC analysis to find more significant gene

5. lastly use ResultsWhiteRace and ResultsBlackRace to find the model for white race and validate using black race
