import pandas as pd

df = pd.DataFrame({
    'Game_Type': ['Home', 'Away'],
    'Points_Per_Game':[26, 32]
})

avg_home = df[df['Game_Type']=='Home']['Points_Per_Game'].mean()
avg_away = df[df['Game_Type']=='Away']['Points_Per_Game'].mean()

with open('../appendices/Tables/Bias_Fairness.txt','w') as f:
    f.write(f'Average Points Home: {avg_home}\n')
    f.write(f'Average Points Away: {avg_away}\n')