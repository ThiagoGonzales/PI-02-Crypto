import streamlit as st
import pandas as pd
import plotly.express as px

def home():
    st.title('KPI')
    st.markdown('***')

    st.markdown('## Consumo de TWh por año del Bitcoin')
    kpi = pd.read_csv('.\\btc_csv\\bitcoin-kpi.csv')

    fig = px.line(kpi, x='date', y=['Estimated TWh per Year', 'Minimum TWh per Year', 'price'],
              labels={'value': 'Valor', 'variable': 'Variable', 'date': 'Fecha'})

    st.plotly_chart(fig)    