import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from criptos import *
from criptos.bitcoin import bitcoin
from criptos.ethereum import ethereum
from criptos.tether import tether
from criptos.ripple import ripple
from criptos.monero import monero
from criptos.usd_coin import usd_coin
from criptos.zcash import zcash
from criptos.true_usd import true_usd
from criptos.dash import dash
from criptos.dogecoin import dogecoin
from home import home

def leer_csv(nombre):
    df = pd.read_csv(f'datos_csv/{nombre}_coin.csv')
    return df

if st.sidebar.button('Home'):
    home()

criptomonedas = {
    'Bitcoin': 'General',
    'Ethereum': 'General',
    'Ripple': 'General',
    'Monero ': 'Privacidad',
    'Zcash ': 'Privacidad',
    'Dash ': 'Privacidad',
    'Tether': 'Estables',
    'USD Coin': 'Estables',
    'Dogecoin': 'Meme',
    'True USD ': 'Estables'
}

criptomonedas_funciones = {
    'Bitcoin': bitcoin,
    'Ethereum': ethereum,
    'Ripple': ripple,
    'Monero ': monero,
    'Zcash ': zcash,
    'Dash ': dash,
    'Tether': tether,
    'USD Coin': usd_coin,
    'True USD': true_usd,
    'Dogecoin': dogecoin
}

orden_categorias = ['General', 'Privacidad', 'Estables', 'Meme']

categoria_seleccionada = st.sidebar.selectbox('Selecciona una categoría', orden_categorias)

criptomonedas_filtradas = {nombre: categoria for nombre, categoria in criptomonedas.items() if categoria == categoria_seleccionada}

tabs = st.sidebar.radio('Selecciona una criptomoneda', list(criptomonedas_filtradas.keys()))

if tabs in criptomonedas_funciones:
    criptomonedas_funciones[tabs]()
