from funciones.fun import logo, grafico
import streamlit as st 

def true_usd():
    moneda = 'true_usd'

    st.title('True_USD')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del True USD')
        resumen = '''TrueUSD (TUSD) es otra stablecoin, similar a Tether (USDT), que busca mantener una paridad 1:1 con el dólar estadounidense (USD). Al igual que otras stablecoins, TrueUSD se creó para ofrecer estabilidad en el valor y facilitar las transacciones en el mundo de las criptomonedas sin verse afectado por la volatilidad característica de muchas otras criptomonedas.

**Estabilidad de Precio:** TrueUSD se emite en función del valor del dólar estadounidense y se respalda por dólares reales en custodia. Esto significa que cada token TUSD debería estar respaldado por un dólar en la cuenta bancaria correspondiente. Esta paridad tiene como objetivo proporcionar a los usuarios una forma confiable de mantener valor en el mundo de las criptomonedas sin preocuparse por las fluctuaciones extremas de precio.

**Transparencia y Auditoría:** Una característica distintiva de TrueUSD es su enfoque en la transparencia y la auditoría. La empresa detrás de TrueUSD, TrustToken, se ha comprometido a realizar auditorías mensuales de sus cuentas bancarias para demostrar que el respaldo fiduciario está en su lugar y que cada token TUSD está respaldado adecuadamente.

**Uso y Adopción:** TrueUSD se utiliza en una variedad de aplicaciones en el ecosistema de las criptomonedas, como intercambios de criptomonedas, plataformas de comercio y pagos. Los usuarios pueden utilizar TrueUSD para mover valor de manera rápida y eficiente en un entorno que mantiene una paridad con el dólar.
'''

        st.write(resumen)