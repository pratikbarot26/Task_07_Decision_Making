import numpy as np
from scipy import stats

yards = np.array([366.5, 467.6])
points = np.array([24.9, 34.1])

def conf_interval(data):
    mean = np.mean(data)
    sem = stats.sem(data)
    return stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)

with open('../appendices/Tables/Uncertainty.txt', 'w') as f:
    f.write(f'Yards per game CI: {conf_interval(yards)}\n')
    f.write(f'Points per game CI: {conf_interval(points)}\n')