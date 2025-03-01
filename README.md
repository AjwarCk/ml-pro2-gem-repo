<span style="font-family: Menlo, monospace;">

## End to End Machine Learning Project2.

## Gemstone Price Prediction - 

## Introduction About the Data : 

The dataset, the goal is to predict price of given diamond (Regression Analysis).

There are 10 independent variables (including id):

- id : unique identifier for each diamond
- carat : carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstone and diamonds.
- cut: quality of dimond cut.
- color : color of diamond.
- clarity : diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics udner 10-power magnification.
- depth: the depth of diamond is its height (in millimeters) measured from the cutlet (bottom tip) to the table (flat, top surface).
- table: A diamond's table is the facet which canb be seen when the stone is viewed face up.
- x : diamond X dimension.
- y : diamond y dimension.

##### Target Variables :

- price : price of the given diamond.

Dataset Source Link : https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

**It is observed that the categorical variables 'cut','color' and 'clarity' are ordinal in nature.**

**Check this link for in-depth:** : [American Gem] (https://www.americangemsociety.org/ags-diamond-grading-system/)


### Approach for the project

1. Data Ingestion :

    - In Data Ingestion phase the data is first read as csv.
    - The the data is split into train and test and saved as csv file.

2. Data Transformation : 

    - In this phase a column transformation pipeline is created.
    - For numeric variables first simpleimputer is applied with strategy median, then standard scaling is performed on numeric data.
    - For categorical variables simpleimputer with most freequent strategy, then ordinal encoding performed, after this data is scaled with standard Scaler.
    - This preprocessor is saved as pickle file.

3. Model Training : 

    - In this phase base model is tested. The best model found was catboost regressor.
    - Post this hyperparameter tuning is performed on catboost and knn model.
    - A final votingregressor is created which will combine prediction of catboost, xgboost and knn models.
    - This model is saved as pickle file.

4. Prediction Pipeline : 

    - This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flast App Creation :

    - Flask app is created with user interface to predict the gemstone prices inside a Web Application.


## Exploratory Data Analysis Notebook :

Link : [EDA_Notebook] ()

## Model Training Approach Notebook : 

Link : [Model_Training_Notebook] ()

## Model Interpretation with LIME

Link : [LIME] ()

</span>%