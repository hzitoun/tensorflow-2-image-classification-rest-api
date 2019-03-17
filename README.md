A Rest API Serving a [Tensorflow 2 Alpha](https://www.tensorflow.org/alpha) keras deep learning model to classify image.

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

  ```Url : 127.0.0.1/api/recognize_image```

  Body : 
   ```json
   {
      "img_url" : "<IMG_TO_CLASSIFY_URL>" (http://www.stickpng.com/assets/thumbs/580b57fbd9996e24bc43bef3.png)
    }
   ```

  And the Server should do the prediction and then response with : 
  ```json
  {
    "data": {
    "confidence": "67%",
    "prediction": "Pullover"
  },
    "isError": false,
    "message": "Success",
    "statusCode": 200
  }
  ```
