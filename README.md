# Student Performance Analytics

## Project Overview
This project explores factors affecting student academic success using Exploratory Data Analysis (EDA), progression modeling, and statistical validation. The goal is to identify patterns in score gaps and move from simple grade averages to "Momentum Modeling" to predict how students progress over time.

## Dataset
The analysis is based on the UCI Student Performance dataset, including:
- **Demographics:** Age, gender, family size.
- **Social Factors:** Study time, free time, alcohol consumption, and health.
- **Academic Grades:** G1 (Period 1), G2 (Period 2), and G3 (Final Grade).

## Project Chapters
### 1. Score Gap Analysis
Comparing performance across different subjects (Math vs. Portuguese) to identify foundational strengths and weaknesses.

### 2. Progression Modeling & Statistical Validation
Developing a "Momentum" model to classify students based on their trajectory:
- **Overachievers:** Students who beat their arithmetic progression.
- **On Track:** Students performing exactly as predicted.
- **Underachievers:** Students whose final performance "crashed" relative to their start.

## Key Statistical Insights
- **The Zero-Cliff:** Identified a non-normal distribution in final grades where a specific segment of the class experiences total performance collapse (G3=0).
- **The Chaos Factor:** Mathematically proved that the "Critical" performance group is 4x more unpredictable (Variance: 7.64) than passing groups.
- **The Absence Paradox:** Discovered a "Small" effect size (Cohen’s d = 0.33) showing that Overachievers often have higher absences, suggesting strategic self-study habits.
- **Clean Slate:** Confirmed that past failures have a negligible impact (Cohen’s d = 0.06) on a student's ability to "overachieve" in the current semester.

## How to Run
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/jahandima/student-performance-analytics.git](https://github.com/jahandima/student-performance-analytics.git)