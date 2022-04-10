from calendar import c
import sys

sys.path.append('.')

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file>]', file=sys.stderr)
		return
	data = pd.read_csv(sys.argv[1])
	numerical_columns = data.select_dtypes("number").columns
	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())

	sns.pairplot(data, hue='Hogwarts House', vars=numerical_columns)
	plt.show()

if __name__ == '__main__':
	main()
