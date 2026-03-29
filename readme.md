# Diabetes Risk Prediction Using LightGBM

**Live Application:**

https://your-streamlit-app-link-here

Use the link above to interact with the application and predict whether an individual has Prediabetes/Diabetes or No Diabetes in real time.

## Project Overview

Diabetes is one of the most prevalent chronic diseases worldwide, impacting millions and leading to serious health complications, including heart disease, vision loss, kidney failure, and lower-limb amputation. Early detection is critical, as lifestyle changes and timely medical interventions can mitigate risks.

<details> <summary><strong>View Project Details</strong></summary>

This project develops a predictive machine learning model that uses key health and lifestyle indicators to classify an individual’s risk of diabetes.

**The system predicts whether an individual is:**

- No Diabetes (healthy)
- Prediabetes / Diabetes (at risk or diagnosed)

By analyzing features such as BMI, age, general health, alcohol consumption, cholesterol levels, and physical/mental health, the application provides an interactive, real-time risk assessment.

**The project demonstrates a full end-to-end machine learning workflow:**

data preprocessing → feature selection → model training → model evaluation → deployment via Streamlit

## Features
- Predicts diabetes risk in real time
- Uses key health and lifestyle indicators for accurate prediction
- Handles both categorical (Yes/No, Sex) and numerical features (BMI, physical/mental health)
- Provides probability scores and interpretable risk levels
Interactive and user-friendly Streamlit interface
- Highlights model prediction and risk level with clear visual cues

## Machine Learning Model

**Model Used:** LightGBM Classifier (selected for highest cross-validation accuracy)

**Objective:** Predict diabetes risk using 21 key health and lifestyle features

0 → No Diabetes

1 → Prediabetes / Diabetes

**Evaluation Metrics:**

The model was thoroughly evaluated using cross-validation to ensure reliable performance, and its predictions were assessed for accuracy and consistency using standard classification metrics, carefully measuring how well it identifies diabetes risk while balancing false positives and false negatives.

## Why LightGBM Was Selected

- High performance on structured tabular datasets
- Captures complex, non-linear relationships among health features
- Reduces overfitting using gradient boosting
- Robust to imbalanced or noisy data
- Provides feature importance insights for health interpretation

## Business Goals
- Identify individuals at risk of prediabetes/diabetes
- Support healthcare providers in early intervention and lifestyle guidance
- Enable data-driven decisions for public health and personal health management
- Reduce long-term diabetes-related health complications

## Objectives
- Build a robust machine learning model to predict diabetes risk
- Identify the most important features affecting diabetes risk
- Minimize false positives/negatives to ensure actionable predictions
- Provide an interactive and easy-to-use web interface for real-time assessment

## Deployment

The model is deployed using Streamlit, enabling users to enter personal health and lifestyle information, receive immediate risk predictions, view the probability distribution for No Diabetes and Prediabetes/Diabetes, and understand their risk level through clear, color-coded visual cues, with strict feature alignment between training and deployment to ensure consistent and reliable predictions.

**Data Source:** [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
</details>