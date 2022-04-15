import pandas as pd
import numpy as np
import sys
import os

def sigmoid(x):
	sigmoid = np.zeros(x.shape)
	for i in range(len(x)):
		sigmoid[i] = 1 / (1 + np.exp(-x[i]))
	return sigmoid

def predict(data, weights):
	return sigmoid(weights.T @ data.T)

def choose_house(predictions):
	res = np.zeros(predictions.shape[0])
	for i in range(len(predictions)):
		cur_max = -1
		cur_max_idx = 0
		for j in range(len(predictions[i])):
			if cur_max <= predictions[i][j]:
				cur_max = predictions[i][j]
				cur_max_idx = j
			res[i] = cur_max_idx
	return res

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

	numerical_columns = data[['Defense Against the Dark Arts', 'Ancient Runes', 'Charms', 'Transfiguration']].columns
	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())
	data['Hogwarts House'].replace({ 'Gryffindor': 0, 'Slytherin': 1, 'Ravenclaw': 2, 'Hufflepuff': 3 }, inplace=True)

	weights = pd.DataFrame()
	try:
		weights = pd.read_csv(sys.argv[2])
	except:
		print('Invalid weights file', file=sys.stderr)
		return 1
	predictions = choose_house(predict(data[numerical_columns].to_numpy(copy=True), weights.to_numpy()).T)

	predictions = pd.DataFrame(predictions, columns=['Hogwarts House'], index=data['Index'])
	predictions['Hogwarts House'].replace({ 0: 'Gryffindor', 1: 'Slytherin', 2: 'Ravenclaw', 3: 'Hufflepuff' }, inplace=True)
	predictions.to_csv('resources/houses.csv')
	print(predictions)

if __name__ == '__main__':
	main()
