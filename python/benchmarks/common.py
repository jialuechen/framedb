
import pandas as pd
import numpy as np


def generate_pseudo_random_dataframe(n, freq="s", end_timestamp="1/1/2023"):
    # Generate random values such that their sum is equal to N
    values = np.random.uniform(0, 2, size=n)
    # Generate timestamps
    timestamps = pd.date_range(end=end_timestamp, periods=n, freq=freq)
    # Create dataframe
    df = pd.DataFrame({"value": values})
    df.index = timestamps
    return df


def generate_random_floats_dataframe(num_rows, num_cols):
    
    columns = [f"col_{n}" for n in range(num_cols)]
    rng = np.random.default_rng()
    data = rng.random((num_rows, num_cols), dtype=np.float64)
    return pd.DataFrame(data, columns=columns)


def generate_benchmark_df(n, freq="min", end_timestamp="1/1/2023"):
    timestamps = pd.date_range(end=end_timestamp, periods=n, freq=freq)
    k = n // 10
    dt = pd.DataFrame()
    dt["id1"] = np.random.choice([f"id{str(i).zfill(3)}" for i in range(1, k + 1)], n)
    dt["id2"] = np.random.choice([f"id{str(i).zfill(3)}" for i in range(1, k + 1)], n)
    dt["id3"] = np.random.choice([f"id{str(i).zfill(10)}" for i in range(1, n // k + 1)], n)
    dt["id4"] = np.random.choice(range(1, k + 1), n)
    dt["id5"] = np.random.choice(range(1, k + 1), n)
    dt["id6"] = np.random.choice(range(1, n // k + 1), n)
    dt["v1"] = np.random.choice(range(1, 6), n)
    dt["v2"] = np.random.choice(range(1, 16), n)
    dt["v3"] = np.round(np.random.uniform(0, 100, n), 6)

    assert len(timestamps) == len(dt)

    dt.index = timestamps

    return dt


def get_prewritten_lib_name(rows):
    return f"prewritten_{rows}"
