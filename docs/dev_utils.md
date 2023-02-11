# DEV UTILS
Hi dev, here some utils for this project

## SETUP

Virtual env creation:

```
conda create --name myenv --file spec-file.txt
conda activate myenv
```
or
```
py -m venv <env>
.\<env>\Scripts\activate
```

Install requirements.txt:
```
pip install -f requirements.txt
```

Install src module:
```
pip install -e .
```

Run dvc pipeline:
* Download dataset
* Train model
* Test model

```
dvc repro
```
If you not configure .env file, all the experiments and models will be saved on your local machine.
To avoid this beahaviour follow this steps:

1. create .env file in the root directory
     ```
     touch .env
     ```
2. insert in the .env file the following variables:
    * MLFLOW_TRACKING_URI = ...
    * MLFLOW_TRACKING_USERNAME = ...
    * MLFLOW_TRACKING_PASSWORD = ...
    * API_URL = http://host.docker.internal:8000/predict/music

## RUN

To execute all project, just run:
```
docker compose up
```
To build and run the project, use:
```
docker compose run --build
```

To build and run single images:

```
BE
docker build -f Dockerfile-be . -t music_genre_classification_api 
docker run -p 8000:8000 music_genre_classification_api

FE
docker build -f Dockerfile-fe . -t music_genre_classification_app
docker run -p 7860:7860 music_genre_classification_app
```

## FORMAT CODE

To format py code:
```
cd <folder>
autopep8 --in-place --recursive .
```

## CREATE DISTRO FEAT_EXTRACTOR
If you want to create a distro on Pypi, just simply add a tag on github and, the github action just do it for you !.
If you want to create a distro from your local machine and push it to pypi, use this commands:

```
cd src
python setup.py sdist
twine upload dist/*
```
