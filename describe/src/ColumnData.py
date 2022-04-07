from dataclasses import dataclass

@dataclass
class ColumnData:
	name: str
	count: int = 0
	mean: float = 0
	std: float = 0
	min: float = 0
	max: float = 0
	median: float = 0
	q1: float = 0
	q3: float = 0

	def get_column_cell_size(self):
		return max(len(self.name), len(str(self.count)), len(str(round(self.mean, 6))),
		len(str(round(self.std, 6))), len(str(round(self.min, 6))), len(str(round(self.max, 6))),
		len(str(round(self.median, 6))), len(str(round(self.q1, 6))), len(str(round(self.q3, 6))))
