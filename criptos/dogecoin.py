from funciones.fun import logo, grafico
import streamlit as st

def dogecoin():
    moneda = 'dogecoin'

    st.title('Dogecoin')
    st.markdown('***')
    
    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Dogecoin')
        resumen = '''
Dogecoin es una criptomoneda que se originó en 2013 como una "broma" o parodia basada en el popular meme de un perro Shiba Inu llamado "Doge". Sin embargo, a pesar de sus orígenes humorísticos, Dogecoin ha ganado una comunidad leal y se ha convertido en una criptomoneda con una base de usuarios significativa.

**Mascota y Comunidad:** Dogecoin se basa en el meme "Doge", que presenta la imagen de un perro Shiba Inu acompañado de texto en inglés mal escrito en estilo cómico. Esto le da a la criptomoneda una atmósfera relajada y amigable, lo que ha atraído a una comunidad diversa y entusiasta en línea.

**Uso y Adopción:** Aunque Dogecoin comenzó como una broma, ha encontrado varios casos de uso reales. Se utiliza a menudo para propinas en línea y donaciones caritativas. También ha ganado cierta aceptación en la industria de los juegos y se ha utilizado para recaudar fondos para causas humanitarias.

**Suministro Ilimitado:** A diferencia de Bitcoin, que tiene un suministro máximo limitado de 21 millones de monedas, Dogecoin tiene un suministro ilimitado. Originalmente, se emitió un gran suministro inicial y se estableció una tasa de emisión continua. Esto ha llevado a críticas y debates sobre la sostenibilidad a largo plazo de la criptomoneda.

**Tecnología y Red:** Dogecoin se basa en una bifurcación (fork) de Litecoin, que a su vez se basa en Bitcoin. Utiliza un algoritmo de prueba de trabajo (PoW) llamado Scrypt. A lo largo de los años, ha habido discusiones sobre la mejora de la red y la adopción de nuevas tecnologías.

'''

        st.write(resumen)
