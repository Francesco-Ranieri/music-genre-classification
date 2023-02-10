# Behavioural tests

This behavioural tests are concerned to test how model react to some input perturbation.<br>
Note: these tests have no assert because they are used to observe how a model behaves in the presence of songs disturbed by noises or musical shifs.

## NORMAL MUSIC TRACK TEST

* Genre: POP
* Predicted: POP
* Normal track:
* Status: PASSED
<img src="./assets/normal.png">

## NOISE TESTS

### NOISE 0.01

* Genre: POP
* Predicted: POP
* Normal track:
* Status: PASSED
<img src="./assets/noise001.png">

### NOISE 0.1

* Genre: POP
* Predicted: POP
* Normal track:
* Status: PASSED
<img src="./assets/noise01.png">

### NOISE 0.2

* Genre: POP
* Predicted: HIPHOP
* Normal track:
* Status: FAILED
<img src="./assets/noise02.png">

### NOISE 0.5

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/noise05.png">

### NOISE 1 - FULL NOISE

* Genre: POP
* Predicted: RANDOM LABEL
* Normal track:
* Status: FAILED
<img src="./assets/noise1.png">





## SHIFT TESTS

### SHIFT 0.1 BOTH

* Genre: POP
* Predicted: POP
* Normal track:
* Status: PASSED
<img src="./assets/shift01.png">

### SHIFT 0.2 LEFT

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/shift02.png">

### SHIFT 10 BOTH

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/shift10.png">

### SHIFT 3 BOTH

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/shift3.png">

### SHIFT 2 RIGTH

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/shift2.png">

### SHIFT 6 LEFT

* Genre: POP
* Predicted: COUNTRY
* Normal track:
* Status: FAILED
<img src="./assets/shift6.png">


## OBSERVATION
This model should be train with more augmented data in order to perform better on this tests.
It seems to be sensitive both to noise and even more to data shift.

