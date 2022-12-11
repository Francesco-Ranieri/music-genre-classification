ml-boilerplate
==============================

boilerplate for machine learning projects

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

---
# Example metadata to be added to a model card.  
# Full model card template at https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md
language:
- {lang_0}  # Example: fr
- {lang_1}  # Example: en
license: {license}  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: {library_name}  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
tags:
- {tag_0}  # Example: audio
- {tag_1}  # Example: automatic-speech-recognition
- {tag_2}  # Example: speech
- {tag_3}  # Example to specify a library: allennlp
datasets:
- {dataset_0}  # Example: common_voice. Use dataset id from https://hf.co/datasets
metrics:
- {metric_0}  # Example: wer. Use metric id from https://hf.co/metrics

# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: {model_id}
  results:
  - task:
      type: {task_type}             # Required. Example: automatic-speech-recognition
      name: {task_name}             # Optional. Example: Speech Recognition
    dataset:
      type: {dataset_type}          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: {dataset_name}          # Required. A pretty name for the dataset. Example: Common Voice (French)
      config: {dataset_config}      # Optional. The name of the dataset configuration used in `load_dataset()`. Example: fr in `load_dataset("common_voice", "fr")`. See the `datasets` docs for more info: https://huggingface.co/docs/datasets/package_reference/loading_methods#datasets.load_dataset.name
      split: {dataset_split}        # Optional. Example: test
      revision: {dataset_revision}  # Optional. Example: 5503434ddd753f426f4b38109466949a1217c2bb
      args:
        {arg_0}: {value_0}          # Optional. Additional arguments to `load_dataset()`. Example for wikipedia: language: en
        {arg_1}: {value_1}          # Optional. Example for wikipedia: date: 20220301
    metrics:
      - type: {metric_type}         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: {metric_value}       # Required. Example: 20.90
        name: {metric_name}         # Optional. Example: Test WER
        config: {metric_config}     # Optional. The name of the metric configuration used in `load_metric()`. Example: bleurt-large-512 in `load_metric("bleurt", "bleurt-large-512")`. See the `datasets` docs for more info: https://huggingface.co/docs/datasets/v2.1.0/en/loading#load-configurations
        args:
          {arg_0}: {value_0}        # Optional. The arguments passed during `Metric.compute()`. Example for `bleu`: max_order: 4
        verified: true              # Optional. If true, indicates that evaluation was generated by Hugging Face (vs. self-reported).
---

This markdown file contains the spec for the modelcard metadata regarding evaluation parameters. When present, and only then, 'model-index', 'datasets' and 'license' contents will be verified when git pushing changes to your README.md file.
Valid license identifiers can be found in [our docs](https://huggingface.co/docs/hub/repositories-licenses).

For the full model card template, see: [https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md).