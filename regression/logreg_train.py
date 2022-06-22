import pandas as pd
import numpy as np
import sys

def sigmoid(x):
	sigmoid = np.zeros(x.shape)
	for i in range(len(x)):
		sigmoid[i] = 1 / (1 + np.exp(-x[i]))
	return sigmoid

def predict(data, weights):
	return sigmoid(weights.T @ data.T)

def house_result(data):
	res = np.zeros((data.shape[0], 4))
	for index in range(data.shape[0]):
		res[index][data.iloc[index]] = 1
	return res

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


def winrate(data, numerical_columns, weights):
	ok = 0
	predictions = choose_house(predict(data[numerical_columns].to_numpy(copy=True), weights).T)
	for index in range(data.shape[0]):
		if data['Hogwarts House'].iloc[index] == predictions[index]:
			ok += 1
	print(f'Prediction rate: {ok / data.shape[0] * 100}%')

def train(data, numerical_columns, iterations=30000, learning_rate=0.005):
	weights = np.zeros((numerical_columns.shape[0], 4))
	for i in range(len(weights)):
		for j in range(len(weights[i])):
			weights[i][j] = np.random.uniform(-1, 1)

	real = house_result(data['Hogwarts House'])
	for i in range(iterations):
		predictions = predict(data[numerical_columns].to_numpy(copy=True), weights)
		gradient = ((predictions - real.T) @ data[numerical_columns].to_numpy(copy=True)) / data.shape[0]
		weights += -learning_rate * gradient.T
		if i % 100 == 0:
			print(f'Iteration {i}/{iterations}')
	return weights

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file>]', file=sys.stderr)
		return
	data = pd.read_csv(sys.argv[1])
	numerical_columns = data[['Defense Against the Dark Arts', 'Ancient Runes', 'Charms', 'Transfiguration']].columns
	data.dropna(inplace=True, subset=numerical_columns)
	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())
	data['Hogwarts House'].replace({ 'Gryffindor': 0, 'Slytherin': 1, 'Ravenclaw': 2, 'Hufflepuff': 3 }, inplace=True)

	weights = train(data, numerical_columns)
	winrate(data, numerical_columns, weights)
	pd.DataFrame({'Gryffindor': weights.T[0], 'Slytherin': weights.T[1], 'Ravenclaw': weights.T[2], 'Hufflepuff': weights.T[3]}).to_csv('resources/weights.csv', index=False)

if __name__ == '__main__':
	main()
