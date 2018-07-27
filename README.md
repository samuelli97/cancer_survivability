# Cancer Survivability Prediction with Machine Learning Models
## Introduction
This repository contains the code relevant to my summer 2018 REU research program at NMSU with faculty advisor Talayeh Razzaghi. I applied traditional machine learning and deep learning models to the National Cancer Institute's Surveillance, Epidemiology, and End Results (SEER) database. This README provides a technical walkthrough of my project and the relevant code.

The research goal was to accurately predict 2-year colorectal cancer survivability (a binary variable indicating whether a patient is alive 2 years after diagnosis). We specifically wanted to focus on the impact of ethnicity. To do this, we compared model performances between the Hispanic and white populations. We also investigated the effects of imbalanced classification  and dimensionality reduction techniques. The exact findings are detailed in the paper in the LaTex folder of this repository.

Data access to the SEER dataset is granted after a form submission to NCI. For details to accessing the SEER database, follow the directions on the access [page](https://seer.cancer.gov/data/access.html). Our project uses the May 2018 SEER dataset.

**Important Note**: Even after being granted SEER data access, releasing pure data instances online is against the agreement. In this repository, many files access data from a '../Data/', '../SEER_raw', or '../SEER_parsed_csv' folder that is not in the repository. Those are local folders where I kept the actual SEER data that requires signing the research agreement to obtain.

## Basic Repository Content Descriptions
### Folders
**SEER-preprocessing**: Contains files which extract data from SEER's pure ASCII format into csv-form.

**ethnicity_codes**: Contains variable index maps for the one-hot encoded instances of each of three datasets.

**LaTex**: Contains the paper written for this project and other LaTex files

### Files
**preprocessing_2year_v2.ipynb**: Data preprocessing on the csv files after SEER-related preprocessing. Includes imputation, one-hot encoding, etc.

**models.ipynb**: Application of machine learning models including logistic regression, random forests, and AdaBoost.

**neural_networks.ipynb**: Application of neural networks.

**Embeddings.ipynb**: Application of [entity embedding](https://arxiv.org/pdf/1604.06737.pdf), a technique which improves performance for instances which contain many sparse categorical variables.

**dimensionality_reduction.ipynb**: Application of PCA and autoencoders.

## Project Outline
### Preprocessing
#### SEER Preprocessing
The SEER files read by our scripts include `read.seer.research.nov17.sas` and the `COLRECT.TXT` file across all time period subdirectories. First we run `get_vars.py` after we make sure `read.seer.research.nov17.sas` is in the same directory. This generates the file `vars.txt` which includes each variable name along with its beginning column and character length within each instance (standardized across all instances).

Next we run `SEER_to_csv.py` which employs the `vars.txt` file previously created. The goal of this file is to compile every `COLRECT.TXT` file from each time period subdirectory into a single csv file where every patient instance is represented as a row of comma-separated values. `SEER_to_csv.py` takes three arguments: The first argument is 't' or 'f', and tells the script whether to print the comma-separated variable names, which we desire at the beginning of the file. We only use 't' when we are running the script for the first time. We run this script once for each `COLRECT.TXT` file. The second argument is the input file to parse, and the third argument is the output file to create or append to. Our runs looked like this:

```
python SEER_to_csv.py 't' COLRECT_1973.TXT COLRECT.TXT
python SEER_to_csv.py 'f' COLRECT_1992.TXT COLRECT.TXT
python SEER_to_csv.py 'f' COLRECT_2000.TXT COLRECT.TXT
```
after we renamed the given SEER `COLRECT.TXT` files. Our output `COLRECT.TXT` file now contains all the parsed colorectal cancer data information in a single file.

### SQL Feature Extraction

#### Data Preprocessing

### Machine Learning models


### Deep Learning models
