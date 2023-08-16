from funciones.fun import logo, grafico
import streamlit as st

def dash():
    moneda = 'dash'

    st.title('Dash')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Dash')
        resumen = '''Dash es una criptomoneda que se originó en 2014 como una bifurcación (fork) de Bitcoin. El nombre "Dash" proviene de la combinación de las palabras "Digital" y "Cash" (dinero digital en inglés), lo que refleja su objetivo de ser una forma de dinero digital que sea rápida, segura y privada.

**Privacidad y Seguridad:** Una de las características distintivas de Dash es su enfoque en la privacidad. Utiliza una tecnología de mezcla de transacciones llamada PrivateSend, que oculta la fuente, la cantidad y el destino de las transacciones. También ofrece una funcionalidad llamada InstantSend, que permite la confirmación rápida de transacciones.

**Gobernanza Descentralizada:** Dash implementa un sistema de gobernanza descentralizada llamado "Dash Governance", que permite a los titulares de Dash proponer y votar sobre cambios en el protocolo y en la financiación de proyectos. Esto permite una toma de decisiones más democrática y adaptable en comparación con algunas otras criptomonedas.

**Red de Nodos Maestros:** Dash utiliza una red de nodos maestros (masternodes) que desempeñan un papel importante en la funcionalidad de privacidad y gobernanza. Los nodos maestros ayudan a facilitar las transacciones privadas y respaldan el sistema de votación para la gobernanza.

**Escalabilidad y Velocidad:** Dash ha implementado mejoras en su protocolo para mejorar la escalabilidad y la velocidad de las transacciones. Su enfoque en la confirmación instantánea (InstantSend) permite transacciones rápidas y seguras.

**Adopción y Casos de Uso:** Dash se utiliza principalmente como una forma de pago digital en una variedad de establecimientos y servicios en línea. Se ha centrado en mercados con dificultades para acceder a servicios financieros tradicionales, como remesas internacionales y pagos en lugares con sistemas bancarios menos desarrollados.'''

        st.write(resumen)