from funciones.fun import logo, grafico
import streamlit as st

def monero():
    moneda = 'monero'

    st.title('Monero')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Monero')
        resumen = '''
Monero (XMR) es una criptomoneda centrada en la privacidad que se lanzó en 2014 con el objetivo de ofrecer transacciones completamente anónimas y no rastreables. A diferencia de muchas otras criptomonedas, Monero se enfoca en ocultar tanto las direcciones de los remitentes como los destinatarios, así como las cantidades involucradas en las transacciones.

**Privacidad y Fungibilidad:** Monero se basa en tecnologías de privacidad avanzadas, como la firma de anillo y los denominados "confidencial transactions", que ocultan los detalles específicos de las transacciones mientras mantienen la capacidad de verificar su validez. Esto busca asegurar que todas las monedas de Monero sean fungibles, lo que significa que cada unidad de XMR es indistinguible de otra, lo que ayuda a prevenir el rastreo y el análisis de transacciones.

**Minado Equitativo:** Monero utiliza un algoritmo de prueba de trabajo llamado RandomX, diseñado para ser resistente a la minería con hardware especializado y para permitir la participación más amplia posible de mineros utilizando CPU y GPU estándar de computadoras personales.

**Comunidad y Uso:** Monero ha ganado una comunidad leal que valora su enfoque en la privacidad y la fungibilidad. La criptomoneda se utiliza en casos en los que la privacidad es especialmente importante, como en donaciones a organizaciones benéficas y transacciones comerciales que requieren un alto grado de confidencialidad.

**Escalabilidad y Desarrollo:** Monero ha trabajado para mejorar la escalabilidad y la eficiencia de su red. El proyecto sigue en constante desarrollo y evolución para abordar desafíos técnicos y mejorar su funcionalidad.

**Regulación y Controversia:** Dado su enfoque en la privacidad, Monero ha enfrentado debates sobre la regulación gubernamental y posibles usos ilícitos. Algunas casas de cambio y servicios financieros han optado por no ofrecer soporte para Monero debido a preocupaciones regulatorias.
'''

        st.write(resumen)