import numpy as np
import pandas as pd
import scipy
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import matplotlib.pyplot as plt

def continous_analysis(data, col):
    colSeri = data[data[col].isnull() != True][col]
    
    colSkew = colSeri.skew()
    colKur = colSeri.kurtosis()
    print('*****', col, '*****')
    print(col,"mean:", colSeri.mean())
    print(col,"median:", colSeri.median())
    print(col, "mode:", colSeri.mode().values)
    print(col, "range:", colSeri.ptp())
    print(col, "min:", colSeri.min())
    print(col, "max:", colSeri.max())
    print(col, "variance:", colSeri.var())
    print(col, "std:", colSeri.std())
    print(col, "skew:", colSkew)
    print(col, "kur:", colKur)
    if (colSkew > 0): 
        print("The distribution of", col, "is right(positive) skew")
    elif (colSkew < 0):
        print("The distribution of", col, "is left(negative) skew")
    else:
        print("The distribution of", col, "is normal distribution")
        
    if (colKur > 0): 
        print("The distribution of", col, "is upper normal distribution")
    elif (colKur < 0):
        print("The distribution of", col, "is lower normal distribution")
    else:
        print("The distribution of", col, "is normal distribution")
    
    
    print("\n")

def continous_outlier(data, col):
    q1 = np.percentile(data[col], 25)
    q3 = np.percentile(data[col], 75)
    iqr = scipy.stats.iqr(data[col])
    upper = data[data[col] > (q3 + 1.5 * iqr)]
    lower = data[data[col] < (q1 - 1.5 * iqr)]
    outlier_per = np.round((len(upper) + len(lower)) / len(data), 4) * 100
    print(col, "upper outlier count:", len(upper))
    print(col, "lower outlier count:", len(lower))
    print(col, "percent outlier on total:", outlier_per, "%")
    print(col, "upper outlier are:", upper[col].values)
    print(col, "lower outlier are:", lower[col].values)

def category_and_category(data, cat1, cat2):
    table_crosstab = pd.crosstab(data[cat1], data[cat2])
    table_crosstab
    table_crosstab.plot(kind='bar', stacked=True)
    plt.show()
    stat, p, dof, expected = chi2_contingency(table_crosstab)
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    alpha = 1.0 - prob
    if (p <= alpha):
        print(cat1, "and", cat2, "are dependent")
    else:
        print(cat1, "and", cat2, "are independent")