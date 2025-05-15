# Loan Approval Prediction App

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

---

## Project Overview

This project aims to build a machine learning model to predict loan approvals using applicant data such as income, credit history, loan amount, and more.

I experimented with several algorithms including Gradient Boosting, Random Forest, Decision Trees, SVM, and Naive Bayes to find the best balance between accuracy and interpretability.

---

## Why Naive Bayes?

The **Naive Bayes** classifier was chosen as the final model because:

- It achieved consistent accuracy of about **93.5%** on training, testing, and cross-validation datasets.  
- It demonstrated minimal overfitting, ensuring good generalization to unseen data.  
- Its simplicity leads to fast training and prediction times and easier interpretability — crucial for real-world applications.

---

## Performance Summary

| Metric                   | Score           |
|--------------------------|-----------------|
| Training Accuracy        | 93.5%           |
| Testing Accuracy         | 93.3%           |
| Cross-Validation Accuracy| 93.5% ± 0.57%   |

---

## Installation

1. Clone the repository:  
   ```
   git clone https://github.com/niskriti1/loan-approval-prediction.git
   cd loan-approval-prediction
   ```
2. (Optional) Create and activate a virtual environment:
    ```
    python3 -m venv venv
    source venv/bin/activate    # Linux/macOS
    venv\Scripts\activate       # Windows
    ```
3. Install dependencies:
   ```
   pip install requirements.txt
   ```
  ## Usage
Prepare your dataset according to the format shown in the notebook or data folder.

Run the notebook  to train and evaluate the Naive Bayes model:
Use the trained model to predict loan approvals on new data.

## What I Learned
How to compare multiple machine learning models effectively.
The importance of cross-validation for robust performance evaluation.
Balancing model complexity with real-world usability and interpretability.

## Contributions and Feedback
Feel free to open issues, submit pull requests, or share suggestions — I’m excited to improve this project!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
