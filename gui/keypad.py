from tkinter import Misc

from math import ceil

from typing import (
	Callable,
	Literal
)

from tkinter.ttk import (
	Button,
	Frame
)

type _KeyMap = dict[str, Callable[[], None]]
type _WrapDirection = Literal["column", "columnreverse", "row", "rowreverse"]


class Keypad(Frame):
	def __init__(self, master: Misc | None = None, **kwargs) -> None:
		super().__init__(master, **kwargs)

		self.key_map: _KeyMap = {},
		self.wrap_count: int = 1,
		self.wrap_direction: _WrapDirection = "column",

	def set_layout(
		self,
		key_map: _KeyMap,
		wrap_count: int,
		wrap_direction: _WrapDirection
	) -> None:
		self.key_map = key_map
		self.wrap_count = wrap_count
		self.wrap_direction = wrap_direction

	def draw_keys(self, column_start: int = 1, row_start: int = 1) -> None:
		if "reverse" in self.wrap_direction:
			key_map = dict(reversed(self.key_map.items()))
		else:
			key_map = self.key_map

		if "column" in self.wrap_direction:
			columns = self.wrap_count
			rows = ceil(len(self.key_map) / self.wrap_count)
			for index, key_text in enumerate(key_map):
				key = Button(self, text = key_text, command = key_map[key_text])
				key.grid(
					column = (index % columns) + column_start,
					row = (index // columns) + row_start,
					sticky="nsew",
				)
		elif "row" in self.wrap_direction:
			columns = ceil(len(self.key_map) / self.wrap_count)
			rows = self.wrap_count
			for index, key_text in enumerate(key_map):
				key = Button(self, text = key_text, command = key_map[key_text])
				key.grid(
					column = (index // rows) + column_start,
					row = (index % rows) + row_start,
					sticky="nsew"
				)

		column_indices = tuple(range(column_start, columns + column_start))
		row_indices = tuple(range(row_start, rows + row_start))

		self.columnconfigure(column_indices, weight = 1)
		self.rowconfigure(row_indices, weight = 1)