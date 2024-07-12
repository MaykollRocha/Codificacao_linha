import streamlit as st

from Subpáginas.auxilio import grafico_auxilio as aux
from Subpáginas.NRZ import main as nrz_main


def main_page():
    st.title('Codificação de Linha')
    st.markdown("""
            ### CONVERSÃO DIGITAL-DIGITAL  
            
            ## Codificação de Linha  
            Codificação de linha é o processo de conversão de dados digitais em sinais digitais. Partimos do pressuposto de que os dados são armazenados na memória do computador como seqüências de bits. A codificação de linha converte uma seqüência de bits em um sinal digital. No emissor, os dados digitais são codificados em um sinal digital; no receptor, os dados digitais são recriados, reconvertendo-se o sinal digita
            """)
    st.markdown("""
            ## Características
            *elemento de dados*:  
                O objetivo é transmitir elementos de dados. Um elemento de dados é a menor entidade capaz de representar uma informação: trata-sedo bit  
                
            *elemento de sinal*:  
                Elementos de sinal transportam elementos de dados. Um elemento de sinal é a menor unidade (em termos de tempo) de um sinal digital.
            
            Em suma os elementos de dados são transportados e os elementos de sinal são os portadores.
            """)
    st.markdown(r"""
                Definir a razão r, que é o número de elementos de dados transportados pelos elementos de sinal
             """)
    st.latex(r''' r = \frac{\text{elemento de dados}}{\text{elemento de sinal}} ''')
    st.image(".\img\grafico_representação de R.png", caption="Um elemento de dados por um elemento de sinal (r = 1)")
    
    st.markdown("""
                Na parte da figura, um elemento de dados é transportado por um elemento de sinal (r = 1).
                Mas isso muda dependendo do tipo de gráfico que será escrito em cada sesão de dados eu provo 
                qual o valor de r dele, mas partindo desse pré visão mais básica já sabemos como ver e a razão dado o sinal.
                """)
    st.write("""
            ## Métodos de Codificação de Linha
            De forma resumida, dividimos os métodos de codificação de linha em cinco grandes categorias e existem vários métodos dentro de cada categoria.
            """)
    st.image('.\img\Métodos de codificação de linha.png', caption='Métodos de codificação de linha')
    
    
    
    st.subheader("Unipolar")
    st.markdown("<Descrissão de um gráfico Unipolar>")
    if st.button('NRZ'):
        st.session_state.page = 'nrz'
        
    st.subheader("Polar")
    if st.button('NRZ-L e NRZ-I'):
        st.session_state.page = '_'
    if st.button('RZ'):
        st.session_state.page = '_' 
    if st.button('Manchester e Manchester Diferencial'):
        st.session_state.page = '_'
        
    st.subheader("Bipolar")
    if st.button('AMI e Peseudonário'):
        st.session_state.page = '_'
    
    st.subheader("Multinível")
    if st.button('2B/1Q'):
        st.session_state.page = '_'
    if st.button('8B/6T'):
        st.session_state.page = '_'
    if st.button('4D-PAM5'):
        st.session_state.page = '_'
    
    st.subheader("Multitransição")
    if st.button('MLT-3'):
        st.session_state.page = '_'
# Defina o estado da página se não estiver definido
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Controle de navegação
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'nrz':
    nrz_main()
else:
    main_page()
    st.write("""
             Ainda está em desenvolvimento
             """)

