import os
import webbrowser
import subprocess
from tk10_dynamically_create_interface import dynamically_create_interface


def get_project_list():
	directory = 'E:/CODE/PYTHON'
	prefix = 'done_backend'
	project_list = list()
	port_numbers = 8000

	for project_name in os.listdir(directory):
		path = f'{directory}/{project_name}'
		check1 = os.path.isdir(path)
		check2 = project_name.startswith(prefix)
		if check1 and check2:
			port_numbers += 1
			project_list.append((project_name, path, port_numbers))

	return project_list


# https://stackoverflow.com/questions/55920419/how-to-write-to-command-line-using-python
if __name__ == '__main__':
	project_list = get_project_list()
	function_packages = list()

	for project_name, path, port_number in project_list:

		def function(path, link, run_server):
			os.chdir(path)
			webbrowser.open(link)
			subprocess.Popen(['start', 'cmd', '/k', run_server], shell=True)

		link = f'http://127.0.0.1:{port_number}/'

		run_server = 'D:/C-PART-2/m2021/Scripts/activate.bat && ' \
		             'py manage.py makemigrations main && ' \
		             'py manage.py migrate && ' \
		             f'py manage.py runserver {port_number}'

		function_package = (project_name, function, path, link, run_server)
		function_packages.append(function_package)

	dynamically_create_interface('run_server', function_packages)