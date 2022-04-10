import sys

sys.path.append('.')

import matplotlib.pyplot as plt
import pandas as pd

def main():
	if len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file>', file=sys.stderr)
		return
	data = pd.read_csv(sys.argv[1])
	numerical_columns = data.select_dtypes("number").columns

	plt.xlabel('Courses')
	plt.ylabel('Notes std between houses')
	plt.title('Notes std between houses per course')

	data[numerical_columns] /= data[numerical_columns].max() - data[numerical_columns].min()
	houses_notes = data.groupby(['Hogwarts House']).mean()

	plt.bar(range(data[numerical_columns].shape[1]), [ col.std() for label, col in houses_notes.iteritems() ])
	plt.xticks(range(data[numerical_columns].shape[1]), [ label for label, col in data[numerical_columns].iteritems() ])
	plt.show()

if __name__ == '__main__':
	main()
