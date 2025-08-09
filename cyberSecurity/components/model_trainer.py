import os, sys
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam

from cyberSecurity.loggers import logger
from cyberSecurity.exceptions import CSException
from cyberSecurity.entity import ModelTrainerConfig, ModelTrainerArtifact
from cyberSecurity.utils import save_bin

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_random_forest_model(self, X_train, y_train, X_test, y_test):
        try:
            rf_model = RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
            rf_model.fit(X_train, y_train)

            train_pred = rf_model.predict(X_train)
            test_pred = rf_model.predict(X_test)

            train_metrics = {
                "accuracy": accuracy_score(y_train, train_pred),
                "classification_report": classification_report(y_train, train_pred)
            }

            test_metrics = {
                "accuracy": accuracy_score(y_test, test_pred),
                "classification_report": classification_report(y_test, test_pred)
            }

            return rf_model, train_metrics, test_metrics
        except Exception as e:
            raise CSException(e, sys)
    
    def train_neural_network_model(self, X_train, y_train, X_test, y_test):
        try:
            model = Sequential([
                Input(shape=(X_train.shape[1],)),
                Dense(128, activation='relu'),
                Dropout(0.3),
                Dense(64, activation='relu'),
                Dropout(0.3),
                Dense(32, activation='relu'),
                Dense(1, activation='sigmoid')
            ])

            model.compile(
                optimizer = Adam(learning_rate=0.001),
                loss='binary_crossentropy',
                metrics=['accuracy']
            )

            history = model.fit(
                X_train, y_train,
                epochs=50,
                batch_size = 32,
                validation_split =0.2,
                verbose =0
            )

            train_loss, train_accuracy = model.evaluate(X_train, y_train, verbose=0)
            test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

            train_metrics = {
                "accuracy": train_accuracy,
                "loss": train_loss
            }

            test_metrics = {
                "accuracy": test_accuracy,
                "loss": test_loss
            }

            return model, train_metrics, test_metrics
        except Exception as e:
            raise CSException(e, sys)
    
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logger.info("Model Training Started")

            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            X_train = train_data.iloc[:, :-1].values
            y_train = train_data.iloc[:, -1].values
            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values

            logger.info("Training Random Forest Model")
            rf_model, rf_train_metrics, rf_test_metrcis = self.train_random_forest_model(
                X_train, y_train, X_test, y_test
            )

            logger.info("Training Neural Network Model")
            nn_model, nn_train_metrics, nn_test_metric = self.train_neural_network_model(
                X_train, y_train, X_test, y_test
            )

            # Choose Best Model Based on Test Accuracy
            if rf_test_metrcis['accuracy'] > nn_test_metric['accuracy']:
                best_model = rf_model
                best_train_metrics = rf_train_metrics
                best_test_metrics = rf_test_metrcis
                logger.info("Random Forest Selected as best Model")
            else:
                best_model = nn_model
                best_train_metrics = nn_train_metrics
                best_test_metrics = nn_test_metric
                logger.info("Neural Network Selected as Best Model")
            
            # Save the Best Model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            save_bin(data=best_model, path=model_path)

            logger.info("Model Training Completed")

            return ModelTrainerArtifact(
                trained_model_file_path=model_path,
                train_metric_artifact=best_train_metrics,
                test_metric_artifact=best_test_metrics
            )
        except Exception as e:
            raise CSException(e, sys)