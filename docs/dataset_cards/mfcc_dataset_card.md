# Dataset Card for MFCC

### Dataset Description

* **Dataset analysis**: [paper](../paper/paper.pdf)
* **Point of Contact**: Francesco Ranieri (ranierifra99@hotmail.it, f.ranieri27@studenti.uniba.it)

### Dataset Summary
This dataset is a sub-dataset of the original songs of [GTZAN dataset](./mfcc_dataset_card.md).

It contains the processing result of all the GTZAN music tracks in order to extract MFCC features in a differnt way.

###  Supported Tasks and Leaderboards
The tasks supported by this dataset are:

* Music Genre Classification

### Languages
It is a non readable human dataset and it is a collection of numpy-array object.

## Dataset Structure

### Data Instances
This dataset is the result of the MFCC feature extraction of the 3 second GTZAN dataset.
The idea behind the creation of the MFCC Dataset is to isolate GTZAN time serializable data in order to train models that fit better this task like
Recurrent Neural Network.

### Data Fields
The dataset is represented by a list of numpy array file. <br>
Each array has this dimension: (None, 130, 13, 1) and it is create by using librosa python package.
The following snippet is the core of the MFCC dataset features extraction:

```
...

# extract mfcc
mfcc = librosa.feature.mfcc(y=signal[start:finish],
                            sr=sample_rate,
                            n_mfcc=num_mfcc,
                            n_fft=n_fft,
                            hop_length=hop_length)

...

```

It is possibile to find the entire creation [here](../../src/data/make_dataset.py).

## Additional Information
### Dataset Curators
The curator of the original dataset is Francesco Ranieri (ranierifra99@hotmail.it, f.ranieri27@studenti.uniba.it).
