import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
import pandas as pd
df = pd.read_csv('frozen2.csv')

indicator_types = ["F1", "F10"]

# Numeric cols only
valid_indicators = [col for col in df.columns if col not in ["id"]]

indicators = st.sidebar.multiselect('Indicators', valid_indicators, default=valid_indicators)

indicator_groups = {k: [i for i in indicators if i.startswith(k)] for k in indicator_types}

# how many groups have a non-empty list of indicators?
# this will be the number of rows in the subplots...
n_rows = len([i for i in indicator_groups.values() if len(i) > 0])

fig = make_subplots(rows=n_rows, cols=1)

row_idx = 1
for gk, gv in indicator_groups.items():

    # if the group has no indicators, skip it...
    if len(gv) > 0:
        
        # add one trace for each element in the group
        for col in gv:
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df[col],
                    name=col,
                ),
                row=row_idx,
                col=1,
            )

        # increase row index just if there are indicators in this group
        row_idx += 1


st.plotly_chart(fig, width= 800, height = 400 * n_rows)