from enum import Enum

from sklearn import naive_bayes, ensemble
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Flatten, Dense, Input, Conv2D, MaxPooling2D, BatchNormalization

from src.data.data_utils import Dataset


class ModelAllowed(Enum):
    GAUSSIAN_NB = 'Gaussian NB'
    RANDOM_FOREST = 'Random Forest'
    CNN = 'CNN'


def get_model_from_name(model_name: str, dataset_type: Dataset):
    """
    :param dataset_type: MFCC or GTZAN
    :param model_name: name of the model
    :return:
    """

    random_state = 0
    if dataset_type == Dataset.GTZAN:

        if model_name == ModelAllowed.GAUSSIAN_NB.value:
            model = naive_bayes.GaussianNB()
        elif model_name == ModelAllowed.RANDOM_FOREST.value:
            model = ensemble.RandomForestClassifier(random_state=random_state)

    elif dataset_type == Dataset.MFCC:

        if model_name == ModelAllowed.CNN.value:
            model = Sequential([
                Input(shape=((130, 13, 1,))),
                BatchNormalization(),
                Conv2D(8,
                       kernel_size=(3, 3),
                       activation='relu',
                       kernel_regularizer=regularizers.l2(l=0.01),
                       kernel_initializer='he_normal'),
                MaxPooling2D((2, 2),
                             strides=(2, 2),
                             padding='same'),
                Conv2D(32,
                       kernel_size=(3, 3),
                       activation='relu',
                       kernel_regularizer=regularizers.l2(l=0.01),
                       kernel_initializer='he_normal'),
                MaxPooling2D((2, 2),
                             strides=(2, 2),
                             padding='same'),
                Flatten(),
                Dense(128, activation='relu'),
                Dense(64, activation='relu'),
                Dense(10, activation='softmax')
            ])

            optimizer_cnn = keras.optimizers.Adam(learning_rate=0.0001)
            model.compile(optimizer=optimizer_cnn,
                          loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            model.summary()

    else:
        raise ValueError("Model name provided is not allowed")

    return model
