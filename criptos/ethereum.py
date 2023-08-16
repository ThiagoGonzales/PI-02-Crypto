from funciones.fun import logo, grafico
import streamlit as st

def ethereum():
    moneda = 'ethereum'

    st.title('Ethereum')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Ethereum')
        resumen = '''
Ethereum es una plataforma blockchain y una criptomoneda que fue propuesta en 2013 y lanzada en 2015 por el desarrollador ruso-canadiense Vitalik Buterin. Se diseñó como una plataforma más versátil que Bitcoin, con un enfoque en la ejecución de contratos inteligentes y la creación de aplicaciones descentralizadas (dApps).

**Contratos Inteligentes:** Ethereum introdujo la idea de los contratos inteligentes, que son programas informáticos que se ejecutan automáticamente cuando se cumplen ciertas condiciones predefinidas. Estos contratos inteligentes permiten la automatización de acuerdos y transacciones sin intermediarios.

**Plataforma para Aplicaciones Descentralizadas (dApps):** Ethereum proporciona una plataforma para el desarrollo y la ejecución de aplicaciones descentralizadas. Esto ha dado lugar a una amplia gama de proyectos que abarcan desde finanzas descentralizadas (DeFi) hasta juegos, identidad digital y más.

**Token Nativo (Ether - ETH):** La criptomoneda nativa de la red Ethereum se llama Ether (ETH). Además de utilizarse como medio de intercambio, el Ether es necesario para pagar las tarifas de transacción y para participar en la ejecución de contratos inteligentes en la red.

**Actualización a Ethereum 2.0:** Ethereum ha estado en proceso de transición de un mecanismo de consenso de Prueba de Trabajo (PoW) a un mecanismo de consenso de Prueba de Participación (PoS) a través de la actualización Ethereum 2.0. Esta actualización tiene como objetivo mejorar la escalabilidad y la eficiencia energética de la red.

**Ecosistema y Adopción:** Ethereum ha creado un próspero ecosistema de desarrolladores, proyectos y empresas que construyen sobre su plataforma. La red ha sido fundamental en el auge de las finanzas descentralizadas (DeFi) y ha facilitado la creación de tokens no fungibles (NFT) para obras de arte y coleccionables digitales.

**Desafíos y Competencia:** A pesar de su éxito, Ethereum ha enfrentado desafíos en términos de escalabilidad y tarifas de transacción durante períodos de alta demanda. Además, ha surgido competencia de otras plataformas blockchain que también buscan abordar estos problemas.
'''

        st.write(resumen)   