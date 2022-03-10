import math
import tkinter as tk
from functools import partial
from tkinter import *


# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
def dynamically_create_interface(window_title, function_packages):
	window = Tk()
	window.title(window_title)
	window.minsize(400, 200)

	function_exit = ['EXIT', window.destroy]
	function_packages.append(function_exit)

	count = len(function_packages)
	row = math.ceil(math.sqrt(count))
	column = row

	idx = 0
	for i in range(row):
		for j in range(column):
			if idx >= count:
				break
			function_name = function_packages[idx][0]
			function_set = function_packages[idx][1:]

			button = Button(window, text=function_name, padx=10, pady=10, bg="#2C3333", fg="white", command=partial(*function_set))
			button.grid(row=i, column=j, sticky="NSEW", padx=10, pady=10)
			idx += 1

	for i in range(row):
		Grid.rowconfigure(window, i, weight=1)
	for j in range(column):
		Grid.columnconfigure(window, j, weight=1)

	window.mainloop()


def function(argument1, argument2):
	print(f'{argument1}, {argument2}')


if __name__ == '__main__':
	function_packages = list()
	argument1, argument2 = 10, 20
	function_package = ('project_name', function, argument1, argument2)
	function_packages.append(function_package)
	dynamically_create_interface('dynamically_create_interface', function_packages)