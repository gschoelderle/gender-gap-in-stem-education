# Gender Gap in STEM & Education 📊

This data analysis project explores disparities in tertiary education access and representation in STEM (Science, technology, engineering, and mathematics) fields across different countries. Special attention is given to how participation varies by gender.

## 🔍 Overview

Using publicly available datasets (UNESCO, OECD, World Bank), this project analyzes:

- 📐 Representation in STEM education by gender
- 🎓 Tertiary education enrollment across countries
- 💸 Government spending on education (% of GDP)
- 📊 Global averages and country-level insights

The data was processed with **Python** and visualized using **Tableau Public**. Code and logic were developed using **VS Code**.


## 🛠️ Tools & Technologies

- **Python** – data wrangling (pandas)
- **VS Code** – development environment
- **Tableau Public** – interactive visualization

## 🧪 Code Snippet

This Python script calculates the gender gap in STEM and tertiary enrollment, and extracts insights on education spending:

```python
import pandas as pd

df = pd.read_csv("education_gender_data.csv")
df['stem_gender_gap'] = df['% Men in STEM'] - df['% Women in STEM']
df['tertiary_gender_gap'] = df['Tertiary Enrollment (Male)'] - df['Tertiary Enrollment (Female)']
df.to_csv("output_tertiary_gap.csv", index=False)

Full code available in education_gender_data.py

```

## 📁 Dataset Files

These CSV files were generated and used during the data processing phase with Python:

- `education_gender_data.csv`: Raw dataset including gender participation in STEM fields and education spending per country.
- `output_stem_gap.csv`: Processed data showing the difference in STEM participation between men and women.
- `output_tertiary_gap.csv`: Tertiary enrollment rates by gender with calculated gender advantage per country.
- `output_edu_spending.csv`: National public expenditure on education as a percentage of GDP.
- `output_tertiary_advantage_count.csv`: Summary count of countries where tertiary enrollment is higher for a given gender.

These files were analyzed and transformed with pandas and then visualized using Tableau Public.


## 📊 Interactive Dashboard

> **View preview**  
![Dashboard preview](img/dashboard-screenshot.png)
> 
> **View live on Tableau**  
> [🌐 Gender Gap in STEM & Education – Tableau Public](https://public.tableau.com/views/GenderGapinSTEMEducation/viz?:language=es-ES&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)

## 🧾 Credits

- Background map design: Pradeep Kumar G ([Twitter](https://x.com/pradeep_zen))
- Icons: [Flaticon by Freepik](https://www.flaticon.com/) 
- Flags: [Circle Flags](https://hatscripts.github.io/circle-flags/gallery)

## 🧠 Key Insight

> “In 68% of countries analyzed, female enrollment in tertiary education exceeds male enrollment — yet STEM fields still show major gender imbalance.”

## 📬 Contact

- GitHub: [@gschoelderle](https://github.com/gschoelderle)
- Email: [greta.schoelderle@gmail.com]

---

© 2025 Greta Schölderle. Licensed under MIT.
