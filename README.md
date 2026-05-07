# Public Data Repository

This repository contains a collection of publicly available datasets for teaching, learning, and research in:

- Data Science
- Business Analytics
- Econometrics
- Economics
- Machine Learning
- Forecasting
- Statistical Computing
- Data Visualization

GitHub repository:

[public_data repository](https://github.com/mbalcilar/public_data)

---

# Repository Structure

Datasets are organized into subfolders by topic, source, course, textbook, software environment, or application area.

Each subfolder may include:

- Raw datasets
- Cleaned datasets
- CSV files
- STATA files
- Documentation
- Readme files
- Supporting materials
- Code examples
- Course exercises

Please refer to the individual subfolder documentation for detailed information about each dataset collection.

---

# Topics Covered

The repository includes datasets related to:

| Area | Examples |
|---|---|
| Econometrics | Cross-sectional, panel, and time series data |
| Economics | Macroeconomic and microeconomic datasets |
| Business Analytics | Customer analytics, operational data, forecasting |
| Data Science | Classification, regression, clustering datasets |
| Machine Learning | Training and benchmark datasets |
| Finance | Financial markets, stock returns, risk measures |
| Forecasting | Economic and business forecasting data |
| Visualization | Data visualization practice datasets |

---

# File Formats

Common file formats include:

| Format | Description |
|---|---|
| `.csv` | Comma-separated values |
| `.xlsx` | Excel workbooks |
| `.dta` | STATA datasets |
| `.sas7bdat` | SAS datasets |
| `.txt` | Text data files |
| `.json` | JSON data |
| `.parquet` | Columnar storage format |

---

# Using the Data in Python

Example using pandas:

```python
import pandas as pd

df = pd.read_csv("data/example.csv")

print(df.head())
```

Example using plotnine:

```python
from plotnine import *
import pandas as pd

df = pd.read_csv("data/example.csv")

(
    ggplot(df, aes(x="x", y="y"))
    + geom_point()
)
```

Example using statsmodels:

```python
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/example.csv")

model = smf.ols("y ~ x1 + x2", data=df).fit()

print(model.summary())
```

---

# Educational Purpose

This repository is intended for:

- Classroom instruction
- Homework assignments
- Econometrics exercises
- Jupyter Notebook tutorials
- Data visualization practice
- Machine learning demonstrations
- Reproducible research
- Statistical computing training

---

# Data Sources

Datasets originate from a variety of publicly available sources, including:

- Government agencies
- International organizations
- Academic textbooks
- Research projects
- Public repositories
- Open data portals
- Educational materials

Detailed source information is typically provided within the corresponding subfolders.

---

# Disclaimer

This repository primarily redistributes publicly available datasets for educational and research purposes.

Users are responsible for checking original licensing terms, citation requirements, and usage restrictions where applicable.

All intellectual property rights remain with the original data creators and providers.

---

# Maintainer

Maintained by:

Mehmet Balcilar  
Department of Economics and Business Analytics  
University of New Haven

GitHub profile:

[mbalcilar GitHub profile](https://github.com/mbalcilar)