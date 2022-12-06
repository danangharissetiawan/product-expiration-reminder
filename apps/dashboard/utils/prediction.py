from datetime import datetime
from pathlib import Path

# import pandas as pd
import numpy as np
import os
import tensorflow as tf

from PIL import Image
from django.conf import settings


def predict(image_path, model_path, label_path, image_size):
    # Read Label
    with open(label_path) as f:
        labels = [line.strip() for line in f.readlines()]

    labels = sorted(labels)

    # Load the model
    model = tf.keras.models.load_model(model_path)

    # Read the image
    img = Image.open(image_path)

    # Preprocess the image and prepare it for classification
    img = img.resize((image_size, image_size))
    img_array = np.array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Classify the input image
    predictions = model.predict(img_array)

    pred = np.argmax(predictions, axis=1)

    # Map the label
    # labels = (train_dataset.class_indices)
    # labels = dict((v,k) for k,v in labels.items())
    pred = [labels[k] for k in pred]
    return pred


def predict_fruit(image_path):
    # Read Label
    label_path = settings.LABEL_FRUIT_PATH
    model_path = settings.MODEL_FRUIT_PATH
    image_size = 256

    pred = predict(image_path, model_path, label_path, image_size)
    name, quality = pred[0].split("_")
    if quality == "Good":
        q_value = "g"
    elif quality == "Bad":
        q_value = "b"
    else:
        q_value = "m"
    return name, q_value


def predict_date_expired(image_path):
    # Read Label
    label_path = settings.LABEL_DATE_PATH
    model_path = settings.MODEL_DATE_PATH
    image_size = 160

    pred = predict(image_path, model_path, label_path, image_size)
    base_format = ["%d-%m-%y", "%d-%m-%Y", "%Y-%m-%d"]
    for i in base_format:
        try:
            date = datetime.strptime(pred[0], i).date()
            return date
        except ValueError:
            pass
    return date

