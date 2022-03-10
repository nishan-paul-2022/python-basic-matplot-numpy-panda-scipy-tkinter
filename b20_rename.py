import glob
import os
import re


def rename():
	path = 'E:/MOVIES - TV SERIES/THE TWILIGHT ZONE (1959)/SEASON 01/'
	sub = path + '*.srt'
	video = path + '*.mkv'
	slist, vlist = glob.glob(sub), glob.glob(video)

	for i in range(len(slist)):
		oname, nname = vlist[i], slist[i].replace('.srt', '.mkv')
		os.rename(oname, nname)


def rename2():
	path = 'E:/CODE/PYTHON/OPENCV/'
	sub = path + '*.py'
	slist = glob.glob(sub)

	for i in range(len(slist)):
		oname = slist[i]
		print(oname)
		nname = re.sub(r'-(?:(?<!\b[0-9]{4}-)|(?![0-9]{2}(?:[0-9]{2})?\b))', '_', oname)
		os.rename(oname, nname)


def rename3():
	path = 'E:/CODE/PYTHON/OPENCV/'
	sub = path + '*.py'
	slist = glob.glob(sub)

	for i in range(len(slist)):
		oname = slist[i]
		print(oname, end=' ')
		nname = re.sub(r'\d', str(i+1), oname)
		print(nname)
		os.rename(oname, nname)


def rename4():
	path = 'E:/CODE/PYTHON/done_tutorial_pytorch/file/pt30_samples/'

	for count, filename in enumerate(os.listdir(path)):
		if filename[0] == 'i':
			os.rename(path + filename, path + filename[1:])


def get_name():
	path = "E:/CODE/PYTHON/done_tutorial_ml_collection"
	os.chdir(path)
	for file in glob.glob("*.py"):
		print(file)

	for file in os.listdir(path):
		d = os.path.join(path, file)
		if os.path.isdir(d):
			print(d)


# rename()
# rename2()
# rename3()
# rename4()
# get_name()