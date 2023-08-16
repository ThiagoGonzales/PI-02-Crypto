import pandas as pd
#from pycoingecko.pycoingecko import CoinGeckoAPI
import streamlit as st
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import numpy as np

#cg = CoinGeckoAPI()

'''def cripto(cripto):
    moneda = cg.get_coin_market_chart_range_by_id(cripto, 'usd', '1577761200', '1640908800')
    moneda = pd.DataFrame(moneda)
    columns_to_drop = ['market_caps','total_volumes']
    moneda.drop(columns=columns_to_drop, axis=1, inplace=True)
    moneda[['date', 'price']] = pd.DataFrame(moneda['prices'].tolist(), columns=['date', 'price'])
    moneda = moneda.drop(columns=['prices'])
    moneda['date'] = pd.to_datetime(moneda['date'], unit='ms')
    nombre_archivo = f'datos_csv{cripto}_coin.csv'
    moneda.to_csv(nombre_archivo, index=False)
    return moneda'''

def consumo_bitcoin():
    return pd.read_csv('.\\btc_csv\\bitcoin-energy-consum.csv')

def logo(nombre, x=300):
    imagen = f'imagenes\\{nombre}.png'
    return st.image(imagen, caption='Imagen', width=x)

def detectar_outliers(data, dates, min_distance_days=3):
    z_scores = np.abs(stats.zscore(data))
    threshold = 3
    outliers = np.where(z_scores > threshold)[0]
    
    filtered_outliers = []
    last_outlier_index = -min_distance_days - 1
    for i in outliers:
        if i - last_outlier_index > min_distance_days:
            filtered_outliers.append(i)
            last_outlier_index = i
    
    return filtered_outliers

def detectar_movimientos_significativos(data, dates, threshold_percentage=0.4, window_size=16):
    movimientos_significativos = []
    for i in range(len(data) - window_size + 1):
        inicio = i
        fin = i + window_size - 1
        cambio_porcentual = (data[fin] - data[inicio]) / data[inicio]
        if abs(cambio_porcentual) > threshold_percentage:
            if cambio_porcentual > 0:
                color = "green"
            else:
                color = "red"
            movimientos_significativos.append((dates[inicio], dates[fin], color))
    return movimientos_significativos

def grafico(nombre):
    df = pd.read_csv(f'./btc_csv/{nombre}.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    fig = px.line(df, x='date', y='price', title='Precio vs Fecha')
    fig.update_xaxes(title_text='Fecha', tickangle=45)
    fig.update_yaxes(title_text='Precio en USD')
    
    outliers = detectar_outliers(df['price'], df['price'])

    def bgLevels(fig, movimientos_significativos, layer):
        for inicio, fin, color in movimientos_significativos:
            fig.add_shape(
                type="rect",
                xref="x",
                yref="paper",
                x0=inicio,
                y0=0,
                x1=fin,
                y1=1,
                line=dict(color="rgba(0,0,0,0)", width=3),
                fillcolor=color,
                layer=layer,
                opacity=1
            )
        return fig

    movimientos_significativos = detectar_movimientos_significativos(df['price'], df['date'])

    fig = bgLevels(fig=fig, movimientos_significativos=movimientos_significativos,
                   layer='below')

    for i in outliers:
        fig.add_annotation(
            x=df.loc[i, 'date'],
            y=df.loc[i, 'price'],
            text="Outlier",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="red",
            bgcolor="rgba(255, 0, 0, 0.5)",
        )

    fig.update_traces(line=dict(color='purple'))

    st.plotly_chart(fig)

