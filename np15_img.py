import numpy as np
import cv2
from PIL import Image as pim
import matplotlib.image as mim
import pandas as pd
from keras.preprocessing.image import load_img, img_to_array, array_to_img


def fst():
    array_created = np.full((500, 500, 3), 255, dtype=np.uint8)   # creating an array using np.full | 255 is code for white color
    cv2.imshow("image1", array_created)  # displaying the image
    cv2.waitKey(1000)

    array = np.zeros([500, 500, 3], dtype=np.uint8)  # creating array using np.zeroes()
    array[:, :] = [255, 255, 255]   # setting RGB color values as 255,255,255
    cv2.imshow("image2", array)  # displaying the image
    cv2.waitKey(1000)


def sec():
    # create a numpy array from scratch using arange function.
    # 1024x720 = 737280 is the amount of pixels.
    # np.uint8 is a data type containing numbers ranging from 0 to 255 and no non-negative integers
    array = np.arange(0, 737280, 1, np.uint8)
    print(type(array))  # check type of array
    print(array.shape)  # our array will be of width 737280 pixels. That means it will be a long dark line

    array = np.reshape(array, (1024, 720))  # Reshape the array into a familiar resolution
    print(array.shape)  # show the shape of the array
    print(array)  # show the array

    data = pim.fromarray(array)  # creating image object of above array
    data.save('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_numpy.png')  # saving the final output as a PNG E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
    img = cv2.imread('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_numpy.png')
    cv2.imshow("image3", img)
    if cv2.waitKey(0) & 0xff == 'q':
        return


def thrd():
    img = pim.open('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_bear.png')
    print(img.format)
    print(img.mode)
    print(img.size)

    numpydata = np.asarray(img)
    print(type(numpydata))
    print(numpydata.shape)

    numpydata1 = np.array(img)
    print(type(numpydata1))
    print(numpydata1.shape)
    print(numpydata1)

    pimg = pim.fromarray(numpydata)  # Below is the way of creating Pillow image from our numpy array
    print(type(pimg))
    print(pimg.mode)
    print(pimg.size)


def frth():
    img = load_img('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_bear.png')
    print(type(img))
    print(img.format)
    print(img.mode)
    print(img.size)


def fifth():
    img = load_img('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_bear.png')
    img_numpy_array = img_to_array(img)  # convert the given image into numpy array
    print("Image is converted and NumPy array information :")

    print(type(img_numpy_array))  # <class 'numpy.ndarray'>
    print("type:", img_numpy_array.dtype)  # type: float32
    print("shape:", img_numpy_array.shape)  # shape: (200, 400, 3)

    img_pil_from_numpy_array = array_to_img(img_numpy_array)  # convert back to image
    print("converting NumPy array into image:", type(img_pil_from_numpy_array))  # <class 'PIL.PngImagePlugin.PngImageFile'>


def sixth():
    img = pim.open('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_bear.png')
    img_to_matrice = np.asarray(img)  # convert image object into array 
    print(img_to_matrice.shape)  # printing shape of image 


def seventh():
    imageMat = mim.imread('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_fruit.png')
    print("Image shape:", imageMat.shape)
    
    if imageMat.shape[2] == 3:  # if image is colored (RGB)
        imageMat_reshape = imageMat.reshape(imageMat.shape[0], -1)  # reshape it from 3D matrice to 2D matrice
        print("Reshaping to 2D array:", imageMat_reshape.shape)
    else:  # if image is grayscale
        imageMat_reshape = imageMat  # remain as it is

    np.savetxt('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_file1.csv', imageMat_reshape)  # saving matrice to .csv E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
    loaded_2D_mat = np.loadtxt('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_file1.csv')  # retrieving matrice from the .csv E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
    loaded_mat = loaded_2D_mat.reshape(loaded_2D_mat.shape[0], loaded_2D_mat.shape[1] // imageMat.shape[2], imageMat.shape[2])  # reshaping it to 3D matrice
    print("Image shape of loaded Image:", loaded_mat.shape)
    
    if (imageMat == loaded_mat).all():  # check if both matrice have same shape or not
        print("Yes, The loaded matrice from CSV E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter is same as original image matrice")


def eight():
    imageMat = mim.imread('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_fruit.png')
    print("Image shape:", imageMat.shape)

    if imageMat.shape[2] == 3:  # if image is colored (RGB)
        imageMat_reshape = imageMat.reshape(imageMat.shape[0], -1)  # reshape it from 3D matrice to 2D matrice
        print("Reshaping to 2D array:", imageMat_reshape.shape)
    else:  # if image is grayscale
        imageMat_reshape = imageMat  # remain as it is

    mat_df = pd.DataFrame(imageMat_reshape)  # converting it to dataframe
    mat_df.to_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_file2.csv', header=None, index=None)  # exporting dataframe to CSV E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
    loaded_df = pd.read_csv('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/np15_file2.csv', sep=',', header=None)  # retrieving dataframe from CSV E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter
    loaded_2D_mat = loaded_df.values  # getting matrice values
    loaded_mat = loaded_2D_mat.reshape(loaded_2D_mat.shape[0], loaded_2D_mat.shape[1] // imageMat.shape[2], imageMat.shape[2])  # reshaping it to 3D matrice
    print("Image shape of loaded Image :", loaded_mat.shape)

    if (imageMat == loaded_mat).all():  # check if both matrice have same shape or not
        print("Yes, The loaded matrice from CSV E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter is same as original image matrice")


if __name__ == '__main__':
    fst()
    sec()
    thrd()
    frth()
    fifth()
    sixth()
    seventh()
    eight()

# https://www.geeksforgeeks.org/create-a-white-image-using-numpy-in-python/
# https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
# https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
# https://www.geeksforgeeks.org/how-to-convert-an-image-to-numpy-array-and-saveit-to-csv-file-using-python/