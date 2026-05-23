# Healthcare System Confusion Matrix

## Overview

A machine learning model was developed for a healthcare system to classify patients into two categories:

- Healthy
- Sick

The dataset contained 100 patient records collected from routine health screenings.

### Dataset Split

- Training Records: 70
- Testing Records: 30

After training, the model was evaluated using 30 unseen patient records.

---

## Testing Results

During testing, the model made 3 incorrect predictions:

- 2 sick patients were predicted as healthy (False Negative)
- 1 healthy patient was predicted as sick (False Positive)

Total incorrect predictions = 3

Total correct predictions = 27

---

# Confusion Matrix

| Actual / Predicted | Healthy | Sick |
|--------------------|----------|------|
| Healthy            | 14       | 1    |
| Sick               | 2        | 13   |

---

## Confusion Matrix Explanation

### True Negative (TN) = 14
Healthy patients correctly classified as healthy.

### False Positive (FP) = 1
Healthy patient incorrectly classified as sick.

### False Negative (FN) = 2
Sick patients incorrectly classified as healthy.

### True Positive (TP) = 13
Sick patients correctly classified as sick.

---

# Matrix Figure

```text
                     Predicted
                 Healthy    Sick

Actual Healthy      14        1
Actual Sick         2        13
