import pandas as pd
from scipy.stats import zscore

df = pd.DataFrame({
    'Yards_Per_Game': [366.5, 467.6],
    'Points_Per_Game': [24.9, 34.1],
    'Plays_Per_Game': [64.8, 76.9]
})

# Missing values
missing = df.isnull().sum()
with open('../appendices/Tables/Sanity_Checks.txt','w') as f:
    f.write('Missing Values:\n')
    f.write(str(missing) + '\n')

# Outliers using Z-score
z_scores = abs(zscore(df))
with open('../appendices/Tables/Sanity_Checks.txt','a') as f:
    f.write('Z-Scores:\n')
    f.write(str(z_scores))