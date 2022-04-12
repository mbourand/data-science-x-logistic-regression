from calendar import c
import sys

sys.path.append('.')

from matplotlib import pyplot as plt
import seaborn as sns
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

	fig = sns.pairplot(data, hue='Hogwarts House', vars=numerical_columns, plot_kws={'alpha':0.3}, diag_kind='hist', diag_kws={'alpha': 0.3})
	fig.savefig('pair_plot.png')

if __name__ == '__main__':
	main()
