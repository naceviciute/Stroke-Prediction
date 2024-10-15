# Stroke Prediction

### Introduction

Stroke is the second leading cause of death worldwide, according to the World Health Organization (WHO), accounting for about 11% of global deaths. 

This project uses a dataset to predict the likelihood of a patient experiencing a stroke based on factors like age, gender, health conditions, and lifestyle choices such as smoking.

### Goal

The objective of this project is to create a model that identifies individuals with high risk of getting a stroke.

### Objectives

To achieve this goal, the following objectives have been established:

- Download, load and clean the dataset.
- Conduct exploratory data analysis and visualize data to identify underlying patterns.
- Perform statistical inference to validate findings.
- Apply linear machine learning models to predict the likelihood of stroke occurrence.
- Summarize results and provide actionable recommendations based on the analysis.

## Exploratory Data Analysis

In this section, the dataset is explored by performing the following:

- Uploading and providing an overview of the dataset
- Generating charts and summaries to visualize key insights
- Analyzing statistics to identify correlations between features and the target variable

## Statistical Inference

This section focuses on statistical inference to evaluate:

- Whether there is a difference in the distribution of age between individuals who have had a stroke and those who have not
- The significance of the correlation between categorical independent variables and the dependent variable

## Statistical Modeling

In this section, statistical modeling is performed by:

- Utilizing a dummy classifier as a benchmark
- Training and evaluating several classifiers, including Logistic Regression, Random Forest, XGBoost, and SVM
- Conducting hyperparameter tuning using Random Search, prioritizing models that minimize false negatives (high recall)
- Adjusting thresholds to minimize false negatives

## Conclusions

- The dataset contains information on over 5000 individuals, revealing a class imbalance where the majority did not experience a stroke.
- Significant correlations were found between stroke occurrence and variables such as age, hypertension, heart disease, and marital status.
- Hypothesis testing showed strong evidence for age differences and associations between variables like hypertension, work type, and stroke risk.
- Logistic Regression and Random Forest were identified as the top models, balancing performance and interpretability, with key predictors like age, hypertension, and smoking status.
- Adjusting classification thresholds for both models improved recall for stroke cases, with Logistic Regression achieving 80% recall and Random Forest improving to 60% recall for positive cases.
- The final model, Logistic Regression, reached 80% recall for stroke cases, but precision remains an area for improvement (15%).

## Model Deployment

The final model was deployed, and a user-friendly interface was built using Streamlit to allow healthcare professionals and users to input patient data and receive real-time predictions.

This app can be accessed via the following link: [Stroke Prediction App] (https://stroke-b5jk6u8tb2cpljafikfwbd.streamlit.app/)


## License

This project is licensed under the [MIT License](LICENSE).

