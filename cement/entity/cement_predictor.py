import os
import sys

from cement.exception import CementException
from cement.util.util import load_object

import pandas as pd


class CementData:

    def __init__(self,
                
                cement:float,
                 
                blast_furnace_slag:float,
                 
                fly_ash:float,
                 
                water:float,
                 
                superplasticizer:float,
                 
                coarse_aggregate:float,
                 
                fine_aggregate:float,
                 
                age:int,
                 
                concrete_compressive_strength: float = None
                 ):
        
        try:
            
            self.cement = cement
            
            self.blast_furnace_slag = blast_furnace_slag
            
            self.fly_ash = fly_ash
            
            self.water = water
            
            self.superplasticizer = superplasticizer
            
            self.coarse_aggregate = coarse_aggregate
            
            self.fine_aggregate = fine_aggregate
            
            self.age = age
            
            self.concrete_compressive_strength = concrete_compressive_strength
        
        
        except Exception as e:
            raise CementException(e, sys) from e

    def get_cement_input_data_frame(self):

        try:
            
            cement_input_dict = self.get_cement_data_as_dict()
            
            return pd.DataFrame(cement_input_dict)
        
        except Exception as e:
            raise CementException(e, sys) from e

    def get_cement_data_as_dict(self):
        
        try:
            
            input_data = {
                "cement": [self.cement],
                
                "blast_furnace_slag": [self.blast_furnace_slag],
                
                "fly_ash": [self.fly_ash],
                
                "water": [self.water],
                
                "superplasticizer": [self.superplasticizer],
                
                "coarse_aggregate": [self.coarse_aggregate],
                
                "fine_aggregate": [self.fine_aggregate],
                
                "age": [self.age]
                
                }
            
            return input_data
        
        
        except Exception as e:
            raise CementException(e, sys)


class CementPredictor:

    def __init__(self, model_dir: str):
        
        try:
            
            self.model_dir = model_dir
        
        except Exception as e:
            raise CementException(e, sys) from e

    
    def get_latest_model_path(self):
        
        try:
            
            folder_name = list(map(int, os.listdir(self.model_dir)))
            
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            
            file_name = os.listdir(latest_model_dir)[0]
            
            latest_model_path = os.path.join(latest_model_dir, file_name)
           
            return latest_model_path
        
        except Exception as e:
            raise CementException(e, sys) from e

    def predict(self, X):
        
        try:
            
            model_path = self.get_latest_model_path()
            
            model = load_object(file_path=model_path)
            
            concrete_compressive_strength = model.predict(X)
            
            return concrete_compressive_strength
        
        except Exception as e:
            raise CementException(e, sys) from e