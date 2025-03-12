### Gemstone Price Prediction - Ajwar CK

#### Introduction About the Data :

The <mark>dataset</mark> The goal is to predict <mark>price<mark> of given diamond (Regression Analysis).

There are 10 independent variables (including id):

- <mark>id</mark> : unique identifier of each diamond
- <mark>carat</mark> : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
- <mark>cut</mark> : Quality of Diamond Cut
- <mark>color</mark> : Color of Diamond
- <mark>clarity</mark> : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
- <mark>depth</mark> : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
- <mark>table</mark> : A diamond's table is the facet which can be seen when the stone is viewed face up.
<mark>x</mark>: Diamond X dimension
<mark>y</mark> : Diamond Y dimension
<mark>z</mark> : Diamond Z dimension

Target variable:

- <mark>price</mark>: Price of the given Diamond.

Dataset Source Link : https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv

**It is observed that the categorical variables 'cut', 'color' and 'clarity' are ordinal in nature**

Check this link for details : Link[American Gem Society](https://www.americangemsociety.org/ags-diamond-grading-system/)

#### AWS Deployment Link :

AWS Elastic Beanstalk link : 

Screenshot of UI
----------------
----------------

#### Approach for the project

1. Data Ingestion :

- In Data Ingestion phase the data is first read as csv.
- Then the data is split into training and testing and saved as csv file.

2. Data Transformation :

- In this phase a ColumnTransformer Pipeline is created.
- for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
- for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
- This preprocessor is saved as pickle file.

3. Model Training :

- In this phase base model is tested . The best model found was catboost regressor.
- After this hyperparameter tuning is performed on catboost and knn model.
- A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
- This model is saved as pickle file.

4. Prediction Pipeline :

- This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :

- Flask app is created with User Interface to predict the gemstone prices inside a Web Application.

#### Exploratory Data Analysis Notebook

Link : EDA Notebook

#### Model Training Approach Notebook

Link : Model Training Notebook

#### Model Interpretation with LIME

Link : LIME Interpretation