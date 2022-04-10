from calendar import c
import sys

sys.path.append('.')

from matplotlib import pyplot as plt
import pandas as pd

def plot_courses(data, numerical_columns, course1, course2):
	if not course1 in numerical_columns.array or not course2 in numerical_columns.array:
		print(f'{course1} or {course2} isn\'t a numerical column in the dataset', file=sys.stderr)
		return
	courses = [ data[course1], data[course2] ]
	plt.scatter(courses[0].values, courses[1].values, alpha=0.3)
	plt.plot([0, 1], [0, 1], 'r')

	plt.xlabel(course1)
	plt.ylabel(course2)
	plt.title(f'{course1} vs {course2}')

def plot_all(data, numerical_columns):
	i = 0
	for label, col in data[numerical_columns].iteritems():
		ok = False
		for label2, col2 in data[numerical_columns].iteritems():
			if not ok:
				ok = (label == label2)
				continue
			plt.scatter(i, col.subtract(col2).abs().mean() * 4)
			plt.annotate(f'{label} - {label2}', (i, col.subtract(col2).abs().mean() * 4))
			i += 1

	plt.xlabel('Index')
	plt.ylabel('Mean of differences')
	plt.title('Difference between courses')

def main():
	if len(sys.argv) != 4 and len(sys.argv) != 2:
		print(f'Usage: {sys.argv[0]} <csv_file> [course1 <course2>]', file=sys.stderr)
		return
	data = pd.read_csv(sys.argv[1])
	numerical_columns = data.select_dtypes("number").columns
	data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].min()) / (data[numerical_columns].max() - data[numerical_columns].min())
	if len(sys.argv) == 4:
		plot_courses(data, numerical_columns, sys.argv[2], sys.argv[3])
	else:
		plot_all(data, numerical_columns)
	plt.show()

if __name__ == '__main__':
	main()
