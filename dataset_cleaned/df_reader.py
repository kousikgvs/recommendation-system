import pandas as pd

def load_df(filename):
    df_new = pd.read_csv(filename)
    return df_new

def save_df(df, filename):
    df.to_csv(f"dataset_cleaned\\{filename}", index=False)