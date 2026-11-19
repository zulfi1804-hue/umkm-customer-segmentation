# UMKM Customer Segmentation

## Project Overview

This project applies unsupervised machine learning to segment customers of a small and medium-sized enterprise (UMKM) in the bakery and coffee business in Bandung, Indonesia.

The objective is to identify customer purchasing behavior, group customers into meaningful segments, and provide targeted marketing strategies for each segment.

The final model uses **K-Means Clustering with 4 clusters** and is integrated into an interactive Streamlit application to predict the segment of new customers.

## Business Problem

The UMKM currently provides similar promotional offers to all customers, even though customers have different purchasing behaviors and preferences.

This project addresses the problem by:
- Identifying distinct customer segments based on purchasing behavior.
- Understanding the characteristics of each segment.
- Providing suitable marketing recommendations for each segment.
- Developing an application that can assign new customers to the identified segments.

## Dataset

The dataset contains 10,000 unique customer records with registration information and transaction summaries from the previous six months.

The dataset includes information such as:
- Customer age and registration date.
- Main purchasing channel.
- Payment method and favorite product category.
- Number of transactions in the last six months.
- Total customer spending.
- Days since the last transaction.
- Percentage of transactions using promotions.
- Average customer rating.

Customer identifiers and registration dates are used for data management and feature engineering. The final clustering model uses six numerical features.

## Machine Learning Approach

This project uses **Unsupervised Learning**, specifically clustering, because the dataset does not contain predefined customer segment labels.

### K-Means Clustering

K-Means was selected as the main clustering algorithm and used in four feature-selection experiments.

The final model uses six numerical features:
1. `jumlah_transaksi_6bln`
2. `total_belanja_rp`
3. `hari_sejak_transaksi_terakhir`
4. `persen_pakai_promo`
5. `rating_rata`
6. `lama_bergabung_hari`

The final model was selected based on internal clustering evaluation metrics and the interpretability of its customer segments.

### Model Evaluation

The final model uses **K = 4** and achieved the following results:

| Evaluation Metric | Result |
|---|---:|
| Silhouette Score | 0.3696 |
| Davies-Bouldin Index | 1.1289 |
| Calinski-Harabasz Index | 5660.67 |
| Number of Clusters | 4 |

The results indicate that the selected model provides a reasonable separation of customer groups and produces interpretable segments for business use.

## Customer Segmentation Results

The final K-Means model identifies four customer segments:

### Cluster 1 — Active and Promotion-Responsive Customers

- Number of customers: 2,497 (24.97%)
- Average transactions: 10.93
- Average spending: Rp348,541
- Average days since last transaction: 12.20
- Promotion usage: 81.54%

**Business Recommendation:**

Provide next-purchase vouchers, bread and coffee bundle promotions, and loyalty stamp programs.

### Cluster 2 — Inactive / At-Risk Customers

- Number of customers: 2,966 (29.66%)
- Average transactions: 2.56
- Average spending: Rp107,158
- Average days since last transaction: 109.61
- Promotion usage: 34.64%

**Business Recommendation:**

Run win-back campaigns, offer customers their favorite products, and conduct customer satisfaction surveys.

### Cluster 3 — High-Value Loyal Customers

- Number of customers: 3,023 (30.23%)
- Average transactions: 27.88
- Average spending: Rp1,353,954
- Average days since last transaction: 5.15
- Promotion usage: 19.66%

**Business Recommendation:**

Provide VIP rewards, early access to new menu items, and customer appreciation programs without relying heavily on discounts.

### Cluster 4 — Occasional High-Spending Customers

- Number of customers: 1,514 (15.14%)
- Average transactions: 4.10
- Average spending: Rp1,093,769
- Average days since last transaction: 30.66
- Promotion usage: 12.56%

**Business Recommendation:**

Offer premium packages, birthday cakes, snack packs, and pre-order reminders.

## Project Workflow

1. Exploratory Data Analysis (EDA)
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. K-Means Clustering Experiments
6. Model Evaluation and Selection
7. Customer Profiling
8. Business Recommendation Development
9. Model Saving and Testing
10. Streamlit Application Development and Deployment

## Streamlit Application

The final model is integrated into an interactive application that allows users to enter customer information and receive a predicted customer segment with a corresponding business recommendation.

**Application Link:**

[UMKM Customer Segmentation — Streamlit App](https://umkm-customer-segmentation.streamlit.app/)

## Repository Structure

```text
umkm-customer-segmentation/
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── model_final.joblib
├── notebooks/
│   └── 01_data_understanding.ipynb
├── reports/
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/zulfi1804-hue/umkm-customer-segmentation.git
cd umkm-customer-segmentation
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
python -m streamlit run app/app.py
```

The application will open in your browser.

## Team Members

- Member 1 — [Atsnaina Habibah]
- Member 2 — [Kholistyani Zulfi]

