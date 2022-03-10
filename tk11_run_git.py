import os
import shutil
import subprocess

import tkinter as tk
from functools import partial
from tkinter import *
from tk10_dynamically_create_interface import dynamically_create_interface


def create_django_project(directory, entry):
	project_name = entry.get()
	cmd = 'D:/C-PART-2/m2021/Scripts/activate.bat && ' \
	      f'django-admin startproject {project_name} && ' \
	      f'cd {project_name} && ' \
	      'py manage.py migrate && ' \
	      'py manage.py createsuperuser && ' \
	      'py manage.py startapp main'

	path = f'{directory}/{project_name}'
	if os.path.exists(path):
		print('already exists')
		return False

	os.chdir(directory)
	subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)


def clone_git_repo(directory, entry):
	repo_name = entry.get()
	cmd = f'git clone https://nishan-paul-2022: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@github.com/nishan-paul-2022/{repo_name}.git && ' \
	      'git config --global credential.helper store'
	os.chdir(directory)
	subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)


def cut_dot_git(directory, entry):
	repo_name, project_name = entry.get().split(', ')
	source = f'{directory}/{repo_name}/.git'
	destination = f'{directory}/{project_name}/.git'
	shutil.move(source, destination)
	shutil.rmtree(source)


def update_git(directory, entry):
	path = entry.get()
	update = f'{directory}/update_git.bat'
	os.chdir(path)
	subprocess.Popen(['start', 'cmd', '/k', update], shell=True)


if __name__ == '__main__':
	window = Tk()
	window_title = 'run_git'
	window.title(window_title)
	window.maxsize(350, 350)

	directory = 'E:/CODE/PYTHON'
	functions = {
		'create_django_project': create_django_project,
		'clone_git_repo': clone_git_repo,
		'cut_dot_git': cut_dot_git,
		'update_git': update_git
	}

	for function_name, function in functions.items():
		entry = Entry(window, width=40)
		entry.focus_set()
		entry.pack()
		Button(window, text=function_name, width=20, command=partial(function, directory, entry)).pack(pady=20)

	window.mainloop()