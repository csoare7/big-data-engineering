import csv

from scipy import stats
import scipy as sp
import numpy as np
import pandas as pd

from statsmodels.stats.proportion import proportion_confint
from statsmodels.stats.weightstats import _tconfint_generic


trips = pd.read_csv('sample10000.csv')

# check how many passengers in the sample paid for their ride with cash.
paid_cash = trips.payment_type==2
print("Sum of passangers who paid cash: ", paid_cash.sum())

# build a 99% confidence interval for the proportion of cash payers.
confidence_interval = proportion_confint(paid_cash.sum(), paid_cash.size, alpha=0.01)
print("Confidence interval:", confidence_interval)

trips_distance = trips["trip_distance"]
# estimate the average trip distance in miles
avg_distance = trips_distance.mean()
print("Avg trip distance:", avg_distance)

# standard deviation of the estimator from the previous question
dist_std_deviation = trips_distance.std(ddof=1)
print("Std dev", dist_std_deviation)

# calculate 95% confidence interval for the mean trip distance.
sqrt = np.sqrt(trips_distance.size)
s = trips_distance.std(ddof=1) / sqrt
print("Std dev of estimator", s)

mean_confidence_interval = _tconfint_generic(trips_distance.mean(), s, trips_distance.size - 1, 0.05, "two-sided")
print("Mean confidence interval:", mean_confidence_interval)





