from enum import Enum


class Operations(Enum):
    # Data -> Data Linkages
    VIEW = "Shallow Copy / Casting"
    COPY = "Copy"
    ROW_FILTER = "Row Filtering"
    COLUMN_SELECT = "Column Selection"
    INDEXER = "Indexer"
    TRANSFORM = "Transformation"
    PIPELINE_TRANSFORM = "Pipeline Transform"
    CONCATENATION = "Concatenation"

    # Data -> Data and Data -> Metric Linkages
    TEST_INPUT = "Test Data"

    # Data -> Model, Data -> Metric Linkages
    TRAINING_DATA = "Training Data"
    TRAINING_LABELS = "Training Labels"
    VALIDATION_DATA = "Validation Data"
    VALIDATION_LABELS = "Validation Labels"

    # Data -> Metric Linkages
    TEST_LABELS = "Test Labels"
    TEST_PREDICTIONS = "Test Predictions"
    DATA_STATS = "Data Stats"
    DATA_PLOT = "Data Plot"

    # Model -> Data
    PREDICTION = "Model Prediction"

    # Model -> Metric Linkages
    EVALUATION = "Model Evaluation"

    # Model -> Model Linkages
    TRANSFER_LEARN = "Transfer Learning"
    ENSEMBLE = "Model Ensembling"
