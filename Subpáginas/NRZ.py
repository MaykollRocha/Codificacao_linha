import matplotlib.pyplot as plt
import streamlit as st


def grafico_NRZ(x, y, labels, high_level, low_level,bits):
    # Plotando o gráfico
    plt.figure(figsize=(8, 4))
    plt.step(x, y, where='post', color='#FF00FF', linewidth=2)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
    plt.ylim(low_level - 1, high_level + 1)  # Definindo limites do eixo y
    plt.xlim(-0.02, len(x)/2 - 1)  # Definindo limites do eixo x
    plt.title('NRZ Unipolar')
    plt.xlabel('Tempo')
    plt.ylabel('Nível de Tensão')
    # Configurando ticks e rótulos do eixo X
    plt.xticks(range(0, len(bits) + 1, 1), [''] + [' ' for bit in bits])
    plt.yticks([low_level, high_level], ['0', 'V'])  # Removendo os ticks do eixo Y
    for (x_pos, bit) in labels:
        plt.text(x_pos, high_level + 0.2, str(bit), ha='center')
    plt.grid(True)
    st.pyplot(plt)

def plot_nrz_unipolar(bits, ultimo=0):
    # Definindo os níveis de tensão para 1 e 0
    high_level = 1
    low_level = 0

    # Preparando os eixos do gráfico
    x = [0]
    y = [ultimo]
    labels = []

    # Gerando os pontos do sinal NRZ unipolar
    for i, bit in enumerate(bits):
        x.extend([i, i + 1])
        if bit == 1:
            y.extend([high_level, high_level])
        else:
            y.extend([low_level, low_level])

        # Adicionando texto do bit sobre a transição
        labels.append((i + 0.5, bit))

    # Plotando o gráfico
    grafico_NRZ(x, y, labels, high_level, low_level,bits)

def main():
    # Streamlit UI
    st.title('Gráfico NRZ Unipolar')
    st.text("<explicar mostrar codigo, dar exemplo de uso, se é bom ou ruim, etc.>")
    # Entrada do usuário para os bits
    st.text("Gerar apartir de sua entrada: ")
    bits_input = st.text_input('Digite a sequência de bits (por exemplo, 01001110):', '01001110')
    ultimo_bit = st.number_input('Último bit (0 ou 1):', min_value=0, max_value=1, value=0)

    # Convertendo a entrada do usuário para uma lista de inteiros
    bits = [int(bit) for bit in bits_input]

    # Gerando o gráfico
    plot_nrz_unipolar(bits, ultimo_bit)
    
    if st.button('Voltar para a página principal'):
        st.session_state.page = 'main'