# Advanced-Linear-Regression

Coefficients:
Intercept:        802.698
x:                  0.037

Standard errors:
x standard error:        0.307

T-values:
Intercept: T-value:        1.912
x: T-value:       -0.121

P values:
Intercept: P value:        0.070
x: P value:        0.905

The null hypothesis that there is no effect cannot be rejected.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.008
Model:                            OLS   Adj. R-squared:                 -0.087
Method:                 Least Squares   F-statistic:                   0.08127
Date:                Sat, 16 Mar 2024   Prob (F-statistic):              0.922
Time:                        16:03:49   Log-Likelihood:                -213.96
No. Observations:                  24   AIC:                             433.9
Df Residuals:                      21   BIC:                             437.5
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        802.6982    419.729      1.912      0.070     -70.176    1675.572
x1            -0.0372      0.307     -0.121      0.905      -0.676       0.601
x2            -0.3134      0.804     -0.390      0.701      -1.985       1.358
==============================================================================
Omnibus:                       29.657   Durbin-Watson:                   2.223
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               51.917
Skew:                           2.546   Prob(JB):                     5.33e-12
Kurtosis:                       8.099   Cond. No.                     1.42e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.42e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
