# Project Configuration File

## Data Configuration
DATASET_PATH = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

## Model Configuration
RANDOM_STATE = 42
TEST_SIZE = 0.30
VALIDATION_SPLIT = 0.10

## Preprocessing Configuration
MIN_MAX_SCALING = True
SMOTE_ENABLED = True
SMOTE_RANDOM_STATE = 42

## Feature Selection
FEATURE_SELECTION_METHOD = "mutual_information"
TOP_N_FEATURES = 10

## Logistic Regression Configuration
LR_SOLVER = "liblinear"
LR_MAX_ITER = 1000
LR_HYPERPARAMETERS = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2']
}
LR_CV_FOLDS = 5
LR_SCORING = "roc_auc"

## Deep Neural Network Configuration
DNN_ARCHITECTURE = {
    'input_layer': 'auto',
    'hidden_layers': [64, 32],
    'activation': 'relu',
    'output_activation': 'sigmoid',
    'optimizer': 'adam',
    'loss': 'binary_crossentropy',
    'metrics': ['AUC']
}

DNN_TRAINING = {
    'epochs': 100,
    'batch_size': 64,
    'validation_split': 0.10,
    'early_stopping': {
        'monitor': 'val_loss',
        'patience': 5,
        'restore_best_weights': True
    }
}

## Evaluation Metrics
EVALUATION_METRICS = [
    'accuracy',
    'precision',
    'recall',
    'f1_score',
    'roc_auc'
]
