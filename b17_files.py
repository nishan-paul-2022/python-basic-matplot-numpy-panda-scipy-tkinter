import os

f = open("E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b17_files1.txt", "r")
g = open("E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b17_files2.txt", "w")
h = open("E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b17_files3.txt", "a")

# os.rename("E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b17_files4.txt", "b17_files5.txt")
# os.remove("E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b17_files6.txt")

# os.mkdir(r'b17_directory')
# os.rmdir(r'b17_directory')
# os.chdir(r'b17_directory')
print(os.getcwd())

# f.seek(10)
print(f.tell())

# print(f.read())
# print(f.read(10))

lst = f.readlines()
for i in lst:
    print(i, end='')

g.write("GOT")
g.write("-is the best\n")
g.write("WestWord is love\n")

h.write("\nScam-1992: A Harshad Mehta Story")

f.close()
g.close()
h.close()

# -- Functions --

# open()
# r, r+
# w, w+ 
# a, a+

# os.rename()
# os.remove()

# os.mkdir()
# os.rmdir()
# os.chdir()
# os.getcwd()

# f.seek()
# f.tell()

# f.read()
# f.read([])
# f.readlines()

# f.write()
