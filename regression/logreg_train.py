import pandas as pd
import numpy as np
import sys

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def predict(data, weights):
	return sigmoid(np.dot(data, weights))

def house_result(house):
	return {'Gryffindor': house == 'Gryffindor', 'Slytherin': house == 'Slytherin', 'Ravenclaw': house == 'Ravenclaw', 'Hufflepuff': house == 'Hufflepuff'}

def choose_house(predictions):
	return max(predictions, key=predictions.get)

def train(data, numerical_columns, iterations=100, learning_rate=0.1):
	weights = {
		'Gryffindor': np.random.rand(numerical_columns.shape[0]),
		'Slytherin': np.random.rand(numerical_columns.shape[0]),
		'Ravenclaw': np.random.rand(numerical_columns.shape[0]),
		'Hufflepuff': np.random.rand(numerical_columns.shape[0])
	}

	for i in range(iterations):
		for index, row in data.iterrows():
			predictions = {
				'Gryffindor': predict(row[numerical_columns], weights['Gryffindor']),
				'Slytherin': predict(row[numerical_columns], weights['Slytherin']),
				'Ravenclaw': predict(row[numerical_columns], weights['Ravenclaw']),
				'Hufflepuff': predict(row[numerical_columns], weights['Hufflepuff'])
			}
			y = house_result(row['Hogwarts House'])

			for house in predictions:
				for j in range(len(weights[house])):
					weights[house][j] += -learning_rate * (predictions[house] - y[house]) * row[numerical_columns[j]]
		print(i)
	return weights

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file>]', file=sys.stderr)
		return
	data = pd.read_csv(sys.argv[1])
	data.dropna(inplace=True)
	numerical_columns = data[['Defense Against the Dark Arts', 'Ancient Runes', 'Herbology' ]].columns

	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())
	weights = train(data, numerical_columns)
	ok = 0
	for index, row in data.iterrows():
		predictions = {
			'Gryffindor': predict(row[numerical_columns], weights['Gryffindor']),
			'Slytherin': predict(row[numerical_columns], weights['Slytherin']),
			'Ravenclaw': predict(row[numerical_columns], weights['Ravenclaw']),
			'Hufflepuff': predict(row[numerical_columns], weights['Hufflepuff'])
		}
		if row['Hogwarts House'] == choose_house(predictions):
			ok += 1
	print(f'Prediction rate: {ok / data.shape[0] * 100}%')
	with open('resources/weights.csv', 'w+') as f:
		for house in weights:
			f.write(f'{house},')
		f.write('\n')
		for i in range(len(weights['Gryffindor'])):
			for house in weights:
				f.write(f'{weights[house][i]},')
			f.write('\n')

if __name__ == '__main__':
	main()
