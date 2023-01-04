# Utilities to run evaluation of classifiers


from sklearn.model_selection import KFold, train_test_split
from sklearn import metrics


# We can perform both KFold validation and hold-out validation, but because of computational cost only the latter is
# used.
def evaluate_classifier(classifier,
                        n_folds,
                        X_train_split,
                        y_train_split,
                        X_validation_split=None,
                        y_validation_split=None,
                        fit=True):
    """
    Utilities to run evaluation of classifiers
    The splits are not performed in these methods because validation sets need to be stored in order to have a reliable evaluation of
    models that are stored and then reloaded.

    If n_folds is falsy, perform a validation with a single test/validation split, using the other parameters

    """

    if n_folds:
        accuracy, precision, recall, fmacro, fmicro = _evaluate_classifier_with_folds(classifier, fit, n_folds)
    else:
        accuracy, precision, recall, fmacro, fmicro = _evaluate_classifier_with_split(classifier, fit, X_train_split,
                                                                                      X_validation_split, y_train_split,
                                                                                      y_validation_split)

    print("Accuracy: ", accuracy)
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1-micro: ", fmicro)
    print("F1-macro: ", fmacro)

    return accuracy, precision, recall, fmacro, fmicro


def _evaluate_classifier_with_folds(classifier, fit, n_folds):
    accuracy, precision, recall, fmacro, fmicro = 0, 0, 0, 0, 0
    X_train_array = np.array(X_train)

    k_fold = KFold(n_splits=n_folds, random_state=0, shuffle=True)
    for idx, (train_index, validation_index) in enumerate(k_fold.split(X_train_array)):

        print(f"Fold #{idx}")
        print(f"Fitting the model...")

        if fit:
            classifier.fit(X_train_array[train_index], y_train[train_index])

        print(f"Model fitted. Predicting on validation set...")
        predicted = classifier.predict(X_train_array[validation_index])
        accuracy = accuracy + metrics.accuracy_score(y_train[validation_index], predicted)
        precision = precision + metrics.precision_score(y_train[validation_index], predicted, average='micro')
        recall = recall + metrics.recall_score(y_train[validation_index], predicted, average='micro')
        fmicro = fmicro + metrics.f1_score(y_train[validation_index], predicted, average='micro')
        fmacro = fmacro + metrics.f1_score(y_train[validation_index], predicted, average='macro')

    accuracy /= n_folds
    precision /= n_folds
    recall /= n_folds
    fmicro /= n_folds
    fmacro /= n_folds

    return accuracy, precision, recall, fmacro, fmicro


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
    fmicro = metrics.f1_score(y_validation_split, predicted, average='micro')
    fmacro = metrics.f1_score(y_validation_split, predicted, average='macro')

    return accuracy, precision, recall, fmacro, fmicro
