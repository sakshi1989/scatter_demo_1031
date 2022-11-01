import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Import WHO data set
who_data = pd.read_csv("WHO_data.csv")

st.header("**The data loaded is:**")
st.write(who_data)

st.sidebar.header("Pick two variables for your scatterplot")

st.header("**Scatter plot and correlation value**")
x_val = st.sidebar.selectbox("Pick your x-axis",list(who_data.select_dtypes(include=np.number).columns))

if x_val != '':    
    cols_list = who_data.select_dtypes(include=np.number).columns.tolist()
    cols_list.remove(x_val)        
    y_val = st.sidebar.selectbox("Pick your y-axis",cols_list)

scatter1 = alt.Chart(who_data, title = f'Correlation between {x_val} and {y_val}')\
    .mark_point(size = 100, color = 'red', opacity = 0.9, fill = 'green')\
    .encode(
            alt.X(x_val, title=f'{x_val}'),
            alt.Y(y_val, title=f'{y_val}'),
            tooltip = [x_val,y_val]
            )

st.altair_chart(scatter1, use_container_width=True)

# calculate the correlation 
corr_data = round(who_data[x_val].corr(who_data[y_val]),2)

st.write(f"_The correlation between {x_val} and {y_val} is {corr_data}_")
