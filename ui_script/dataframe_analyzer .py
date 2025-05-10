import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose

class TimeSeriesAnalyzer:
    def __init__(self, series):
        self.series = series.dropna()

    def assess_mean_std_stability(self, segments=4):
        segment_length = len(self.series) // segments
        means = []
        stds = []

        for i in range(segments):
            segment = self.series[i * segment_length:(i + 1) * segment_length]
            if len(segment) > 0:
                means.append(segment.mean())
                stds.append(segment.std())

        mean_variation = max(means) - min(means)
        std_variation = max(stds) - min(stds)

        return {
            'segment_means': means,
            'segment_stds': stds,
            'mean_variation': mean_variation,
            'std_variation': std_variation,
            'is_mean_stable': mean_variation < 0.1 * np.mean(means),
            'is_std_stable': std_variation < 0.1 * np.mean(stds)
        }

    def adf_test(self, signif=0.05):
        result = adfuller(self.series)
        return {
            'adf_statistic': result[0],
            'adf_p_value': result[1],
            'adf_lags_used': result[2],
            'adf_n_obs': result[3],
            'adf_critical_values': result[4],
            'adf_is_stationary': result[1] <= signif
        }

    def kpss_test(self, signif=0.05, regression='c'):
        statistic, p_value, lags, critical_values = kpss(self.series, regression=regression, nlags="auto")
        return {
            'kpss_statistic': statistic,
            'kpss_p_value': p_value,
            'kpss_lags_used': lags,
            'kpss_critical_values': critical_values,
            'kpss_is_stationary': p_value > signif
        }

    def compute_acf_pacf(self, nlags=40):
        acf_vals = acf(self.series, nlags=nlags)
        pacf_vals = pacf(self.series, nlags=nlags)
        return {
            'acf_values': acf_vals.tolist(),
            'pacf_values': pacf_vals.tolist()
        }

    def decompose(self, model='additive', freq=None):
        decomposition = seasonal_decompose(self.series, model=model, period=freq)
        trend = decomposition.trend.dropna() if decomposition.trend is not None else None
        seasonal = decomposition.seasonal.dropna() if decomposition.seasonal is not None else None
        resid = decomposition.resid.dropna() if decomposition.resid is not None else None
        return {
            'trend': trend.tolist() if trend is not None else None,
            'seasonal': seasonal.tolist() if seasonal is not None else None,
            'residual': resid.tolist() if resid is not None else None
        }

    def full_summary(self, signif=0.05, segments=4, nlags=40, freq=None):
        summary = {}
        summary.update(self.assess_mean_std_stability(segments))
        summary.update(self.adf_test(signif))
        summary.update(self.kpss_test(signif))
        summary.update(self.compute_acf_pacf(nlags))
        summary.update(self.decompose(model='additive', freq=freq))
        return summary
