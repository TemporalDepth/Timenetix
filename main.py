
# ---------- Imports ----------
import os
import sys
import json
import gradio as gr
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from darts import TimeSeries
from darts_models.darts_models_script import create_component

# ---------- Paths ----------
from darts_models.darts_models_script import run_forecast_model
from ui_script.interface_script import load_model_types
from ui_script.interface_script import plot_time_series
from ui_script.interface_script import load_model_variants
from ui_script.interface_script import save_file

from ui_script.interface_script import load_csv
from ui_script.darts_menu import component_dict

# ---------- Gradio Interface ----------

with gr.Blocks() as demo:
    with gr.Column():
        gr.Markdown(
            """
            # Darts Time Series Forecasting
            Upload a CSV file with datetime and target columns (only two columns).
            """
        )
        file_uploader = gr.File(
            label="Upload file",
            height=400,
            file_types=[".csv"],
            file_count="single"
        )
        table_output = gr.Dataframe(max_height=200, col_count=2)
        time_series_plot = gr.Plot(label="Time Series Plot")

    with gr.Row():
        with gr.Column():
            model_types = load_model_types()

            gr.HTML(
                "<div style='margin-top: 20px; font-size: 16px;'>"
                "<a href='https://unit8co.github.io/darts/#forecasting-models' target='_blank'>🔗 Learn more about Darts models</a>"
                "</div>"
            )

            with gr.Row():
                with gr.Column():
                    model_type_dropdown = gr.Dropdown(
                        model_types,
                        interactive=True,
                        label="Model Type",
                        value='Choose model type'
                    )
                    model_variant_dropdown = gr.Dropdown(
                        choices=[],
                        interactive=True,
                        label="Model Variant"
                    )
                with gr.Column():
                    selected_variant_state = gr.State("")

                    model_variant_dropdown.change(
                        fn=lambda x: x,
                        inputs=model_variant_dropdown,
                        outputs=selected_variant_state
                    )

                    train_test_split_value = gr.Number(
                        label='Train/Test Split',
                        value=0.8,
                        interactive=True
                    )
                    forecast_horizon_value = gr.Number(
                        label='Forecast Horizon',
                        value=12,
                        interactive=True
                    )

                    @gr.render(inputs=selected_variant_state)
                    def render_model_params(variant_key):
                        with gr.Row():
                            component_configs = component_dict.get(variant_key, [])
                            model_param_inputs = [
                                create_component({k: v for k, v in cfg.items() if k != 'param_name'})
                                for cfg in component_configs
                            ]

                            forecast_button.click(
                                fn=run_forecast_model,
                                inputs=[table_output, model_variant_dropdown, train_test_split_value, forecast_horizon_value] + model_param_inputs,
                                outputs= [forecast_plot_output,forecast_table_output],
                                scroll_to_output=True
                            )



            forecast_button = gr.Button("Predict", variant="primary", elem_id="forecast_button")
            forecast_plot_output = gr.Plot(label="Forecast Plot")
            forecast_table_output = gr.Dataframe(max_height=300, col_count=2)

            with gr.Column():
                gr.Markdown(
                """
                The output file is stored in the '''output''' folder within the project’s root directory.
                """)
                save_file_name = gr.Textbox(label = 'file name')
                select_extension_to_save = gr.Dropdown(
                        ["csv","excel"],
                        interactive=True,
                        label="select file extension for save"
                    )


            save_forecast_button = gr.Button("Save", variant="primary", elem_id="save_button")
            save_forecast_button.click(
                                    fn = save_file,
                                    inputs = [save_file_name,select_extension_to_save,forecast_table_output],
                                    outputs = None
                                )


    # ---------- Event Listeners ----------
    file_uploader.change(fn=load_csv, inputs=file_uploader, outputs=table_output)
    file_uploader.change(fn=plot_time_series, inputs=file_uploader, outputs=time_series_plot)

    model_type_dropdown.change(
        fn=load_model_variants,
        inputs=model_type_dropdown,
        outputs=model_variant_dropdown
    )

# ---------- Launch ----------
demo.launch()
