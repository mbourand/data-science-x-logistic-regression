import sys
import math

sys.path.append('.')

import matplotlib.pyplot as plt
import pandas as pd

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file>', file=sys.stderr)
		return
	data = pd.DataFrame()
	try:
		data = pd.read_csv(sys.argv[1])
	except:
		print('Invalid dataset file', file=sys.stderr)
		return
	numerical_columns = data.select_dtypes("number").columns

	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())

	fig, ax = plt.subplots(4, 4, figsize=(20, 20))

	for house in 'Gryffindor Slytherin Hufflepuff Ravenclaw'.split():
		x = 0
		y = 0
		for label, col in data.loc[data['Hogwarts House'] == house][numerical_columns].iteritems():
			ax[y, x].hist(col, bins=50, density=True, alpha=0.3)
			ax[y, x].set_title(label)
			x += 1
			if x >= math.sqrt(data[numerical_columns].shape[1]):
				y += 1
				x = 0

	fig.savefig('histogram.png')

if __name__ == '__main__':
	main()
