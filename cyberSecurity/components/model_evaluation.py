import sys
import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.entity import ModelEvaluationConfig, ModelEvaluationArtifact
from cyberSecurity.utils import load_bin, save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        try:
            actual = np.array(actual).astype(int)
            pred = np.array(pred).astype(int)

            logger.info(f"Evaluating - Actual: {actual.shape}, Pred: {pred.shape}")
            logger.info(f"Unique actual: {np.unique(actual)}, Unique pred: {np.unique(pred)}")
            
            accuracy = accuracy_score(actual, pred)
            precision = precision_score(actual, pred, average='weighted', zero_division=0)
            recall = recall_score(actual, pred, average='weighted', zero_division=0)
            f1 = f1_score(actual, pred, average='weighted', zero_division=0)

            # Enhanced ROC-AUC Handling
            try:
                unique_classes = np.unique(actual)
                if len(unique_classes) == 2:
                    roc_auc = roc_auc_score(actual, pred)
                elif len(unique_classes) > 2:
                    roc_auc = roc_auc_score(actual, pred, multi_class='ovr', average='weighted')
                else:
                    roc_auc = 0.0
            except Exception as roc_error:
                logger.warning(f"ROC-AUC calculation failed: {roc_error}")
                roc_auc = 0.0
            
            return accuracy, precision, recall, f1, roc_auc
        except Exception as e:
            raise CSException(e, sys)
        
    
    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            logger.info(f"Model Evaluation Started")

            test_data = pd.read_csv(self.config.test_data_path)
            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values
            
            logger.info(f"Test data shape: {X_test.shape}")
            logger.info(f"Test labels shape: {y_test.shape}")
            logger.info(f"Unique labels: {np.unique(y_test)}")
            
            model = load_bin(Path(self.config.model_path))
            logger.info(f"Model loaded: {type(model).__name__}")
            
            predictions = model.predict(X_test)
            logger.info(f"Predictions shape: {predictions.shape}")
            logger.info(f"Prediction data type: {predictions.dtype}")
            logger.info(f"Unique predictions: {np.unique(predictions)}")
            
            accuracy, precision, recall, f1, roc_auc = self.eval_metrics(y_test, predictions)
            
            # Create evaluation report
            evaluation_report = {
                "accuracy": float(accuracy),
                "precision": float(precision),
                "recall": float(recall),
                "f1_score": float(f1),
                "roc_auc_score": float(roc_auc),
                "model_type": type(model).__name__
            }

            save_json(path=Path(self.config.metric_file_name), data = evaluation_report)

            logger.info(f"Model evaluation completed with accuracy: {accuracy}")
            logger.info(f"Evaluation report: {evaluation_report}")

            return ModelEvaluationArtifact(
                evaluation_report=evaluation_report,
                model_accuracy=accuracy
            )
        except Exception as e:
            raise CSException(e, sys)