import os
import subprocess

import tkinter as tk
from functools import partial
from tkinter import *
from tk10_dynamically_create_interface import dynamically_create_interface


def update_git(path):
	directory = 'E:/CODE/PYTHON'
	update = f'{directory}/update_git.bat'
	os.chdir(path)
	subprocess.Popen(['start', 'cmd', '/k', update], shell=True)


if __name__ == '__main__':
	window_title = 'update_selected_git'

	function_packages = list()

	paths = {
		'done_backend_barcode_scanner': 'E:\CODE\PYTHON\done_backend_barcode_scanner',
		'done_backend_job_recruitment': 'E:\CODE\PYTHON\done_backend_job_recruitment',
		'done_tutorial_basic_matplot_numpy_panda_scipy_tkinter': 'E:\CODE\PYTHON\done_tutorial_basic_matplot_numpy_panda_scipy_tkinter',
		'done_tutorial_opencv': 'E:\CODE\PYTHON\done_tutorial_opencv',
		'SESSIONAL': 'E:\CODE\SESSIONAL',
		'done_expresso': 'E:\CODE\XAMPP\htdocs\WEB\PROJECT\done_expresso'
	}

	for project_name, project_path in paths.items():
		function_package = (project_name, update_git, project_path)
		function_packages.append(function_package)

	dynamically_create_interface(window_title, function_packages)
