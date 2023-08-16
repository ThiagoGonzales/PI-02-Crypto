from funciones.fun import logo, grafico
import streamlit as st

def ripple():
    moneda = 'ripple'

    st.title('Ripple')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Ripple')
        resumen = '''
Ripple es tanto una plataforma de pagos globales como una criptomoneda que busca habilitar transacciones rápidas y eficientes, así como soluciones para la transferencia de valor a nivel internacional. La criptomoneda asociada con la plataforma Ripple se llama XRP.

**Red de Pagos Ripple:** Ripple se diferencia de muchas otras criptomonedas en que su enfoque principal es facilitar las transacciones internacionales y la transferencia de valor entre diferentes monedas y sistemas financieros. La plataforma RippleNet se utiliza para conectar bancos, instituciones financieras y proveedores de pagos en una red global para facilitar pagos rápidos y económicos.

**Criptomoneda XRP:** XRP es la criptomoneda nativa de la plataforma Ripple. Aunque se puede utilizar como medio de intercambio y para el pago de tarifas de transacción en la red, también ha sido diseñada para agilizar las transacciones internacionales. XRP es preminado, lo que significa que todos los XRP ya han sido creados y están en circulación.

**Protocolo de Consenso:** Ripple utiliza un protocolo de consenso llamado Ripple Consensus Algorithm (RCA), también conocido como Ripple Protocol (RPCA). A diferencia de otras cadenas de bloques que utilizan minería o validadores basados en pruebas de trabajo (PoW) o pruebas de participación (PoS), el protocolo de Ripple se basa en un proceso de consenso que involucra a los nodos de la red para validar transacciones.

**Adopción en la Industria Financiera:** Ripple ha colaborado con una serie de instituciones financieras y bancos en todo el mundo para explorar formas de mejorar la eficiencia de las transacciones internacionales y la liquidación de pagos transfronterizos. Su solución xCurrent se centra en la liquidación de pagos y la mensajería financiera, mientras que xRapid utiliza XRP como puente de liquidez para las transacciones.

**Regulación y Controversia:** Ripple y XRP han enfrentado controversias y desafíos regulatorios en relación con si XRP debe considerarse una seguridad. La Comisión de Valores y Bolsa de los Estados Unidos (SEC) ha llevado a cabo acciones legales contra Ripple Labs por presuntas ventas no registradas de XRP como valores.
'''

        st.write(resumen)