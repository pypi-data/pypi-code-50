import argparse
import pexpect
import os
import sys
import json
import seaborn as sns
import sklearn.preprocessing as sp
import sklearn.linear_model as slm
import sklearn.ensemble as se
import sklearn.tree as st
import sklearn.model_selection as sms
import sklearn.metrics as sm
import pandas as pd
import numpy as np
import modAL.models as mm
import joblib
import random

from alanbootstrap.components import ast as ast_module

SEED = 30
SHARED_AST_TARGET = 'target'
SHARED_AST_FEATURES = 'complexity_features'
SHARED_AST_SQL = 'SQL'
SHARED_AST_CU = "CU_Q"
SHARED_AST_CU_MUL = "multi-line_CU_Q"


def create_parser():
    parser = argparse.ArgumentParser(description='Parameters for AST classification active learner. '
                                                 'The model will be persisted into the output folder at every iteration. '
                                                 'If a dev dataset was provided, the classification accuracy score would '
                                                 'be calculated on this dataset at each iteration and a performance '
                                                 'plot would be saved into the output folder.'
                                     )
    parser.add_argument('-i', '--init', required=True,
                        help='Shared-AST json file path; '
                             'ASTs in this file will be used to initialize the active learner. '
                             'Every AST in this file must contain a target value and a list of complexity_features.'
                        )
    parser.add_argument('-p', '--pool', required=True,
                        help='Shared-AST json file path; '
                             'Active learner will sample ASTs from this file '
                             'Every AST in this file must contain a list of complexity_features.'
                        )
    parser.add_argument('-o', '--output', required=True,
                        help="Absolute path of the model persisting folder."
                        )
    parser.add_argument('-d', '--devset', required=False,
                        help='Shared-AST json file path; '
                             'ASTs in this file will be used to evaluate the active learner. '
                             'Every AST in this file must contain a target value and a list of complexity_features.'
                        )
    args = parser.parse_args()

    return args


def vectorize_ast(ast_list, feature_names=None):
    X_y = list(map(
        lambda ast: (ast.data[SHARED_AST_FEATURES], ast.data[SHARED_AST_TARGET])
        if SHARED_AST_TARGET in ast.data else ast.data[SHARED_AST_FEATURES],
        ast_list
    ))

    if isinstance(X_y[0], tuple):
        X, y = list(zip(*X_y))
    else:
        X = X_y
        y = None

    # list of feature names sorted alphabeltically
    if feature_names is None:
        feature_names = sorted(list(X[0].keys()))

    # dict --> list
    def dict_to_list(x_):
        return [x_[name] for name in feature_names]

    X = [dict_to_list(x) for x in X]

    return X, y, feature_names


def persist_model(active_learner: mm.ActiveLearner, model_output_folder: str):
    model_path = os.path.join(
        model_output_folder, "ast_bin_classifier.joblib"
    )

    joblib.dump(active_learner.estimator, model_path)


def evaluate_model(active_learner: mm.ActiveLearner, X_dev, y_dev):
    y_pred = active_learner.estimator.predict(X_dev)

    # evaluation
    accuracy = sm.accuracy_score(y_dev, y_pred)
    return accuracy


