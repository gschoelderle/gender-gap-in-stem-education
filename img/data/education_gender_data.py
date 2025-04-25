import pandas as pd

archivo = "/Users/greta/Desktop/PORTFOLIO/education_gender_data.csv" 
df = pd.read_csv(archivo)

print(df.head())

df['stem_gender_gap'] = df['% Men in STEM'] - df['% Women in STEM']
top_gap = df[['Country', 'stem_gender_gap']].sort_values(by='stem_gender_gap', ascending=False)

tertiary_enrollment = df[['Country', 'Tertiary Enrollment (Male)', 'Tertiary Enrollment (Female)']].copy()
tertiary_enrollment['gap'] = tertiary_enrollment['Tertiary Enrollment (Male)'] - tertiary_enrollment['Tertiary Enrollment (Female)']

top_spending = df[['Country', 'Education Spending (% of GDP)']].sort_values(by='Education Spending (% of GDP)', ascending=False)

print("\n🔍 Gender gap in STEM (Top 5):\n", top_gap.head())
print("\n🎓 Tertiary education gap:\n", tertiary_enrollment.sort_values(by='gap', ascending=False).head())
print("\n💸 Top 5 in education spending (% GDP):\n", top_spending.head())

top_gap.to_csv("output_stem_gap.csv", index=False)
tertiary_enrollment.to_csv("output_tertiary_gap.csv", index=False)
top_spending.to_csv("output_edu_spending.csv", index=False)            
