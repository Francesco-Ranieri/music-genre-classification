from sklearn.model_selection import KFold
from sklearn import metrics
import numpy as np


def evaluate_classifier(classifier,
                        n_folds,
                        x_train_split,
                        y_train_split,
                        x_validation_split=None,
                        y_validation_split=None,
                        fit=True):
    """
    Utilities to run evaluation of classifiers

    If n_folds is false, perform a validation with a single test/validation split, using the other parameters
    :param classifier: model used to classify
    :param n_folds: number of folds in cross validation
    :param x_train_split: X train set
    :param y_train_split: y train set
    :param x_validation_split: X test set
    :param y_validation_split: y test set
    :param fit: indicates if the model needs to be fit or not
    :return:
    """

    if n_folds:
        accuracy, precision, recall, f_macro, f_micro, classifier = _evaluate_classifier_with_folds(classifier,
                                                                                                    fit,
                                                                                                    x_train_split,
                                                                                                    y_train_split,
                                                                                                    n_folds)
    else:
        accuracy, precision, recall, f_macro, f_micro, classifier = _evaluate_classifier_with_split(classifier,
                                                                                                    fit,
                                                                                                    x_train_split,
                                                                                                    x_validation_split,
                                                                                                    y_train_split,
                                                                                                    y_validation_split)
    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1-micro: ", f_micro)
    print("F1-macro: ", f_macro)

    metrics_calc = {
                        "accuracy": accuracy,
                        "precision": precision,
                        "recall": recall,
                        "f_micro": f_micro,
                        "f_macro": f_macro
                    }

    return metrics_calc, classifier


def _evaluate_classifier_with_folds(classifier,
                                    fit,
                                    n_folds,
                                    X_train,
                                    y_train):
    accuracy, precision, recall, f_macro, f_micro = 0, 0, 0, 0, 0
    x_train_array = np.array(X_train)

    k_fold = KFold(n_splits=n_folds, random_state=0, shuffle=True)
    for idx, (train_index, validation_index) in enumerate(k_fold.split(x_train_array)):

        print(f"Fold #{idx}")
        print(f"Fitting the model...")

        if fit:
            classifier.fit(x_train_array[train_index], y_train[train_index])

        print(f"Model fitted. Predicting on validation set...")
        predicted = classifier.predict(x_train_array[validation_index])
        accuracy = accuracy + metrics.accuracy_score(y_train[validation_index], predicted)
        precision = precision + metrics.precision_score(y_train[validation_index], predicted, average='micro')
        recall = recall + metrics.recall_score(y_train[validation_index], predicted, average='micro')
        f_micro = f_micro + metrics.f1_score(y_train[validation_index], predicted, average='micro')
        f_macro = f_macro + metrics.f1_score(y_train[validation_index], predicted, average='macro')

    accuracy /= n_folds
    precision /= n_folds
    recall /= n_folds
    f_micro /= n_folds
    f_macro /= n_folds

    return accuracy, precision, recall, f_macro, f_micro, classifier


def _evaluate_classifier_with_split(classifier,
                                    fit,
                                    X_train_split,
                                    X_validation_split,
                                    y_train_split,
                                    y_validation_split):
    if fit:
        print(f"Fitting the model...")
        classifier.fit(X_train_split, y_train_split)

    print(f"Model fitted. Prediting on validation set...")
    predicted = classifier.predict(X_validation_split)

    accuracy = metrics.accuracy_score(y_validation_split, predicted)
    precision = metrics.precision_score(y_validation_split, predicted, average='macro')
    recall = metrics.recall_score(y_validation_split, predicted, average='macro')
    f_micro = metrics.f1_score(y_validation_split, predicted, average='micro')
    f_macro = metrics.f1_score(y_validation_split, predicted, average='macro')

    return accuracy, precision, recall, f_macro, f_micro, classifier
