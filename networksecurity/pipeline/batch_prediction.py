import os
import sys
import numpy as np
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel


class BatchPrediction:
    def __init__(self, input_file_path: str):
        try:
            self.input_file_path = input_file_path
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_batch_prediction(self):
        try:
            # Data load karo
            dataframe = pd.read_csv(self.input_file_path)
            logging.info(f"Loaded data from {self.input_file_path}")

            # Model aur preprocessor load karo
            preprocessor = load_object("final_model/preprocessor.pkl")
            model = load_object("final_model/model.pkl")

            network_model = NetworkModel(
                preprocessor=preprocessor,
                model=model
            )

            # Prediction karo
            y_pred = network_model.predict(dataframe)
            dataframe['predicted_column'] = y_pred
            dataframe['predicted_column'].replace(0, -1, inplace=True)

            # Output save karo
            os.makedirs("prediction_output", exist_ok=True)
            output_path = os.path.join("prediction_output", "output.csv")
            dataframe.to_csv(output_path, index=False)
            logging.info(f"Predictions saved to {output_path}")

            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys)