from cement.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig,   \
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from cement.util.util import read_yaml_file

from cement.logger import logging
import sys,os
from cement.constant import *
from cement.exception import CementException



class Configuartion:

    def __init__(self,
                
                config_file_path:str = CONFIG_FILE_PATH,
                
                current_time_stamp:str = CURRENT_TIME_STAMP
                
                ) -> None:
        
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            
            self.training_pipeline_config = self.get_training_pipeline_config()
            
            self.time_stamp = current_time_stamp
        
        except Exception as e:
            raise CementException(e,sys) from e



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        try:
            
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)
            
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            ## The url location 
            ### dataset_download_url='https://drive.google.com/uc?export=download&id=1W42yoxCeY3vnz34hKdFdWa3cLJh0pKgC'
            
            
            zip_download_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_ZIP_DOWNLOAD_DIR_KEY])
            ## The path
            ### zip_download_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\zip_data'
            
            
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            ## The path
            ### raw_data_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\raw_data

            
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            
            
            
            ingested_train_dir = os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ## The path
            ### ### ingested_train_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\ingested_data\\train'
            
            
            ingested_test_dir =os.path.join(ingested_data_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])
            ## The path
            ### ingested_test_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\ingested_data\\test'


            data_ingestion_config = DataIngestionConfig(
                                                        dataset_download_url = dataset_download_url, 
                                                        
                                                        zip_download_dir = zip_download_dir, 
                                                        
                                                        raw_data_dir = raw_data_dir,

                                                        ingested_train_dir = ingested_train_dir, 
                                                        
                                                        ingested_test_dir = ingested_test_dir)
            
            logging.info(f"Data Ingestion config: {data_ingestion_config}")

            
            return data_ingestion_config

            ## Returns the following paths and url location
            ## DataIngestionConfig(dataset_download_url='https://drive.google.com/uc?export=download&id=1W42yoxCeY3vnz34hKdFdWa3cLJh0pKgC', 
            ## zip_download_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\zip_data', 
            ## raw_data_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\raw_data',
            ## ingested_train_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\ingested_data\\train',
            ## ingested_test_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_ingestion\\2022-07-26-20-21-24\\ingested_data\\test')
            ## Note : THe Timestamp will always be current new timestamp folder.
        
        except Exception as e:
            raise CementException(e,sys) from e




    def get_data_validation_config(self) -> DataValidationConfig:
        
        
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            
            data_validation_artifact_dir = os.path.join(artifact_dir,DATA_VALIDATION_ARTIFACT_DIR_NAME,self.time_stamp)
            
            
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]


            schema_file_path = os.path.join(
                                            ROOT_DIR,
                                            
                                            data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY],
                                            
                                            data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
                                            )

            ## The path
            ### schema_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\config\\schema.yaml'

            
            report_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME_KEY])
            ## The path
            ## report_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_validation\\2022-07-27-22-34-09\\report.json'

            
            
            report_page_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])
            ## The path
            ## report_page_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_validation\\2022-07-27-22-34-09\\report.html'

            
            data_validation_config = DataValidationConfig(
                                                          schema_file_path=schema_file_path,
                                                          
                                                          report_file_path=report_file_path,
                                                          
                                                          report_page_file_path=report_page_file_path
                                                          )
            
            
            return data_validation_config
            ## It returns the following
            ## DataValidationConfig( schema_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\config\\schema.yaml', 
            #  report_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_validation\\2022-07-27-22-34-09\\report.json', 
            #  report_page_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_validation\\2022-07-27-22-34-09\\report.html')

        
        
        except Exception as e:
            raise CementException(e,sys) from e




    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        try:
            
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_transformation_artifact_dir=os.path.join(
                                                          artifact_dir,
                                                          
                                                          DATA_TRANSFORMATION_ARTIFACT_DIR,
                                                          
                                                          self.time_stamp
                                                          )

            
            data_transformation_config_info=self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            


            preprocessed_object_file_path = os.path.join(
                                                         data_transformation_artifact_dir,
                                                         
                                                         data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                                                         
                                                         data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY]
                                                        )

            ## The path
            ### preprocessed_object_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\preprocessed\\preprocessed.pkl'

            
            transformed_train_dir=os.path.join(
                                               data_transformation_artifact_dir,
                                               
                                               data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                                               
                                               data_transformation_config_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY]
                                               )

            ## The path 
            ### transformed_train_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\transformed_data\\train'


            transformed_test_dir = os.path.join(
                                                data_transformation_artifact_dir,
                                                
                                                data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                                                
                                                data_transformation_config_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY]
                                                )


            ## The path
            ### transformed_test_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\transformed_data\\test'
            

            data_transformation_config= DataTransformationConfig(
                                                                preprocessed_object_file_path = preprocessed_object_file_path,
                                                                
                                                                transformed_train_dir = transformed_train_dir,
                                                                
                                                                transformed_test_dir = transformed_test_dir
                                                                )

            
            logging.info(f"Data transformation config: {data_transformation_config}")
            
            
            
            return data_transformation_config
            ## This returns the following
            ## DataTransformationConfig(transformed_train_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\transformed_data\\train', 
            ## transformed_test_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\transformed_data\\test', 
            ## preprocessed_object_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\data_transformation\\2022-07-28-18-04-30\\preprocessed\\preprocessed.pkl')
        
        
        
        except Exception as e:
            raise CementException(e,sys) from e



    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        
        
        try:
            
            artifact_dir = self.training_pipeline_config.artifact_dir

            
            model_trainer_artifact_dir = os.path.join(artifact_dir,MODEL_TRAINER_ARTIFACT_DIR,self.time_stamp)
            
            
            
            model_trainer_config_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            
            
            
            trained_model_file_path = os.path.join(
                                                   model_trainer_artifact_dir,
                                                   
                                                   model_trainer_config_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
                                                   
                                                   model_trainer_config_info[MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY]
                                                   )

            ## The path
            ## trained_model_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\model_trainer\\2022-07-28-23-57-03\\trained_model\\model.pkl

            
            model_config_file_path = os.path.join(model_trainer_config_info[MODEL_TRAINER_MODEL_CONFIG_DIR_KEY],
                                                  model_trainer_config_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY]
                                                  )

            ## model_config_file_path='config\\model.yaml'

            base_accuracy = model_trainer_config_info[MODEL_TRAINER_BASE_ACCURACY_KEY]

            
            
            model_trainer_config = ModelTrainerConfig(
                                                      trained_model_file_path = trained_model_file_path,
                                                      
                                                      base_accuracy = base_accuracy,
                                                      
                                                      model_config_file_path = model_config_file_path
                                                      )
            
            logging.info(f"Model trainer config: {model_trainer_config}")
            
            
            return model_trainer_config
            ## This returns the following:
            ## ModelTrainerConfig(trained_model_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\model_trainer\\2022-07-28-23-57-03\\trained_model\\model.pkl', 
            # base_accuracy=0.6, model_config_file_path='config\\model.yaml')
        
        except Exception as e:
            raise CementException(e,sys) from e



    
    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        
        
        try:
            
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            
            artifact_dir = os.path.join(self.training_pipeline_config.artifact_dir,MODEL_EVALUATION_ARTIFACT_DIR, )

            model_evaluation_file_path = os.path.join(artifact_dir,model_evaluation_config[MODEL_EVALUATION_FILE_NAME_KEY])
            ## The path
            ## model_evaluation_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\model_evaluation\\model_evaluation.yaml'
            
            
            response = ModelEvaluationConfig(model_evaluation_file_path = model_evaluation_file_path,time_stamp = self.time_stamp)
            
            
            logging.info(f"Model Evaluation Config: {response}.")
            
            return response
            ## This returns the following
            ## ModelEvaluationConfig(model_evaluation_file_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact\\model_evaluation\\model_evaluation.yaml', 
            # time_stamp='2022-07-29-03-32-25')
        
        
        except Exception as e:
            raise CementException(e,sys) from e



    def get_model_pusher_config(self) -> ModelPusherConfig:
        
        
        try:
            
            
            time_stamp = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            model_pusher_config_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            
            export_dir_path = os.path.join(ROOT_DIR, model_pusher_config_info[MODEL_PUSHER_MODEL_EXPORT_DIR_KEY],time_stamp)
            ## The path
            ## export_dir_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\saved_models\\20220729033258'

            
            model_pusher_config = ModelPusherConfig(export_dir_path=export_dir_path)
            
            logging.info(f"Model pusher config {model_pusher_config}")
            
            return model_pusher_config
            ## Returns
            ## ModelPusherConfig(export_dir_path='c:\\Users\\sayan\\Cement-Strength-Prediction\\saved_models\\20220729033258')

        
        except Exception as e:
            raise CementException(e,sys) from e








    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        
        try:
            
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            
            artifact_dir = os.path.join(
                                    ROOT_DIR,
                                        
                                    training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        
                                    training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                    )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            
            return training_pipeline_config
            ## It return the path of the artifact folder
            ### TrainingPipelineConfig(artifact_dir='c:\\Users\\sayan\\Cement-Strength-Prediction\\cement\\artifact') 
        
        except Exception as e:
            raise CementException(e,sys) from e
