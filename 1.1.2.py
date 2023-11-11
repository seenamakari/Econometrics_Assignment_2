from scipy.stats import chi2

#Here is the code for finding the chi-square value with 406 observations and a 5% significance level

degrees_of_freedom = 405  # (n - 1) for n = 406 observations

# Calculate the critical chi-square value
critical_value = chi2.ppf(0.95, degrees_of_freedom)
print(critical_value)