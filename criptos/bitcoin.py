from funciones.fun import logo, grafico, consumo_bitcoin
import streamlit as st

def bitcoin():
    moneda = 'bitcoin'

    st.title('Bitcoin')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Bitcoin')
        resumen = '''Bitcoin (BTC) es la primera y más conocida criptomoneda, creada por una persona (o grupo de personas) bajo el seudónimo de Satoshi Nakamoto y lanzada en 2009. Bitcoin introdujo la tecnología blockchain y revolucionó la forma en que concebimos el dinero y las transacciones en línea.

**Tecnología Blockchain:** Bitcoin utiliza la tecnología blockchain para llevar un registro de todas las transacciones realizadas en su red. El blockchain es un libro de contabilidad público y descentralizado que garantiza la seguridad y la transparencia de las transacciones sin la necesidad de intermediarios.

**Suministro Limitado:** A diferencia de las monedas tradicionales, Bitcoin tiene un suministro máximo limitado de 21 millones de monedas. Esto se hace para evitar la inflación y establecer un límite en la cantidad de Bitcoin que se puede extraer.

**Minería y Prueba de Trabajo (PoW):** Bitcoin se crea a través de un proceso llamado minería, donde los mineros resuelven complejos problemas matemáticos para verificar y agregar transacciones al blockchain. Esto garantiza la seguridad y la integridad de la red. Bitcoin utiliza un algoritmo de prueba de trabajo (PoW) para este proceso.

**Inversión y Almacenamiento de Valor:** Bitcoin se ha convertido en una forma popular de inversión y almacenamiento de valor. Muchos inversores consideran que Bitcoin es una reserva de valor similar al oro digital y lo utilizan como un activo de refugio seguro.

**Adopción y Casos de Uso:** Bitcoin se utiliza para una variedad de casos de uso, que van desde transferencias internacionales y remesas hasta compras en línea y donaciones. También ha habido un aumento en la aceptación de Bitcoin por parte de comerciantes y empresas.

**Escalabilidad y Desarrollo:** Bitcoin ha enfrentado desafíos en términos de escalabilidad, lo que ha llevado a debates sobre cómo mejorar la velocidad y la capacidad de procesamiento de la red. Además, hay debates en curso sobre las posibles actualizaciones y mejoras en la red.

**Comunidad y Cambios:** La comunidad de Bitcoin es diversa y activa en la toma de decisiones sobre el desarrollo de la red. Los cambios y mejoras en el protocolo se determinan mediante un proceso de consenso que implica a los mineros, los desarrolladores y otros miembros de la comunidad.'''

        st.write(resumen)