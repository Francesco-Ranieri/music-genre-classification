from enum import Enum


class ModelAllowedGTZAN(Enum):
    """
        Enum representing model allowed for GTZAN dataset. \n
        Possible Value: \n
        - **Random Forest** \n
        - **Gaussian NB**
    """

    GAUSSIAN_NB = 'Gaussian NB'
    RANDOM_FOREST = 'Random Forest'


class ModelAllowedMFCC(Enum):
    """
        Enum representing model allowed for MFCC dataset. \n
        Possible Value: \n
        - **CNN**
    """

    CNN = 'CNN'
