# NSL-KDD Network Intrusion Detection

## Problem

### Description

Network intrusion occurs when malicious activities attempt to compromise, disrupt, or gain unauthorized access to a computer network. Detecting these activities helps organizations identify security threats, protect network resources, and respond to potential attacks.

The objective is to detect whether network connections are normal or malicious and classify attack traffic into major categories and specific attack types using connection-level features.

### Solution

Develop Machine Learning classification models to detect and classify network intrusions using the NSL-KDD dataset.

The solution involves:

- Data preprocessing and exploratory data analysis.
- Feature analysis, correlation analysis, and feature selection.
- Encoding categorical features and scaling numerical features.
- Training and evaluating three XGBoost classification models.
- Performing binary detection, major-category classification, and fine-grained attack classification.
- Addressing class imbalance using balanced sample weights.
- Evaluating model performance using classification metrics.

The project includes three modeling tasks:

1. **Binary Detection:** Normal vs. Attack.
2. **Major-Category Classification:** Classifying attack traffic into DoS, Probe, R2L, and U2R.
3. **Fine-Grained Classification:** Classifying attack traffic by specific attack names.

The goal is to build a machine learning-based intrusion detection system capable of identifying malicious network connections and distinguishing between different attack categories and types.

## Insights

### Features

The dataset contains 41 connection-level features describing network activity, including:

- **Basic Connection Features:** Duration, protocol type, service, flag, and source/destination bytes.
- **Error and Unusual Packet Features:** Wrong fragments, urgent packets, failed logins, and suspicious activity indicators.
- **Content Features:** Login status, compromised conditions, root shell access, and file creation counts.
- **Traffic Features:** Connection counts, service counts, error rates, and destination-host traffic statistics.

### Target

- `label`
