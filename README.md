

# Marketing Experimentation & Uplift Modeling

A data science project that analyzes the effectiveness of marketing email campaigns using **A/B testing and uplift modeling** to identify customers most likely to respond to promotional emails.

---

## Project Overview

Marketing teams often send promotional emails to a large number of customers. However:

* Some customers would purchase **even without the email**
* Some customers **never purchase**
* Only a subset of customers are **influenced by the email campaign**

Sending emails to everyone increases **marketing costs and customer fatigue**.

This project uses **experimentation and uplift modeling** to determine:

> Which customers should receive marketing emails to maximize conversions.

---

## Dataset

This project uses the
Kevin Hillstrom Email Marketing Dataset.

The dataset contains:

* Customer purchase history
* Marketing email campaign segments
* Website visits
* Conversion outcomes

Important columns include:

| Column       | Description                   |
| ------------ | ----------------------------- |
| recency      | Months since last purchase    |
| history      | Customer spending history     |
| mens         | Purchased men's products      |
| womens       | Purchased women's products    |
| zip_code     | Customer region               |
| new_customer | New or returning customer     |
| channel      | Marketing acquisition channel |
| segment      | Email campaign group          |
| conversion   | Whether customer purchased    |

---

## Project Objectives

1. Analyze marketing experiment results using **A/B testing**
2. Measure statistical significance of email campaigns
3. Build an **uplift model** to predict customer responsiveness
4. Identify high-impact customers for targeted marketing

---

## Methodology

The project follows a typical **data science experimentation pipeline**.

### 1. Exploratory Data Analysis

* Data inspection and cleaning
* Customer behavior analysis
* Conversion rate visualization

### 2. A/B Testing

Statistical testing was performed to evaluate whether sending marketing emails increased conversions.

Techniques used:

* Hypothesis testing
* T-test
* Conversion rate comparison

### 3. Uplift Modeling

An uplift model was built using the **Two-Model approach**:

```
Uplift = P(conversion | treatment) − P(conversion | control)
```

Where:

* Treatment = customer received marketing email
* Control = customer did not receive email

The model identifies customers whose purchasing behavior is **positively influenced by marketing emails**.

---

## Model

The uplift model uses:

* **Random Forest classifiers**
* Two-model uplift approach
* Separate models for treatment and control groups

Library used: **scikit-uplift**

---

## Model Evaluation

Model performance was evaluated using:

* **Uplift Curve**
* **Qini Curve**
* **Uplift AUC Score**

These metrics measure the model's ability to identify customers most likely to respond to marketing campaigns.

---

## Results

The uplift model successfully identifies customers most likely to respond to promotional emails.

Key insight:

Targeting only **high-uplift customers** can significantly improve marketing campaign effectiveness while reducing unnecessary marketing costs.

---

## Tech Stack

Python libraries used:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* scipy
* statsmodels
* scikit-uplift

---

## Project Structure

```
uplift-modeling-marketing-experiment
│
├── data
│   └── hillstrom.csv
│
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_AB_Testing.ipynb
│   └── 03_Uplift_Model.ipynb
│
├── src
│   └── uplift_pipeline.py
│
├── requirements.txt
│
└── README.md
```

---

## How to Run the Project

Clone the repository:

```
git clone https://github.com/yourusername/uplift-modeling-marketing-experiment.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the notebooks:

```
jupyter notebook
```

---

## Future Improvements

Possible extensions to this project:

* Add **feature importance analysis**
* Build a **Streamlit dashboard** for interactive targeting
* Deploy the model as a **marketing recommendation system**

---

## Author

Divya Tiwari
B.Tech CSE Student

