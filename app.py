
import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')

st.header('Web application development')
introduction = """ In this project we will develop and deploy a web application to a cloud service making it accessible to the public. \ 
 The projects tasks include opening accounts on github and render.com. Git repositary with README.md and gitignore files will be created. \ 
 Jupyter notebook platform, VS Code (as an IDE) and python with its packages necessary to perform the project taks will be used.  \ 
 We will work on the dataset on car sales advertisements. First, using Jupyter notebook in VS Code IDE the dataset will be preprocced \ 
 (working on missing and duplicated values). Further analisys will be done by excluding outlires and finding the correlations between column values. \ 
 The revealed correlations we will visualized by plotting (scatter and histogram) the figures. These results will be stored in EDA.ipynb.
Next, in order to develop web applications we create app.py file in the root directory of the project. The main results including the obtained \ 
figures in EDA.ippynb will be copied to app.py. After getting all files with necessary results and contents we will commit and push them \ 
to the git repository. Committing and pushing processes of any update/change on the git repository files and directories will be done repeatedly \ 
until getting the final results on the web app. """
st.subheader('Car advertisement')


#Preprosessing ['model_year'], ['cylinders'], ['odometer'] columns

vehicles['model_year'] = vehicles.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
vehicles['cylinders'] = vehicles.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
vehicles['odometer'] = vehicles.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))


# 'model_year' is strongly right-skewed, and consider only cars produced since 1995, excluding older cars as outlires 

lower_year = 1995
vehicles = vehicles[vehicles['model_year'] >= lower_year]

# Here, we study the dependence of the car prices on their model years

#Histogram

model_year_order = vehicles.groupby('model_year')['price'].agg(['mean', 'count']).reset_index()
hist_model_year = px.bar(model_year_order, x='model_year', y='count', 
             labels={'model_year': 'Model Year', 'count': 'Frequency'}, title='Histogram of Car Model Years Frequencies')
hist_model_year.update_traces(marker=dict(line=dict(width=2, color='Blue')))
hist_model_year.show()

st.write("###Histogram model year")
st.plotly_chart(hist_model_year)


# Scatter plot

fig_model_year = px.scatter(model_year_order, x='model_year', y='mean', title='model year vs price')
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



st.markdown('## Main outcomes.')
outcome = """ The analysis of the dataset after preprocessing, grouping and filtering allows obtaining correlation \
    between car prices and model year and car conditions. These correlations visualized by histograms and scatter-style figures. \
    The above shown figure demonstrates the gradual increase of avarage prices of cars from older to newer ones. \
    The above shown histogram demonstrates that the cars produced 2011 - 2013 are most popular ones. \ 
    The decrease corresponding to 2009 - 2010 can be caused by the crisis in economy. 
    """
st.markdown(outcome)