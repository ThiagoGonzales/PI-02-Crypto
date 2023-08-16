from funciones.fun import logo, grafico
import streamlit as st

def usd_coin():
    moneda = 'usd_coin'

    st.title('USD Coin')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del USD Coin')
        resumen = '''USD Coin (USDC) es una stablecoin respaldada por el dólar estadounidense emitida por el consorcio CENTRE, una colaboración entre Circle y Coinbase. Al igual que otras stablecoins, el objetivo principal de USD Coin es proporcionar estabilidad en el valor y facilitar transacciones y pagos en el mundo de las criptomonedas.

**Estabilidad de Precio:** Al igual que otras stablecoins, USD Coin está diseñado para mantener una paridad 1:1 con el dólar estadounidense (USD). Cada token USDC emitido se respalda por una reserva de dólares estadounidenses en custodia, lo que proporciona estabilidad en el valor y reduce la volatilidad inherente a muchas otras criptomonedas.

**Transparencia y Regulación:** USD Coin pone un fuerte énfasis en la transparencia y el cumplimiento regulatorio. Las reservas subyacentes de dólares se auditan de manera regular para garantizar que la cantidad de USDC en circulación esté respaldada adecuadamente por activos reales.

**Uso y Adopción:** USD Coin se utiliza en una variedad de aplicaciones en el ecosistema de las criptomonedas, como intercambios de criptomonedas, plataformas de comercio y pagos. Debido a su estabilidad, los usuarios pueden utilizar USD Coin como una forma de mantener valor en un entorno criptográfico sin preocuparse por la volatilidad del mercado.

**Rápida Liquidación:** USD Coin también permite la transferencia rápida y eficiente de fondos a nivel global. Esto puede ser especialmente útil en comparación con los sistemas de transferencia de dinero tradicionales, que a menudo involucran tiempos de procesamiento más largos y tarifas más altas.
'''

        st.write(resumen)