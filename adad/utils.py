import time

import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype


def time2str(time_elapsed, formatstr='%Hh%Mm%Ss'):
    """Format millisecond to string."""
    return time.strftime(formatstr, time.gmtime(time_elapsed))


def category2code(df):
    """Change all columns to ordinal data, represent in codes.
    (e.g.: from {2, 5, 8} to {0, 1, 2})
    """
    result = df.copy()
    for c in df.columns:
        categories = np.sort(np.unique(df[c].to_numpy()))
        cattype = CategoricalDtype(categories=categories, ordered=True)
        result[c] = result[c].astype(cattype).cat.codes
    return result


def get_range(X):
    """Return a tuple of minimal and maximum values"""
    if isinstance(X, pd.DataFrame):
        return (X.min(axis=0).to_numpy(), X.max(axis=0).to_numpy())
    return X.min(axis=0), X.max(axis=0)
