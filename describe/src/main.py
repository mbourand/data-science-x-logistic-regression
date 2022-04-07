import sys

sys.path.append('.')

import pandas as pd
from ColumnData import ColumnData
import shared.src.utils as utils

def print_stat(label, var_name, columns_data):
	print(label, end='  ')
	for column in columns_data:
		print(f'{round(column.__dict__[var_name], 6):>{column.get_column_cell_size()}}', end='  ')
	print()

def print_stat_str(label, var_name, columns_data):
	print(label, end='  ')
	for column in columns_data:
		print(f'{column.__dict__[var_name]:>{column.get_column_cell_size()}}', end='  ')
	print()

def main():
	if len(sys.argv) != 2:
		print(f'Usage: ./{sys.argv[0]} <csv_file>')
		return
	data = pd.read_csv(sys.argv[1])
	numerical_data = data.select_dtypes(include=['float64', 'int64'])

	columns_data = []
	for col in numerical_data.columns:
		columns_data.append(ColumnData(col))

	for column in columns_data:
		column.count = utils.count(numerical_data[column.name])
		column.mean = utils.mean(numerical_data[column.name])
		column.std = utils.std(numerical_data[column.name])
		column.min = utils.min(numerical_data[column.name])
		column.q1 = utils.percentile(numerical_data[column.name], 25)
		column.median = utils.percentile(numerical_data[column.name], 50)
		column.q3 = utils.percentile(numerical_data[column.name], 75)
		column.max = utils.max(numerical_data[column.name])

	print_stat_str(' ' * 5, 'name', columns_data)
	print_stat('count', 'count', columns_data)
	print_stat('mean ', 'mean', columns_data)
	print_stat('std  ', 'std', columns_data)
	print_stat('min  ', 'min', columns_data)
	print_stat('25%  ', 'q1', columns_data)
	print_stat('50%  ', 'median', columns_data)
	print_stat('75%  ', 'q3', columns_data)
	print_stat('max  ', 'max', columns_data)

if __name__ == '__main__':
    main()
