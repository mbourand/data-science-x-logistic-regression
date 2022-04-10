#!/bin/bash
if [ $# -eq 2 ]; then
	python visualisation/src/scatter_plot.py resources/datasets/dataset_train.csv "$1" "$2"
elif [ $# -eq 0 ]; then
	python visualisation/src/scatter_plot.py resources/datasets/dataset_train.csv
else
	echo "Usage: ./scatter_plot.sh [feature_1 <feature_2>]"
fi
