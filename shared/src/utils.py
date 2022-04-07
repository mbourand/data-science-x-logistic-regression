import pandas as pd
import math

def count(column: pd.Series):
	i = 0
	for _, k in column.iteritems():
		if not math.isnan(k):
			i += 1
	return i

def mean(column: pd.Series):
	i = 0
	for _, k in column.iteritems():
		if not math.isnan(k):
			i += k
	return i / count(column)

def std(column: pd.Series):
	sum = 0
	col_mean = mean(column)
	for _, k in column.iteritems():
		if not math.isnan(k):
			sum += (k - col_mean) ** 2
	return math.sqrt(sum / count(column))

def percentile(column: pd.Series, percent):
	size = count(column)
	cpy = column.sort_values()
	i = 0
	for _, k in cpy.iteritems():
		if not math.isnan(k):
			i += 1
			if i == math.ceil(size * (percent / 100)):
				return k

def min(column: pd.Series):
	m = math.inf
	for _, k in column.iteritems():
		if not math.isnan(k):
			if k < m:
				m = k
	return m

def max(column: pd.Series):
	m = -math.inf
	for _, k in column.iteritems():
		if not math.isnan(k):
			if k > m:
				m = k
	return m
