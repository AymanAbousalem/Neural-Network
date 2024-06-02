import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data() 

# Function to display a random MNIST digit image
def display_random_mnist_image():
    # Generate a random index
    random_index = np.random.randint(0, len(x_train))
    
    # Get the random image and its label
    random_image = x_train[random_index] 
    random_label = y_train[random_index] 
    
    random_image = 255.0 - random_image

    # Display the image with its label
    plt.imshow(random_image, cmap='gray')
    plt.title(f'Label: {random_label}')
    plt.axis('off')
    plt.show()

# Call the function to display the random MNIST image
if __name__ == "__main__":
    display_random_mnist_image()


#python random_mnist_image.py


