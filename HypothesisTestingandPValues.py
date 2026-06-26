import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
#Sample_Data
data=[12,14,15,16,17,18,19]

#Null Hypothesis: mean =15
population_mean = 15


# Perform t-test
t_stat, p_value = ttest_1samp(data, population_mean)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)
# Interpret Results
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Fail to Reject the null hypothese: no significant difference")
    # Data from two groups
group1 = [12, 14, 15, 16, 17, 18, 19]
group2 = [11, 13, 14, 15, 16, 17, 18]
# Perform t-test
tt_stat, pp_value = ttest_ind(group1, group2)
print("T-Statistic: ", tt_stat)
print("P-Value: ", pp_value)
# Interpretation 
# alpha = 0.05
alpha_1 = 0.05
if p_value <= alpha_1:
    print("Reject the null hypothesis: significant difference")
else:
    print("Fail to Reject the null hypothesis: no significant difference")