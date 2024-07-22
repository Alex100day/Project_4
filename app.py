
import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')

st.header('Vehicles_adv')
st.subheader('Car_price')

#Histogram

model_year_order = vehicles.groupby('model_year')['price'].agg(['mean', 'count']).reset_index()
hist_model_year = px.bar(model_year_order, x='model_year', y='count', 
             labels={'model_year': 'Model Year', 'count': 'Frequency'}, title='Histogram of Car Model Years Frequencies')
hist_model_year.update_traces(marker=dict(line=dict(width=2, color='Blue')))
hist_model_year.show()

st.write("### Histogram model year")
st.plotly_chart(hist_model_year)


# Scatter plot

fig_model_year = px.scatter(model_year_order, x='model_year', y='mean', title='Model year vs price')
fig_model_year.update_layout(xaxis_title='Model year', yaxis_title='Average price')
fig_model_year.show()

st.write("### Scatter: model year vs average price")
st.plotly_chart(fig_model_year)


if st.checkbox('Toggle Plot Type'):
    plot_type = st.selectbox('Select Plot Type', ['Histogram', 'Scatter Plot'])

    if plot_type == 'Histogram':
        st.plotly_chart(hist_model_year)
    elif plot_type == 'Scatter Plot':
        st.plotly_chart(fig_model_year)

