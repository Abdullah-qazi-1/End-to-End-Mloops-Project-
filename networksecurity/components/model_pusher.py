import os
import sys
import shutil
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import ModelTrainerArtifact, ModelPusherArtifact
from networksecurity.entity.config_entity import ModelPusherConfig

class ModelPusher:
    def __init__(self, model_trainer_artifact: ModelTrainerArtifact,
                 model_pusher_config: ModelPusherConfig):
        try:
            self.model_trainer_artifact = model_trainer_artifact
            self.model_pusher_config = model_pusher_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            trained_model_path = self.model_trainer_artifact.trained_model_file_path
            
            # final model dir mein copy karo
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=model_file_path)

            # saved models dir mein bhi copy karo
            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            model_pusher_artifact = ModelPusherArtifact(
                saved_model_path=saved_model_path,
                model_file_path=model_file_path
            )
            logging.info(f"Model pusher artifact: {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)