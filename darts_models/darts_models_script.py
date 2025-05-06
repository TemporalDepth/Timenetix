import pandas as pd
import gradio as gr
import plotly.graph_objects as go

from darts import TimeSeries
from darts.models import (
    RNNModel, BlockRNNModel,
    NBEATSModel, TCNModel, TransformerModel,
    NHiTSModel,ExponentialSmoothing, Prophet,
    RegressionModel,LinearRegressionModel,RandomForest,LightGBMModel,
    XGBModel,CatBoostModel,
    RNNModel, BlockRNNModel, NBEATSModel, NHiTSModel,
      TCNModel, TransformerModel, TFTModel,DLinearModel,
      NLinearModel, TiDEModel, TSMixerModel
    )

from darts.metrics import mape
from darts_models.create_models_param import ModelParamBuilder
from sklearn.linear_model import (
    LinearRegression, Ridge, RidgeCV, SGDRegressor
)
# ---------- Utils ----------

def create_component(component_config):
    component_type = component_config.pop("type")
    component_class = getattr(gr, component_type, None)
    if component_class is None:
        raise ValueError(f"Unknown component type: {component_type}")
    return component_class(**component_config)

# ---------- Core Forecast Logic ----------


def run_forecast_model(series, model_name, train_ratio, forecast_horizon, *args):

    series = series.copy()

    datetime_col = None
    value_col = None


    for col in series.columns:
        if series[col].dtype == 'object':
            converted = pd.to_datetime(series[col], errors='coerce')
            if converted.notna().sum() > 0.8 * len(series):
                series[col] = converted


    for col in series.columns:
        if pd.api.types.is_datetime64_any_dtype(series[col]):
            datetime_col = col
        elif pd.api.types.is_numeric_dtype(series[col]):
            value_col = col


    if datetime_col is None or value_col is None:
        raise ValueError("Timestamp columns not found or value column not detected.")


    model_params = ModelParamBuilder(model_name, *args).model_params


    series = TimeSeries.from_dataframe(series, time_col=datetime_col, value_cols=value_col)

    train_series, test_series = series.split_before(train_ratio)
    prediction_length = forecast_horizon or len(test_series)

    model_class = getattr(__import__('darts.models', fromlist=[model_name]), model_name, None)
    if model_class is None:
        raise ValueError(f"Model '{model_name}' not found in darts.models.")

    model = model_class(**model_params)
    model.fit(train_series)

    forecast_series = model.predict(prediction_length)

    error_score = mape(test_series, forecast_series)

    fig = plot_forecast(train_series.concatenate(test_series), forecast_series, test_series, model_name, error_score)

    forecast_dataframe = forecast_series.to_dataframe().reset_index()

    return fig , forecast_dataframe

def plot_forecast(series, forecast, test_series, model_name, mape_score):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=series.time_index,
        y=series.values().flatten(),
        mode='lines',
        name='Actual'
    ))

    fig.add_trace(go.Scatter(
        x=forecast.time_index,
        y=forecast.values().flatten(),
        mode='lines',
        name='Forecast'
    ))

    fig.update_layout(
        title=f"{model_name} Forecast (MAPE: {mape_score:.2f}%)",
        xaxis_title="Date",
        yaxis_title="Value",
        template="plotly_white",
        legend_title="Legend"
    )

    return fig
