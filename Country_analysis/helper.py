import pandas as pd
def regionAna(df):
    df["Surface area (km2)"]=df["Surface area (km2)"]=pd.to_numeric(df["Surface area (km2)"],errors='coerce')

    sa=df.groupby("Region").sum()[["Surface area (km2)"]].sort_values("Surface area (km2)",ascending=False).reset_index()
    return sa
    

    