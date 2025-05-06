component_dict = {

#------Baseline Models---------

    "NaiveMean": [
    ],
    "NaiveSeasonal": [
        {"type": "Number", "label": "K-value", "param_name": "K"},
    ],
    "NaiveDrift": [
    ],
    "NaiveMovingAverage": [
        {"type": "Number", "label": "input_chunk_length", "param_name": "input_chunk_length"},
    ],

#------Statistical / Classic Models----
    "ARIMA": [
        {"type": "Number", "label": "p-value", "param_name": "p"},
        {"type": "Number", "label": "d-value", "param_name": "d"},
        {"type": "Number", "label": "q-value", "param_name": "q"},
        {
            "type": "Dataframe",
            "label": "seasonal_order",
            "headers": ["p", "d", "q", "s"],
            "datatype": ["number", "number", "number", "number"],
            "col_count": (4, "fixed"),
            "row_count": (1, "fixed"),
            "value": [[0, 0, 0, 12]],
            "param_name": "seasonal_order"
        },
        {
            "type": "Dropdown",
            "label": "trend",
            "choices": ["n", "t", "ct", "c"],
            "interactive": True,
            "param_name": "trend"
        }
    ],
    "AutoARIMA": [
        {
            "type": "Number", "label": "season_length", "param_name": "season_length"
        },
    ],
    "ExponentialSmoothing": [
        {
            "type": "Dropdown",
            "label": "trend",
            "choices": ["NONE", "ADDITIVE", "MULTIPLICATIVE"],
            "interactive": True,
            "param_name": "trend"
        },
        {
            "type": "Dropdown",
            "label": "seasonal",
            "choices": ["NONE", "ADDITIVE", "MULTIPLICATIVE"],
            "interactive": True,
            "param_name": "seasonal"
        },

        {
            "type": "Checkbox", "label": "damped", "param_name": "damped"
        },
        {
            "type": "Number", "label": "seasonal_periods", "param_name": "seasonal_periods"
        },

    ],
    "TBATS": [
        {"type": "Number", "label": "season_length", "value": 12, "param_name": "season_length"},
    ],
    "Theta": [
        {
            "type": "Dropdown",
            "label": "season_mode",
            "choices": ["NONE", "ADDITIVE", "MULTIPLICATIVE"],
            "interactive": True,
            "param_name": "season_mode"
        },
        {
            "type": "Number", "label": "seasonality_period", "param_name": "seasonality_period"
        },
    ],
    "Prophet": [
        {
            "type": "Textbox",
            "label": "seasonality_mode",
            "value": "'name':'quarterly_seasonality','seasonal_periods':4,'fourier_order':5",

        }

#---------Regression Models--------

    ],
    "RegressionModel": [
        {
            "type": "Dropdown",
            "label": "trend",
            "choices": ["LinearRegression", "Ridge", "RidgeCV", "SGDRegressor"],
            "interactive": True,
            "param_name": "model"
        },
        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        }
    ],
    "LinearRegressionModel": [

        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        },

    ],
    "RandomForest": [
        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "n_estimators", "param_name": "n_estimators"
        },
        {
            "type": "Dropdown",
            "label": "criterion",
            "choices": ["absolute_error", "squared_error"],
            "interactive": True,
            "param_name": "criterion"
        },

    ],
    "LightGBMModel": [

        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        },

    ],
    "XGBModel": [
        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        },

    ],
    "CatBoostModel": [

        {
            "type": "Number", "label": "lags", "param_name": "lags"
        },
        {
            "type": "Number", "label": "output_chunk_length", "param_name": "output_chunk_length"
        },

    ],

    #---------NN Models--------
    "RNNModel": [
        {
            "type": "Dropdown",
            "label": "model",
            "choices": ["RNN", "LSTM", "GRU"],
            "interactive": True,
            "param_name": "model"
        },
        {
            "type": "Number", "label": "hidden_dim", "value": 64, "param_name": "hidden_dim"
        },
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "training_length", "value": 48, "param_name": "training_length"
        },
        {
            "type": "Number", "label": "n_rnn_layers", "value": 2, "param_name": "n_rnn_layers"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "BlockRNNModel": [
        {
            "type": "Number", "label": "hidden_dim", "value": 64, "param_name": "hidden_dim"
        },
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "n_rnn_layers", "value": 2, "param_name": "n_rnn_layers"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "NHiTSModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "NBEATSModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "TCNModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "TransformerModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],

    "DLinearModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },

        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "NLinearModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },

        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "TiDEModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ],
    "TSMixerModel": [
        {
            "type": "Number", "label": "input_chunk_length", "value": 24, "param_name": "input_chunk_length"
        },
        {
            "type": "Number", "label": "output_chunk_length", "value": 12, "param_name": "output_chunk_length"
        },
        {
            "type": "Number", "label": "dropout", "value": 0.1, "param_name": "dropout"
        },
        {
            "type": "Number", "label": "batch_size", "value": 64, "param_name": "batch_size"
        },
        {
            "type": "Number", "label": "n_epochs", "value": 100, "param_name": "n_epochs"
        }
    ]


}
