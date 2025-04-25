import pandas as pd

# Cargar archivo CSV
archivo = "/Users/greta/Desktop/PORTFOLIO/education_gender_data.csv" 
df = pd.read_csv(archivo)

# Mostrar las primeras filas del dataset
print(df.head())

# 1. Brecha de género en STEM por país
df['stem_gender_gap'] = df['% Men in STEM'] - df['% Women in STEM']
top_gap = df[['Country', 'stem_gender_gap']].sort_values(by='stem_gender_gap', ascending=False)

# 2. Escolaridad terciaria por género
tertiary_enrollment = df[['Country', 'Tertiary Enrollment (Male)', 'Tertiary Enrollment (Female)']].copy()
tertiary_enrollment['gap'] = tertiary_enrollment['Tertiary Enrollment (Male)'] - tertiary_enrollment['Tertiary Enrollment (Female)']

# 3. Países que más invierten en educación
top_spending = df[['Country', 'Education Spending (% of GDP)']].sort_values(by='Education Spending (% of GDP)', ascending=False)

# Resultados en consola
print("\n🔍 Gender gap in STEM (Top 5):\n", top_gap.head())
print("\n🎓 Tertiary education gap:\n", tertiary_enrollment.sort_values(by='gap', ascending=False).head())
print("\n💸 Top 5 in education spending (% GDP):\n", top_spending.head())

# Guardar resultados como CSV
top_gap.to_csv("output_stem_gap.csv", index=False)
tertiary_enrollment.to_csv("output_tertiary_gap.csv", index=False)
top_spending.to_csv("output_edu_spending.csv", index=False)            