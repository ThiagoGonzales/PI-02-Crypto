from funciones.fun import logo, grafico
import streamlit as st

def zcash():
    moneda = 'zcash'

    st.title('Zcash')
    st.markdown('***')

    logo(moneda, 150)
    grafico(moneda)

    if st.button('Resumen'):
        st.markdown('### Resumen del Zcash')
        resumen = '''
Zcash (ZEC) es una criptomoneda que se lanzó en 2016 con un enfoque especial en la privacidad y la confidencialidad de las transacciones. A diferencia de Bitcoin y muchas otras criptomonedas que ofrecen transacciones públicas y transparentes en un libro de contabilidad público (blockchain), Zcash utiliza tecnologías avanzadas para permitir transacciones privadas y seguras.

**Privacidad y Confidencialidad:** La característica distintiva de Zcash es su enfoque en la privacidad. Utiliza una tecnología llamada zk-SNARKs (corto para "Zero-Knowledge Succinct Non-Interactive Argument of Knowledge") que permite a los usuarios realizar transacciones totalmente privadas. Con zk-SNARKs, es posible demostrar la validez de una transacción sin revelar los detalles específicos de dicha transacción.

**Transacciones Blindadas:** En Zcash, las transacciones se pueden realizar de dos maneras: "transparentes" o "blindadas". Las transacciones transparentes funcionan de manera similar a Bitcoin y son visibles en el blockchain. Las transacciones blindadas, en cambio, son completamente privadas y no revelan ninguna información confidencial.

**Descentralización y Minería:** Zcash utiliza un algoritmo de prueba de trabajo (PoW) llamado Equihash para garantizar la seguridad de la red y la emisión de nuevas monedas. Aunque la minería de Zcash es accesible para cualquier persona con un equipo de minería, también ha habido preocupaciones sobre la centralización de la minería en ciertas empresas y grupos.

**Uso y Casos de Uso:** Zcash se utiliza en situaciones en las que la privacidad es especialmente importante, como en transacciones financieras confidenciales y para proteger la identidad de los usuarios en la cadena de bloques. También se ha utilizado en la creación de tokens no fungibles (NFT) privados.
        '''

        st.write(resumen)