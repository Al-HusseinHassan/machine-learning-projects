# Student Performance Analysis

## Problem

### Description

Student academic performance is influenced by several factors, including study habits, attendance, parental support, extracurricular activities, and educational background. Understanding these factors helps identify patterns that contribute to academic success and recognize students who may need additional support.

The objective is to analyze student academic performance and investigate the relationships between students' personal characteristics, study habits, family support, and academic outcomes.

### Solution

Perform Exploratory Data Analysis (EDA) using the Student Performance dataset to investigate the factors associated with students' academic achievement.

The solution involves:

- Data cleaning and preprocessing.
- Exploratory data analysis and statistical analysis.
- Analyzing GPA and grade distributions.
- Investigating the relationship between study time and academic performance.
- Exploring the impact of absences on student grades.
- Analyzing the influence of parental education and support.
- Comparing academic performance across gender and ethnicity.
- Investigating the relationship between extracurricular activities and GPA.
- Identifying the factors most associated with academic performance.
- Visualizing distributions, correlations, and relationships using charts and graphs.

The goal is to extract meaningful insights into student academic performance and understand the factors associated with better educational outcomes.

## Insights

### Features

The dataset contains 15 features describing students' demographic information, educational background, and academic performance:

- **Student Information:** `StudentID`, `Age`, `Gender`, `Ethnicity`.
- **Family Background:** `ParentalEducation`, `ParentalSupport`.
- **Study Habits:** `StudyTimeWeekly`, `Absences`, `Tutoring`.
- **Extracurricular Activities:** `Extracurricular`, `Sports`, `Music`, `Volunteering`.
- **Academic Performance:** `GPA`.

### Target

`GradeClass` — Multi-class classification representing students' academic performance:

- `0` — A (GPA ≥ 3.5)
- `1` — B (3.0 ≤ GPA < 3.5)
- `2` — C (2.5 ≤ GPA < 3.0)
- `3` — D (2.0 ≤ GPA < 2.5)
- `4` — F (GPA < 2.0)