def active_learn(args):
    init_train_path = os.path.abspath(args.init)
    pool_path = os.path.abspath(args.pool)
    if 'devset' in args:
        dev_path = os.path.abspath(args.devset)
    output_path = os.path.abspath(args.output)

    np.random.seed(SEED)
    random.seed = SEED

    print("\nLoading Data...")
    # load training data that are used to initialize the active learner
    json_path = init_train_path
    init_train_data = ast_module.AST.from_shared_ast_json_file(
        json_path, data_keys=[SHARED_AST_TARGET, SHARED_AST_FEATURES]
    )
    random.shuffle(init_train_data)

    # load ast data pool
    json_path = pool_path
    pool_data = ast_module.AST.from_shared_ast_json_file(
        json_path, data_keys=[SHARED_AST_FEATURES, SHARED_AST_SQL, SHARED_AST_CU, SHARED_AST_CU_MUL]
    )
    random.shuffle(pool_data)

    if 'devset' in args:
        # load testing data that are used to evaluate the active learner
        json_path = dev_path
        dev_data = ast_module.AST.from_shared_ast_json_file(
            json_path, data_keys=[SHARED_AST_TARGET, SHARED_AST_FEATURES]
        )

    print("\nPreprocessing...")
    # vectorize training data
    X_train, y_train, feature_names = vectorize_ast(init_train_data)
    print("List of features: ")
    print("\t" + str(feature_names))

    # vectorize AST pool
    X_pool, _, _ = vectorize_ast(pool_data, feature_names=feature_names)

    # normalize pool data features, assume data pool is large enough to cover the input space
    normalizer = sp.RobustScaler()
    normalizer.fit(X_pool)
    print('Before normalization: ' + str(X_pool[0]))
    X_pool = normalizer.transform(X_pool)
    print('After normalization: ' + str(X_pool[0]))

    # normalize training data features
    X_train = normalizer.transform(X_train)

    # vectorize and normalize dev data
    if dev_data is not None:
        X_dev, y_dev, _ = vectorize_ast(dev_data, feature_names=feature_names)
        X_dev = normalizer.transform(X_dev)

    model = se.RandomForestClassifier(n_estimators=50, random_state=SEED)
    accuracy_scores = list()

    # initialize the training
    print("\nModel Training Start...")
    learner = mm.ActiveLearner(estimator=model, X_training=X_train,
                               y_training=np.array(y_train).astype('int'))
    persist_model(learner, output_path)
    if dev_data is not None:
        accuracy = evaluate_model(learner, X_dev, y_dev)
        print("Model Accuracy Before Active Learning: %.3f" % accuracy)
        accuracy_scores.append(accuracy)

    # start active learning
    iterations = 0
    while True:
        # find next training sample
        query_idx, query_sample = learner.query(X_pool)
        query_idx = int(query_idx[0])
        print("\n" + ''.join(['+'] * 100))
        print(''.join(['+'] * 100))
        print("\n%d Iteration Starts: " % iterations)
        print('~~~~~ Shared-AST ~~~~~')
        pool_data[query_idx].pretty_print()

        if SHARED_AST_SQL in pool_data[query_idx].data:
            print('~~~~~ SQL ~~~~~')
            print(pool_data[query_idx].data[SHARED_AST_SQL])

        if SHARED_AST_CU in pool_data[query_idx].data:
            print('~~~~~ Cannonical question (long form) ~~~~~')
            print(pool_data[query_idx].data[SHARED_AST_CU])

        if SHARED_AST_CU_MUL in pool_data[query_idx].data:
            print('~~~~~ Cannonical question (multi line) ~~~~~')
            print(pool_data[query_idx].data[SHARED_AST_CU_MUL])

        print('~~~~~ Metadata ~~~~~')
        print('Complexity: ' + str(pool_data[query_idx].complexity))

        print('~~~~~ Please EVALUATE The AST, and type 1 or 0 ~~~~~')
        print('~~~~~ 1 --> Pick Up, 0 --> Throw Away, q --> Quit Learning~~~~~')
        user_input = str(input('>>'))
        while user_input not in {'1', '0', 'q'}:
            print('UNKNOWN USER INPUT!')
            print('~~~~~ Please EVALUATE The AST, and type 1 or 0 ~~~~~')
            print('~~~~~ 1 --> Pick Up, 0 --> Throw Away~~~~~, q --> Quit Learning')
            user_input = str(input('>>'))
            if user_input == 'q':
                break

        if user_input == 'q':
            if len(accuracy_scores) > 1:
                sns_plot = sns.lineplot(
                    y='batch_accuracy', x='iter',
                    data=pd.DataFrame({'batch_accuracy': accuracy_scores, 'iter': list(range(len(accuracy_scores)))})
                )
                fig_path = os.path.join(output_path, "ast_bin_classifier_al_accuracy.png")
                sns_plot.get_figure().savefig(fig_path)
            break

        y_ = int(user_input)
        learner.teach(
            X=X_pool[query_idx:query_idx + 1],
            y=np.array([y_]).astype('int')
        )

        # Remove the queried instance from the unlabeled pool.
        X_pool = np.delete(X_pool, query_idx, axis=0)
        pool_data.pop(query_idx)

        persist_model(learner, output_path)
        if dev_data is not None:
            accuracy = evaluate_model(learner, X_dev, y_dev)
            print("Model Accuracy at %d Iteration: %.3f" % (iterations, accuracy))
            accuracy_scores.append(accuracy)

        print("%d Iteration Completed!" % iterations)
        iterations += 1


if __name__ == '__main__':

    args = create_parser()
    active_learn(args)
