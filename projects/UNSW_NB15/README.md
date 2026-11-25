# UNSW-NB15 Network Intrusion Detection

## Problem

### Description

Network intrusion occurs when malicious activities attempt to compromise, disrupt, or gain unauthorized access to a computer network. Detecting these activities helps organizations identify security threats, protect network resources, and respond to potential attacks.

The objective is to detect whether network traffic is normal or malicious and classify attack traffic into different attack families using network flow features.

### Solution

Develop Machine Learning classification models to detect and classify network intrusions using the UNSW-NB15 dataset.

The solution involves:

- Data preprocessing and exploratory data analysis.
- Feature engineering, including binning numerical features into categorical groups.
- Correlation analysis and feature selection.
- Encoding categorical features and scaling numerical features.
- Training and evaluating three XGBoost classification models.
- Addressing class imbalance using balanced sample weights.
- Evaluating model performance using classification metrics and confusion matrices.

The project includes three modeling stages:

1. **Binary Detection:** Normal vs. Attack.
2. **Attack-Family Classification:** Classifying attack traffic into six major families.
3. **DoS-Family Classification:** Separating Analysis, Backdoor, DoS, and Exploits using a dedicated sub-model.

The goal is to build a machine learning-based intrusion detection system capable of detecting malicious network traffic and classifying attack families, while investigating the challenges of distinguishing between highly similar attack types.

## Insights

### Features

The dataset contains 49 flow-level features describing network activity, including:

- **Basic Connection Features:** Duration, protocol, service, and connection state.
- **Packet and Byte Features:** Source/destination packets, bytes, and traffic rate.
- **TTL and Load Features:** Source/destination TTL, window sizes, and network load.
- **Timing Features:** Packet intervals, jitter, TCP round-trip time, SYN-ACK, and ACK-DAT.
- **Connection Statistics:** Connection counts and service/host-based traffic statistics.
- **Binary Flags:** FTP login status and source/destination IP-port indicators.

### Target

- `label` — Binary classification: 0 (Normal) / 1 (Attack).
- `attack_group` — Multi-class classification by six attack families:
    - `DoS_family` — Analysis, Backdoor, DoS, Exploits.
    - `Fuzzers`
    - `Generic`
    - `Reconnaissance`
    - `Shellcode`
    - `Worms`
- `attack_cat` — Fine-grained classification into the original attack categories, used by the dedicated DoS-family sub-model to distinguish Analysis, Backdoor, DoS, and Exploits.

### Model Performance

| Model                | Task                         | Accuracy |
| -------------------- | ---------------------------- | -------: |
| Detection            | Binary Detection             |   93.88% |
| Classification       | Attack-Family Classification |   92.69% |
| DoS-Family Sub-Model | Fine-Grained Classification  |   56.60% |

**Note:** The detection and attack-family classification models achieve accuracy in the low-to-mid 90% range. However, distinguishing between Analysis, Backdoor, DoS, and Exploits is considerably more challenging, with the dedicated sub-model achieving 56.6% accuracy. Rare and overlapping attack categories have particularly low precision and recall, highlighting the difficulty of fine-grained attack classification in this dataset.
