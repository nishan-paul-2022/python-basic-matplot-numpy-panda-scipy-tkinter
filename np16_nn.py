import numpy as np
import matplotlib.pyplot as plt

# Step 1: Creating the data set using numpy array of 0s and 1s.
# As the image is a collection of pixel values in matrix, we will create those matrix of pixel for a, b, c
a = [0, 0, 1, 1, 0, 0,
     0, 1, 0, 0, 1, 0,
     1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 1,
     1, 0, 0, 0, 0, 1]

b = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0]

c = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 0]

y = [[1, 0, 0],  # Creating labels
     [0, 1, 0],
     [0, 0, 1]]

# Step 2 : Visualization of data set
plt.imshow(np.array(a).reshape(5, 6)), plt.title('a'), plt.show()
plt.imshow(np.array(b).reshape(5, 6)), plt.title('b'), plt.show()
plt.imshow(np.array(c).reshape(5, 6)), plt.title('c'), plt.show()

# Step 3: As the data set is in the form of list we will convert it into numpy array.
# Convert the matrix of 0 and 1 into one hot vector. So that we can directly feed it to the neural network.
# These vectors are then stored in a list x.
x = [np.array(a).reshape(1, 30), np.array(b).reshape(1, 30), np.array(c).reshape(1, 30)]
y = np.array(y)  # Labels are also converted into NumPy array
print('{} {}'.format(x, y))


# Step 4 : Defining the architecture or structure of the deep neural network.
# This includes deciding the number of layers and the number of nodes in each layer.
# Our neural network is going to have the following structure.
# Step 5: Declaring and defining all the  function to build deep neural network
def sigmoid(x):  # activation function
    return 1 / (1 + np.exp(-x))


# Creating the Feed forward neural network :
# 1 Input layer(1, 30) | 1 hidden layer (1, 5) | 1 output layer(3, 3)
def f_forward(x, w1, w2):
    # hidden
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # output of layer 2
    # output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer
    return a2


def generate_wt(x, y):  # initializing the weights randomly
    l = []
    for i in range(x * y):
        l.append(np.random.randn())
    return np.array(l).reshape(x, y)


def loss(out, Y):  # for loss we will be using mean square error(MSE)
    s = (np.square(out - Y))
    s = np.sum(s) / len(y)
    return s


def back_prop(x, y, w1, w2, alpha):  # Back propagation of error
    # hidden layer
    z1 = x.dot(w1)  # input from layer 1
    a1 = sigmoid(z1)  # output of layer 2
    # output layer
    z2 = a1.dot(w2)  # input of out layer
    a2 = sigmoid(z2)  # output of out layer
    # error in output layer
    d2 = (a2 - y)
    d1 = np.multiply((w2.dot((d2.transpose()))).transpose(), (np.multiply(a1, 1 - a1)))
    # Gradient for w1 and w2
    w1_adj = x.transpose().dot(d1)
    w2_adj = a1.transpose().dot(d2)
    # Updating parameters
    w1 = w1 - (alpha * w1_adj)
    w2 = w2 - (alpha * w2_adj)
    return w1, w2


def train(x, Y, w1, w2, alpha=0.01, epoch=10):
    acc, losss = [], []
    for j in range(epoch):
        l = []
        for i in range(len(x)):
            out = f_forward(x[i], w1, w2)
            l.append((loss(out, Y[i])))
            w1, w2 = back_prop(x[i], y[i], w1, w2, alpha)

        value = (1 - (sum(l) / len(x))) * 100
        print('epochs:', j + 1, '======== acc:', value)
        acc.append((1 - (sum(l) / len(x))) * 100)
        losss.append(sum(l) / len(x))

    return acc, losss, w1, w2


def predict(x, w1, w2):
    Out = f_forward(x, w1, w2)
    maxm = 0
    k = 0
    for i in range(len(Out[0])):
        if maxm < Out[0][i]:
            maxm = Out[0][i]
            k = i
    if k == 0:
        print("Image is of letter A.")
    elif k == 1:
        print("Image is of letter B.")
    else:
        print("Image is of letter C.")
    plt.imshow(x.reshape(5, 6)), plt.show()


# Step 6: Initializing the weights, as the neural network is having 3 layers, so there will be 2 weight matrix associate with it.
# The size of each matrix depends on the number of nodes in two connecting layers.
w1 = generate_wt(30, 5)
w2 = generate_wt(5, 3)
print('{} {}'.format(w1, w2))

# Step 7 : Training the model.
# The arguments of train function are data set list x, correct labels y, weights w1 w2, learning rate = 0.1, no of epochs or iteration.
# The function will return the matrix of accuracy and loss and also the matrix of trained weights w1, w2
acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)

# Step 8 : Plotting the  graphs of loss and accuracy with respect to number of epochs(Iteration).
plt.plot(acc), plt.ylabel('Accuracy'), plt.xlabel("Epochs:"), plt.show()  # plotting accuracy
plt.plot(losss), plt.ylabel('Loss'), plt.xlabel("Epochs:"), plt.show()  # plotting Loss
print('{} {}'.format(w1, w2))  # the trained weights are

# Step 9: Making prediction.
# The predict function will take the following arguments:
# 1) image matrix | 2) w1 trained weights | 3) w2 trained weights
predict(x[1], w1, w2)

# https://www.geeksforgeeks.org/implementation-of-neural-network-from-scratch-using-numpy/