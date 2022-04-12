import pandas as pd
import numpy as np
import sys
import os

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def predict(data, weights):
	return sigmoid(np.dot(data, weights))

def choose_house(predictions):
	return max(predictions, key=predictions.get)

def main():
	if len(sys.argv) != 3:
		print(f'Usage: {sys.argv[0]} <csv_file> <weights_file>', file=sys.stderr)
		return 1

	data = pd.DataFrame()
	try:
		data = pd.read_csv(sys.argv[1])
	except:
		print('Invalid dataset file', file=sys.stderr)
		return 1

	numerical_columns = data[['Defense Against the Dark Arts', 'Ancient Runes', 'Herbology' ]].columns

	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())
	weights = pd.DataFrame()
	try:
		weights = pd.read_csv(sys.argv[2])
	except:
		print('Invalid weights file', file=sys.stderr)
		return 1

	with open('resources/houses.csv', 'w+') as f:
		for index, row in data.iterrows():
			predictions = {
				'Gryffindor': predict(row[numerical_columns], weights['Gryffindor']),
				'Slytherin': predict(row[numerical_columns], weights['Slytherin']),
				'Ravenclaw': predict(row[numerical_columns], weights['Ravenclaw']),
				'Hufflepuff': predict(row[numerical_columns], weights['Hufflepuff'])
			}
			f.write(f'{row["Index"]},{choose_house(predictions)}\n')

if __name__ == '__main__':
	main()
