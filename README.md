Since [Tensorflow 2 Alpha](https://www.tensorflow.org/alpha) was annonced recently, I wanted to try it out by making a simple image classification model trained on fashion mnist data set using a 3 layers neural networks. The model is served as a Rest API.

Defined classes are 'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'.

## Training set

[keras.datasets.fashion_mnist](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/fashion_mnist)

## Libs

- Tensorflow 2.0.0-alpha0
- Keras
- Python 3
- skimage
- Flask 
- Numpy

## How to run?

1- Install the required libs (with ```conda install``` or ```pip install```).

2- Run ```python train_and_export_model.py``` to train the deep neural networks and export to export it to ```fashion_mnist_classifier savedModel```.

3- Run ```python app.py``` to start the server that runs the port 5000.

4- Send a POST query to the ```http://127.0.0.1/api/recognize_image``` with a body consisting of a JSON content:

   ```json
   {
      "img_url" : "<IMG_TO_CLASSIFY_URL> (http://www.stickpng.com/assets/thumbs/580b57fbd9996e24bc43bef3.png)"
    }
   ```

  And the Server should do the prediction and then respond with : 
  ```json
  {
    "data": {
    "confidence": "89%",
    "prediction": "Dress"
  },
    "isError": false,
    "message": "Success",
    "statusCode": 200
  }
  ```
