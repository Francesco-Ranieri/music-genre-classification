# Model Card for RANDOM FOREST

<!-- Provide a quick summary of what the model is/does. -->

The model is a Random Forest trained on the [GTZAN dataset]((../dataset_cards/gtzan_dataset_card.md)).
It predicts the music genre based on 58 music features.

## Model Details

- **Developed by:** Francesco Ranieri (ranierifra99@hotmail.it, f.ranieri27@studenti.uniba.it)
- **Library:** scikit-learn
- **Model type:** Random Forest
- **Model date:** 2023
- **License:**  [MIT License](../../LICENSE)
- **Paper:**  [Music Genre Classifiction Paper](../paper/paper.pdf)


## Use cases

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This model could be used as music genre classifier.

## Out of Scope cases

This model is not intended to be used for Music Name Recognizer.

# Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

This dataset used to train this model is composed of 10000 songs divided in 10 different genres:
* blues
* classical
* country
* hip hop
* pop
* reggae
* rock
* metal
* disco
* jazz

The limitation of this model is that it can predict only one of this classes and the music should be 
the cleanest audio possible. Adding augmented data to the dataset could alleviate this model disadvantage.

# Training Details

## Training Data

This model has been trained on the [GTAN Dataset](../dataset_cards/gtzan_dataset_card.md).
The dataset was split randomly in:
* training data (67%)
    * actual training data (67%) &nbsp;&nbsp;&nbsp;&nbsp; : for parameters fine-tuning
    * validation data (33%) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : for testing parameters fine-tuning
* test data (33%)


## Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

### Parameter 

| Name                        | Value |
| --------------------------- | ----- |
| batch_size                  | 32    |
| class_weight                | None  |
| epochs                      | 50    |
| initial_epoch               | 0     |
| max_queue_size              | 10    |
| opt_amsgrad                 | False |
| opt_beta_1                  | 0.9   |
| opt_beta_2                  | 0.999 |
| opt_clipnorm                | None  |
| opt_clipvalue               | None  |
| opt_ema_momentum            | 0.99  |
| opt_ema_overwrite_frequency | None  |
| opt_epsilon                 | 1e-07 |
| opt_global_clipnorm         | None  |
| opt_is_legacy_optimizer     | False |
| opt_jit_compile             | False |
| opt_learning_rate           | 1e-04 |
| opt_name                    | Adam  |
| opt_use_ema                 | False |
| opt_weight_decay            | None  |
| sample_weight               | None  |
| shuffle                     | True  |
| steps_per_epoch             | None  |
| use_multiprocessing         | False |
| validation_batch_size       | None  |
| validation_freq             | 1     |
| validation_split            | 0.0   |
| validation_steps            | None  |
| workers                     | 1     |

### Speeds, Sizes, Times
The training time is very fast because it fits in the range of 3 to 5 minutes.
# Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

## Testing Data, Factors & Metrics

### Testing Data

<!-- This should link to a Data Card if possible. -->

Testing data was composed of a random 33% split of the dataset.

### Metrics and Results

| Name                                                                                                                                                                                                                                                                                                                                                                        | Value |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| [accuracy](https://dagshub.com/Francesco-Ranieri/music-genre-classification.mlflow/#/metric/accuracy?runs=[%22672b41634a5546e39d1f3044cd3c9d3d%22]&experiments=[%220%22]&plot_metric_keys=[%22accuracy%22]&plot_layout={%22autosize%22:true,%22xaxis%22:{},%22yaxis%22:{}}&x_axis=relative&y_axis_scale=linear&line_smoothness=1&show_point=false&deselected_curves=[]&last_linear_y_axis_range=[])             | 0.913 |
| [loss](https://dagshub.com/Francesco-Ranieri/music-genre-classification.mlflow/#/metric/loss?runs=[%22672b41634a5546e39d1f3044cd3c9d3d%22]&experiments=[%220%22]&plot_metric_keys=[%22loss%22]&plot_layout={%22autosize%22:true,%22xaxis%22:{},%22yaxis%22:{}}&x_axis=relative&y_axis_scale=linear&line_smoothness=1&show_point=false&deselected_curves=[]&last_linear_y_axis_range=[])                         | 0.783 |
| [val_accuracy](https://dagshub.com/Francesco-Ranieri/music-genre-classification.mlflow/#/metric/val_accuracy?runs=[%22672b41634a5546e39d1f3044cd3c9d3d%22]&experiments=[%220%22]&plot_metric_keys=[%22val_accuracy%22]&plot_layout={%22autosize%22:true,%22xaxis%22:{},%22yaxis%22:{}}&x_axis=relative&y_axis_scale=linear&line_smoothness=1&show_point=false&deselected_curves=[]&last_linear_y_axis_range=[]) | 0.626 |
| [val_loss](https://dagshub.com/Francesco-Ranieri/music-genre-classification.mlflow/#/metric/val_loss?runs=[%22672b41634a5546e39d1f3044cd3c9d3d%22]&experiments=[%220%22]&plot_metric_keys=[%22val_loss%22]&plot_layout={%22autosize%22:true,%22xaxis%22:{},%22yaxis%22:{}}&x_axis=relative&y_axis_scale=linear&line_smoothness=1&show_point=false&deselected_curves=[]&last_linear_y_axis_range=[])             | 1.576 |

### Metrics comparison
<img src="assets/metrics_RF.png">

### Confusion Matrix
<img src="assets/confusion_matrix_RF.png">

Dataset Model Card Reference: 
* https://www.kaggle.com/code/var0101/model-cards
* https://github.com/openai/gpt-3/blob/master/model-card.md