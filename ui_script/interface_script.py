# ---------- Imports ----------
import os
import sys
import json
import openpyxl
import gradio as gr
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



def load_csv(file):
    df = pd.read_csv(file)
    return df

def plot_time_series(file):
    import pandas as pd
    import plotly.express as px

    df = pd.read_csv(file)


    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception:
                pass

    datetime_col = None
    value_col = None

    for col in df.columns:
        if datetime_col is None and pd.api.types.is_datetime64_any_dtype(df[col]):
            datetime_col = col
        elif value_col is None and pd.api.types.is_numeric_dtype(df[col]):
            value_col = col

    # Проверка, что всё найдено
    if datetime_col is None or value_col is None:
        raise ValueError("Failed to identify the time and numeric column.")

    fig = px.line(df, x=datetime_col, y=value_col, title='Time series')
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=[
                    dict(count=7, label="7d", step="day", stepmode="backward"),
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ]
            ),
            rangeslider=dict(visible=True),
            type="date"
        )
    )
    return fig


def load_model_types():
    with open("darts_models/darts_model_name.json", "r") as file:
        data = json.load(file)
    return list(data.keys())

def load_model_variants(model_type):
    with open("darts_models/darts_model_name.json", "r") as file:
        data = json.load(file)
    model_variants = data[model_type]
    return gr.update(choices=model_variants, value=model_variants[0])

def save_file(file_name,pandas_save_method,file):

    if pandas_save_method == "excel":
        file_extension = "xlsx"
    else:
        file_extension = pandas_save_method

    save_file = getattr(file,f'to_{pandas_save_method}')
    save_file(f'output/{file_name}.{file_extension}', index = False)

    gr.Info(f'✅ File successfully saved as output/{file_name}.{file_extension}')
