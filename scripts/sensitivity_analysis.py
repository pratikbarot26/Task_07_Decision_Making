import numpy as np

yards = np.array([366.5, 467.6])
perturbed = yards * 1.05  # +5% perturbation
with open('../appendices/Tables/Sensitivity.txt','w') as f:
    f.write(f'Original Yards: {yards}\n')
    f.write(f'Perturbed (+5%): {perturbed}\n')