# models_param_convert.py
import ast
import pandas as pd

from darts.models import (
    RNNModel, BlockRNNModel,
    NBEATSModel, TCNModel, TransformerModel, 
    NHiTSModel,ExponentialSmoothing,
    RegressionModel,LinearRegressionModel,RandomForest,LightGBMModel,
    XGBModel,CatBoostModel
)
from darts.utils.utils import ModelMode, SeasonalityMode
from ui_script.darts_menu import component_dict
from sklearn.linear_model import Ridge, LinearRegression,RidgeCV,SGDRegressor

class ModelParamBuilder:
    def __init__(self, model_name, *args):
        self.model_name = model_name
        self.args = args
        self.model_params = self.dispatch()

    def dispatch(self):
        model_func = getattr(self, self.model_name, None)
        if callable(model_func):
            return model_func(*self.args)
        else:
            raise ValueError(f"Model '{self.model_name}' not found in ModelParamBuilder.")

    def __str__(self):
        return self.model_name

    def _build_param_dict(self, args):
        param_labels = [component.get('param_name', '') for component in component_dict[self.model_name]]
        return dict(zip(param_labels, args))

    # ------------ Baseline Models -----------------------            
    def NaiveMean(self, *args):
        return self._build_param_dict(args)

    def NaiveSeasonal(self, *args):
        return self._build_param_dict(args)

    def NaiveDrift(self, *args):
        return self._build_param_dict(args)

    def NaiveMovingAverage(self, *args):
        return self._build_param_dict(args)

    # ------------- Statistical Models ---------------------
    def ARIMA(self, *args):
        param_dict = self._build_param_dict(args)
        for key, value in param_dict.items():
            if isinstance(value, pd.DataFrame):
                param_dict[key] = tuple(value.iloc[0].astype(int))
        return param_dict

    def AutoARIMA(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def ExponentialSmoothing(self, *args):
        param_dict = self._build_param_dict(args)
        for key in ["trend", "seasonal"]:
            if key in param_dict:
                param_dict[key] = getattr(ModelMode, param_dict[key])
        for key in ["seasonal_periods"]:
            if key in param_dict and param_dict[key] == 0:
                param_dict[key] = None
        return param_dict


    def TBATS(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def Theta(self, *args):
        param_dict = self._build_param_dict(args)
        for key in ["season_mode"]:
            if key in param_dict:
                param_dict[key] = getattr(SeasonalityMode, param_dict[key])
        for key in ["seasonality_period"]:
            if key in param_dict and param_dict[key] == 0:
                param_dict[key] = None
        return param_dict


    def RegressionModel(self, *args):
        MODEL_MAP = {
            'LinearRegression': LinearRegression,
            'Ridge': Ridge,
            'Ridge': RidgeCV,
            'SGDRegressor': SGDRegressor
            }
        param_dict = self._build_param_dict(args)
        
        for key, value in param_dict.items():
            if param_dict[key] in MODEL_MAP:
               param_dict[key] = MODEL_MAP[value]()
             
            else:
                
                raise ValueError(f"Неизвестная модель: {value}")
            return param_dict 
    
    def LinearRegressionModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def RandomForest(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def LightGBMModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def XGBModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def CatBoostModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def RNNModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict
    
    def BlockRNNModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def NBEATSModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def NHiTSModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def TCNModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def TransformerModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def TFTModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def DLinearModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def NLinearModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def TiDEModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

    def TSMixerModel(self, *args):
        param_dict = self._build_param_dict(args)
        return param_dict

        


