from dash import callback, Input, Output
import pandas as pd

df = pd.read_csv("datas/avocado.csv")

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
def update_table(selected_region, selected_types):
    filtered_df = df.copy()

    if selected_region:
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    if selected_types and "ALL" not in selected_types:
        filtered_df = filtered_df[filtered_df["type"].isin(selected_types)]

    filtered_df = filtered_df.drop(
        columns=[col for col in COLUMNS_TO_HIDE if col in filtered_df.columns]
    )

    return (
        filtered_df.to_dict("records"),
        f"Nombre de lignes affichées : {len(filtered_df)}"
    )