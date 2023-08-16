from funciones.fun import logo, grafico
import streamlit as st

def tether():
    moneda = 'tether'

    st.title('Tether')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Bitcoin')
        resumen = '''Tether (USDT) es una criptomoneda conocida como "stablecoin" que se diseñó para mantener una paridad 1:1 con una moneda fiduciaria, generalmente el dólar estadounidense (USD). A diferencia de otras criptomonedas que pueden experimentar fluctuaciones de precios significativas, las stablecoins como Tether buscan proporcionar estabilidad y facilitar la transferencia de valor entre las monedas tradicionales y el entorno de las criptomonedas.

**Estabilidad de Precio:** Tether se emite y respalda con una cantidad equivalente de moneda fiduciaria en custodia. Esto significa que, en teoría, 1 USDT siempre debería valer aproximadamente 1 USD. Esta estabilidad de precio permite a los usuarios retener valor en forma de criptomoneda sin verse afectados por las volatilidades del mercado.

**Casos de Uso:** Tether es ampliamente utilizado en el ecosistema de las criptomonedas como una forma de mover fondos rápidamente entre intercambios y servicios sin tener que pasar por el sistema bancario tradicional. También se utiliza como una forma de mantener un valor estable durante períodos de volatilidad en otros activos digitales.

**Emisión y Transparencia:** Tether Limited es la entidad que emite Tether. Sin embargo, ha habido controversias y preocupaciones en torno a si Tether realmente mantiene reservas suficientes para respaldar todos los USDT en circulación. La empresa ha afirmado que cada token USDT está respaldado por un dólar en su cuenta, pero esto ha sido objeto de escrutinio y demandas legales.

**Otras Versiones:** Además del USDT respaldado por dólares estadounidenses, también existen versiones de Tether vinculadas a otras monedas fiduciarias, como el euro (EUR) y el yen japonés (JPY). Estas versiones buscan proporcionar estabilidad en otras monedas importantes.
'''

        st.write(resumen)
