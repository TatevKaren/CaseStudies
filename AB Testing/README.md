# A/B Testing Case Study Using Python

This Python script is designed to conduct a simulated A/B test, a commonly used method in statistics and data science for comparing two versions of a single variable. The objective is to determine which version performs better. This script serves as a practical case study to showcase A/B testing.

![Control](https://github.com/TatevKaren/CaseStudies/assets/76843403/08318891-36ab-49da-acc5-6eca9a5780c0)

Google Collab Link with Python Code - <a href = "https://colab.research.google.com/drive/1XP7_NS0tGq2UvQj4W9HyRMwN20Ynn0Yt?usp=sharing"> Click here </a>


## 1. Simulating Click Data for A/B Testing

### Objective
To simulate click data for an experimental group (`exp`) and a control group (`con`).

### Method (generating data similar to what we use in our case study)
- Utilizes `numpy` and `pandas` libraries to generate random binary click data (`1` = click, `0` = no click).
- Creates two datasets: `df_exp` for the experimental group and `df_con` for the control group.
- Each group has `1000` samples with different click probabilities (`0.5` for `exp` and `0.2` for `con`).
- Merges the data into a single DataFrame `df_ab_test` for analysis.
![Unknown](https://github.com/TatevKaren/CaseStudies/assets/76843403/7b754602-d3a7-42ad-961c-9e9b276aa9ed)

## 2. Statistical Significance in A/B Testing

### Objective
To determine if the difference in click rates between the experimental and control groups is statistically significant.

### Method
- Calculates total number of clicks (`X_con`, `X_exp`) and click probabilities (`p_con_hat`, `p_exp_hat`) for each group.
- Computes a pooled click probability (`p_pooled_hat`) and pooled variance.
- Calculates standard error (`SE`) to measure the precision of click probability estimates.
- Performs a two-sample Z-test (calculates test statistic (`Test_stat`), critical value (`Z_crit`), and p-value).
- Determines a confidence interval (`CI`) to estimate the true difference in click probabilities.

## Application as a Case Study

### Scenario
A website is testing two different webpage designs to see which one results in higher user engagement, measured by clicks.

### Process
- The `exp` group is shown the new webpage design, while the `con` group sees the original design.
- The script simulates user interactions and calculates the click-through rate for each group.
- Statistically analyzes the results to assess if the new design significantly improves user engagement.

## Conclusion

### Findings
The script provides statistical evidence on whether the new design (experimental group) leads to a higher click rate compared to the control group.

![ABtesting_figure](https://github.com/TatevKaren/CaseStudies/assets/76843403/a8ada9b2-4fe2-4381-875f-199d7a9a9c22)


### Decision Making
Decisions are made based on the p-value and confidence interval, determining the implementation of the new design across the website.

---

*This case study illustrates the effective use of A/B testing in digital marketing, website optimization, and user experience research for data-driven decision-making.*

