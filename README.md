A Rest API Serving a Tensorflow 2 keras deep learning model to classify image.

## Training set

keras.datasets.fashion_mnist

## Libs

- Tensorflow 2.0.0-alpha0
- Keras
- Python 3
- skimage
- Flask 
- Numpy

# How to run?

1- Install the required libs (with conda install or pip install).

2- Run python train_and_export_model.py to train the deep neural networks and export the to fashion_mnist_classifier savedModel.

3- Run app.py to start the server that runs the port 5000.

4- Send a POST query to the 127.0.0.1/api/recognize_image with a body consisting of a JSON content:

  Url : 127.0.0.1/api/recognize_image

  Body : {
    "img_url" : "<IMG_TO_CLASSIFY_URL>" (http://www.stickpng.com/assets/thumbs/580b57fbd9996e24bc43bef3.png)
  }

  And the Server should do the prediction and then response with : 
  
  {
    "data": {
    "confidence": "67%",
    "prediction": "Pullover"
  },
    "isError": false,
    "message": "Success",
    "statusCode": 200
  }
