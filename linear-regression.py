import numpy as np
import statsmodels.api as sm
import pandas as pd


x = [0, 1], [5, 1], [15, 2], [25, 5], [689, 11], [45, 15], [55, 34], [60, 35], [82, 1], [5, 1], [15, 2464], [645, 5], [35, 11], [45, 15], [55, 34], [60, 35], [0, 1], [5, 71], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [6440, 35]
y = [4, 5, 20, 14, 232, 22, 38, 43,4, 5, 20, 6414, 32, 22, 38, 6443,4, 5, 2066, 14, 32, 2221, 318, 43]

data = pd.DataFrame(dict(y=y, X=x))

data.head()

x, y = np.array(x), np.array(y)

# Create a design matrix for the independent variable x
X = sm.add_constant(x)

# Fit an OLS model to the data using the design matrix X and response y
model = sm.OLS(y, X)
results = model.fit()

print("Coefficients:")
for name, coef in zip(['Intercept', 'x'], results.params):
    print("%-12s %12.3f" % (name + ":", abs(coef)))

print("\nStandard errors:")
for name, se in zip([None, 'x'], results.bse):
    if name is None:
        continue
    print("%-12s %12.3f" % ('%s standard error:' % name, se))

print("\nT-values:")
tstats = results.tvalues
for name, tstat in zip(['Intercept', 'x'], tstats):
    print('%s T-value: %12.3f' % (name + ':', tstat))

print("\nP values:")
pvals = results.pvalues
for name, pval in zip(['Intercept', 'x'], pvals):
    print('%s P value: %12.3f' % (name + ':', pval))

if all(p < 0.05 for p in pvals):
    print("\nThe null hypothesis that there is no effect can be rejected.")
else:
    print("\nThe null hypothesis that there is no effect cannot be rejected.")

print(results.summary())