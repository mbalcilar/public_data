# Analysis of Economics Data (2022) — CSV Dataset Repository

This repository provides CSV versions of datasets accompanying:

> Cameron, A. Colin.  
> *Analysis of Economics Data: An Introduction to Econometrics*. 2022.

The original book website is available at:

📘 https://cameron.econ.ucdavis.edu/aed/

The original datasets distributed by the author are provided in **STATA (.dta)** format.  
This repository converts those datasets into **CSV format** for easier use in:

- Python
- pandas
- statsmodels
- Jupyter Notebook
- Excel
- R
- MATLAB
- Julia
- Other statistical software

---

# Source of the Data

Original datasets and textbook materials are available from:

A. Colin Cameron  
*Analysis of Economics Data: An Introduction to Econometrics* (2022)

Official website:

https://cameron.econ.ucdavis.edu/aed/

All credit for the original datasets belongs to the author and publisher.

---

# Purpose of This Repository

The goal of this repository is to make the datasets easier to use in modern data science and econometrics workflows, especially in:

- Python-based econometrics courses
- Jupyter Notebook environments
- pandas/statmodels workflows
- Machine learning and data analysis tutorials
- Cross-platform data analysis environments

CSV files are platform-independent and easier to import into most software.

---

# File Formats

| Format | Description |
|---|---|
| `.csv` | Converted CSV datasets |
| `.dta` | Original STATA datasets (author source format) |

All converted CSV filenames are written in lowercase for consistency and portability across operating systems.

---

# Using the Data in Python

Example using pandas:

```python
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
```

Example using statsmodels:

```python
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("dataset.csv")

model = smf.ols("y ~ x1 + x2", data=df).fit()

print(model.summary())
```

---

# Dataset Conversion

The datasets were converted from STATA `.dta` format to `.csv` using Python and pandas.

Example conversion code:

```python
import pandas as pd

df = pd.read_stata("example.dta")
df.to_csv("example.csv", index=False)
```

---

# Educational Use

These datasets are intended for:

- Econometrics instruction
- Classroom demonstrations
- Homework assignments
- Empirical replication
- Statistical programming tutorials
- Research training

---

# Citation

If you use these datasets, please cite the original textbook:

> Cameron, A. Colin. *Analysis of Economics Data: An Introduction to Econometrics*. 2022.

---

# Disclaimer

This repository is an unofficial educational conversion of publicly distributed companion datasets associated with the textbook.

All intellectual property rights for the original datasets, textbook, and supporting materials remain with the author and publisher.

---

# Maintainer

Prepared for educational and instructional use in econometrics, statistics, and data science courses.

