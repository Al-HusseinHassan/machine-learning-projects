# CICIDS2017 Network Intrusion Detection

## Problem

### Description

Network intrusion occurs when malicious activities attempt to compromise, disrupt, or gain unauthorized access to a computer network. Detecting these activities helps organizations identify security threats, protect network resources, and respond to potential attacks.

The objective is to detect whether network traffic is benign or malicious and classify detected attacks into their corresponding categories and specific attack types using network flow features.

### Solution

Develop Machine Learning classification models to detect and classify network intrusions using the CICIDS2017 dataset.

The solution involves:

- Data preprocessing and exploratory data analysis.
- Feature engineering, correlation analysis, and feature selection.
- Training and evaluating five XGBoost classification models.
- Performing binary detection, multi-class attack classification, and sub-attack classification.
- Addressing class imbalance using balanced sample weights.
- Evaluating model performance using classification metrics.

The project includes five modeling tasks:

1. **Binary Detection:** Benign vs. Attack.
2. **Attack Classification:** Classifying attack traffic into major categories.
3. **Weighted Attack Classification:** Major attack-category classification with balanced sample weights.
4. **Detection & Classification:** Classifying all traffic into benign and major attack categories.
5. **Sub-Attack Classification:** Classifying attack traffic into specific attack variants.

The goal is to build a machine learning-based intrusion detection system capable of identifying malicious network traffic and distinguishing between different attack types.

## Insights

### Features

Network flow features describing traffic characteristics, including:

- Flow duration and inter-arrival times.
- Forward and backward packet counts.
- Forward and backward byte volumes.
- Packet lengths and flow rates.
- Header lengths and packet statistics.
- Active and idle time statistics.
- Destination port information.

### Target

- `binary_cat` — Binary classification: 0 (Benign) / 1 (Attack).
- `major_cat` — Multi-class classification by major category (Benign, DoS, DDoS, Brute Force, Web Attack, Port Scan, Bot, Infiltration, Heartbleed).
- `sub_attack` — Multi-class classification by specific attack variant (e.g., Hulk, GoldenEye, XSS, SQL Injection).

### Model Performance

| Model   | Task                           | Accuracy |
| ------- | ------------------------------ | -------: |
| Model 1 | Binary Detection               |   99.92% |
| Model 2 | Attack Classification          |   99.98% |
| Model 3 | Weighted Attack Classification |   99.98% |
| Model 4 | Detection & Classification     |   99.89% |
| Model 5 | Sub-Attack Classification      |   99.77% |

**Note:** Although the models achieve high accuracy, performance can vary across individual classes, particularly rare attacks such as Heartbleed and Infiltration. Therefore, precision, recall, and F1-score should also be considered when evaluating the models.
