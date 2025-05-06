# ⏳ Timenetix:

**Timenetix** is a user-friendly tool for time series forecasting built on top of the [Darts](https://github.com/unit8co/darts) library.

---

## ✅ Features

- ⚡ Easy-to-use CLI and Python interface
- 🧠 Access to cutting-edge models (ARIMA, Prophet, RNNs, N-BEATS, TFT, etc.)
- 📈 Visualization of forecasts and historical data
---

## 📋 Prerequisites

- Linux-based operating system (recommended)
- Python 3.9 or higher
- Git
- Installation on Windows may be possible, but it has not been tested
---

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TemporalDepth/Timenetix
   cd Timenetix
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. ## ⚙️ Installation and System Requirements

🧠 All required libraries, including [Darts](https://github.com/unit8co/darts) and its dependencies, will be installed automatically on first run.

---

### ⚡ Using with GPU (Recommended)

If you plan to use PyTorch-based models (such as `RNN`, `N-BEATS`, `TFT`) and have an NVIDIA GPU:

1. Install the latest drivers for your NVIDIA GPU
2. Install CUDA:
   - **Recommended version:** 12.6
   - **Supported (but not recommended):** 12.8
3. Install PyTorch with CUDA support
   👉 Installation guide: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

---

### 🖥 Using without GPU (CPU Only)

If you don’t have a dedicated GPU:

- Install PyTorch with **CPU-only support**
- All models will still work, but training and forecasting may be significantly slower

---

💡 Example command to install PyTorch with CPU support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


## 🧪 Quick Start

### Launch the application

If you're on Ubuntu or using a virtual environment, first activate it:
```bash
source venv/bin/activate
```

Then run the main script:
```bash
python main.py
```
or:
```bash
python3 main.py
```

---
## 🚧 Current Limitations

- Not all forecasting models provided by the [Darts](https://github.com/unit8co/darts) library are currently implemented in the project.
- Some model parameters are not yet supported.
- Advanced features and utilities offered by Darts—such as model ensembling, probabilistic forecasting, and automated hyperparameter tuning—are not yet integrated.

## 🛠️ Future Plans

- Compatible with Windows OS
- Support for **kwargs for flexible parameter configuration
- SQL query generation using SQLAlchemy
- Forecasting model comparison
- Automatic hyperparameter optimization with Optuna
- Support for alternative forecasting methods such as NeuralProphet

---

## 🖼️ interface example

![ui](image/example_workplace.png)


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- [Darts by Unit8](https://github.com/unit8co/darts) – the backbone of the forecasting engine.
