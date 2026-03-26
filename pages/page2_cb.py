import os
from dash import callback, Input, Output
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CSV_PATH = os.path.join(BASE_DIR, "datas", "avocado.csv")

df = pd.read_csv(CSV_PATH)

COLUMNS_TO_HIDE = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags",
]

@callback(
    Output("page2-table", "data"),
    Output("page2-badge-count", "children"),
    Input("page2-region-dropdown", "value"),
    Input("page2-type-checklist", "value"),
)
def update_table(selected_region, selected_type):
    filtered_df = df.copy()

    if selected_region:
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    if selected_type and selected_type != "ALL":
        filtered_df = filtered_df[filtered_df["type"] == selected_type]

    filtered_df = filtered_df.drop(
        columns=[col for col in COLUMNS_TO_HIDE if col in filtered_df.columns]
    )

    return filtered_df.to_dict("records"), f"Lignes: {len(filtered_df)}"