import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 5)

# and used to select the displayed lines
head_df = df.head(line_count)

st.write(df)

def get_map_data():

    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)


def get_dataframe_data():

    return pd.DataFrame(
            np.random.randn(10, 5),
            columns=('col %d' % i for i in range(5))
        )

df = get_dataframe_data()

cm = sns.color_palette("coolwarm_r", as_cmap=True)
df = df.head().style.background_gradient(cmap=cm)



def get_bar_chart_data():

    return pd.DataFrame(
            np.random.randn(50, 3),
            columns=["a", "b", "c"]
        )

chart_data = get_bar_chart_data()

st.bar_chart(chart_data)



head_df