<details>
<summary>Code example</summary>

```
📦ml-boilerplate
 ┣ 📂.dvc
 ┣ 📂.github                                         
 ┃ ┗ 📂workflows                                 : project pipelines
 ┃ ┃ ┣ 📜aws_deploy_api.yml                      : backend app aws deploy 
 ┃ ┃ ┣ 📜aws_deploy_app.yml                      : frontend app aws deploy
 ┃ ┃ ┣ 📜linter.yml                              : code checks and tests
 ┃ ┃ ┗ 📜release_to_pypi.yml                     : pypi package release
 ┃ ┣ 📜.gitignore
 ┣ 📂data                                        : Hosted Dataset 
 ┃ ┣ 📂processed                                 : PROCESSED DATA - DVC hosted
 ┃ ┃                       
 ┃ ┃ ┣ 📂gtzan_data                              : 1° dataset
 ┃ ┃ ┃ ┣ 📜x_test.pkl                            : test dataset features
 ┃ ┃ ┃ ┣ 📜x_train.pkl                           : train dataset features
 ┃ ┃ ┃ ┣ 📜x_train_split.pkl                     : train subset dataset features
 ┃ ┃ ┃ ┣ 📜x_validation.pkl                      : test subset dataset features
 ┃ ┃ ┃ ┣ 📜y_test.pkl                            : test dataset labels
 ┃ ┃ ┃ ┣ 📜y_train.pkl                           : train dataset labels
 ┃ ┃ ┃ ┣ 📜y_train_split.pkl                     : train subset dataset labels
 ┃ ┃ ┃ ┗ 📜y_validation.pkl                      : test subset dataset labels
 ┃ ┃ ┃      
 ┃ ┃ ┗ 📂mfcc_data                               : 2° dataset                       
 ┃ ┃ ┃ ┣ 📜x_test.pkl                            : ...        
 ┃ ┃ ┃ ┣ 📜x_train.pkl                           : ...
 ┃ ┃ ┃ ┣ 📜x_train_split.pkl                     : ...
 ┃ ┃ ┃ ┣ 📜x_validation.pkl                      : ...
 ┃ ┃ ┃ ┣ 📜y_test.pkl                            : ...
 ┃ ┃ ┃ ┣ 📜y_train.pkl                           : ...
 ┃ ┃ ┃ ┣ 📜y_train_split.pkl                     : ...
 ┃ ┃ ┃ ┗ 📜y_validation.pkl                      : ...
 ┃ ┃                            
 ┃ ┗ 📂raw                                       - RAW DATA - Google Drive hosted                 
 ┃ ┃ ┗ 📂dataset                                 : 1000 songs, 10x genre
 ┃ ┃ ┃ ┣ 📂genres_original                       : Original .wav song
 ┃ ┃ ┃ ┃ ┣ 📂blues                               : 100 blues songs
 ┃ ┃ ┃ ┃ ┣ 📂classical                           : 100 classical songs
 ┃ ┃ ┃ ┃ ┣ 📂country                             : 100 contry songs
 ┃ ┃ ┃ ┃ ┣ 📂disco                               : ...
 ┃ ┃ ┃ ┃ ┣ 📂hiphop                              : ...
 ┃ ┃ ┃ ┃ ┣ 📂jazz                                : ...
 ┃ ┃ ┃ ┃ ┣ 📂metal                               : ...
 ┃ ┃ ┃ ┃ ┣ 📂pop                                 : ...
 ┃ ┃ ┃ ┃ ┣ 📂reggae                              : ...
 ┃ ┃ ┃ ┃ ┗ 📂rock                                : 100 rock songs
 ┃ ┃ ┃ ┗ 📜features_3_sec.csv                    : Song features
 ┣ 📂notebooks
 ┃ ┣ 📜audio_augmentation.ipynb                  : Song augmentation notebook
 ┃ ┗ 📜feat_extractor.ipynb                      : Song features extractor 
 ┣ 📂observability                               : Observability module
 ┃ ┣ 📂grafana                                   
 ┃ ┃ ┣ 📂dashboards                              
 ┃ ┃ ┃ ┗ 📜dashboards.json                       : Grafana dashboard implementation 
 ┃ ┃ ┣ 📜dashboards.yml                          : Grafana config
 ┃ ┃ ┣ 📜data_source.yml                         : Grafana data source 
 ┃ ┃ ┗ 📜grafana.ini                             
 ┃ ┣ 📂prometheus
 ┃ ┃ ┣ 📜alert.yml                               : Prometheus alerts 
 ┃ ┃ ┗ 📜prometheus.yml                          : Prometheus config
 ┃ ┗ 📂tempo 
 ┃ ┃ ┗ 📜tempo.yml                               : Tempo config
 ┣ 📂reports
 ┃ ┣ 📂figures                                   
 ┃ ┣ 📂history                                   : Pipeline track files
 ┃ ┃ ┣ 📜gtzan_history.json
 ┃ ┃ ┗ 📜mfcc_history.json
 ┃ ┗ 📂tests                                     : Test track files
 ┃ ┃ ┣ 📜deep_checks.json                        : ─┒
 ┃ ┃ ┣ 📜deep_gtzan_checks.html                  :  ┣──> Deep checks reports file
 ┃ ┃ ┗ 📜deep_mfcc_checks.html                   : ─┛
 ┣ 📂src                 
 ┃ ┣ 📂api                                       : App BE folder
 ┃ ┃ ┣ 📂entities                                : Api models
 ┃ ┃ ┃ ┣ 📜model_allowed_enum.py
 ┃ ┃ ┃ ┣ 📜predict_model_request.py
 ┃ ┃ ┣ 📜api_rest.py                             : Api controller
 ┃ ┃ ┣ 📜music_prediction.py                     : Api services
 ┃ ┃
 ┃ ┣ 📂app                                       : App FE folder
 ┃ ┃ ┣ 📜gradio_app.py                           : App main
 ┃ ┣ 📂data                                      : Data modeling
 ┃ ┃ ┣ 📜data_utils.py                       
 ┃ ┃ ┣ 📜make_dataset.py                         
 ┃ ┣ 📂feat_extractor                            : PyPi package used in APP
 ┃ ┃ ┣ 📜feat_extractor.py
 ┃ ┣ 📂models                                    
 ┃ ┃ ┣ 📂classes                                  
 ┃ ┃ ┃ ┣ 📜base_model.py                         : Common Model
 ┃ ┃ ┃ ┣ 📜gtzan_model.py                       
 ┃ ┃ ┃ ┣ 📜mfcc_model.py
 ┃ ┃ ┣ 📜evaluation.py                           : Model evaluation utils
 ┃ ┃ ┣ 📜model_utils.py                          : Model creation utils
 ┃ ┃ ┣ 📜predict_model.py                        : Pipeline script for testing
 ┃ ┃ ┣ 📜train_model.py                          : Pipeline script for training
 ┃ ┣ 📂visualization
 ┃ ┃ ┣ 📜visualize.py                            : Song feature visualization
 ┃ ┣ 📜pathUtils.py                              : Relative project paths
 ┃ ┣ 📜setup.py
 ┣ 📂tests
 ┃ ┣ 📂api_tests
 ┃ ┃ ┗ 📜test_api.py                             : Unit tests - API
 ┃ ┣ 📂dataset_tests 
 ┃ ┃ ┣ 📜test_dataset_integrity.py               : Integrity tests - DATASET     
 ┃ ┃ ┗ 📜test_dataset_util.py                    : Unit tests - DATASET
 ┃ ┣ 📂feat_extractor_tests
 ┃ ┃ ┗ 📜test_feat_extractor.py                  : Unit tests - PyPI package
 ┃ ┣ 📂models_tests
 ┃ ┃ ┣ 📜test_behavioral_model.py                : Behavioral Tests - MODEL
 ┃ ┃ ┗ 📜test_model.py                           : Unit tests - MODEL
 ┃ ┣ 📂path_utils_tests                          
 ┃ ┃ ┗ 📜test_path_utils.py                      : Unit tests - PATH UTILS
 ┃ ┣ 📂resources                             
 ┃ ┃ ┣ 📂augmented                           
 ┃ ┃ ┃ ┣ 📂noise                                            
 ┃ ┃ ┃ ┗ 📂shift_time
 ┃ ┃ ┗ 📜hip_hop_test.wav
 ┃ ┣ 📂test_utils
 ┃ ┃ ┣ 📜mock_dataset.py
 ┃ ┃ ┣ 📜utils.py
 ┣ 📜docker-compose.yml                          : docker compose for BE/FE/Observability
 ┣ 📜Dockerfile-be                               : BE docker file
 ┣ 📜Dockerfile-fe                               : FE docker file
 ┣ 📜dvc.yaml                                    : DVC pipeline file
 ┣ 📜params.yaml                                 : DVC pipeline params
 ┣ 📜requirements.txt
 ┣ 📜requirements_be.txt
 ┣ 📜requirements_fe.txt
 ┣ 📜setup.py                                    : Src folder installation
 ```

 </details>
 
 
