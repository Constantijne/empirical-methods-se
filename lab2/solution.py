import pandas as pd
import streamlit as st

df = pd.read_csv('data.txt', sep=",", header=None,
                 names=["loc", "vg", "evg", "ivg", "n", "v", "l", "d", "i", "e", "b", "t",
                        "lOCode", "lOComment", "lOBlank", "locCodeAndComment", "uniq_Op", "uniq_Opnd", "total_Op",
                        "total_Opnd", "branchCount"])


filter_plot = st.multiselect("Choose filter", list(df.index),
                             )
data = df.loc[filter_plot]
st.area_chart(data.sort_index())
st.dataframe(data.sort_index())
