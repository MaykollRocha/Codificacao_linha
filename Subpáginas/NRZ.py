import matplotlib.pyplot as plt
import streamlit as st


def grafico_NRZ(x, y, labels, high_level, low_level, bits):
    """
    Plota um gráfico de sinal NRZ Unipolar utilizando os valores de tensão e bits fornecidos.

    Args:
        x (list or numpy.ndarray): Eixo x (tempo) do gráfico, representando os pontos de transição do sinal.
        y (list or numpy.ndarray): Eixo y (níveis de tensão), indicando os valores de tensão para cada bit.
        labels (list of tuples): Lista de tuplas contendo a posição no eixo x e o valor do bit a ser exibido como rótulo.
                                  Exemplo: [(x_pos, bit), ...], onde `x_pos` é a posição no eixo x e `bit` é o valor binário.
        high_level (float or int): Valor da tensão que representa um bit '1' (nível alto).
                                   Exemplo: 5 (representando 5V).
        low_level (float or int): Valor da tensão que representa um bit '0' (nível baixo).
                                  Geralmente é 0V.
        bits (list): Lista contendo a sequência de bits (0s e 1s) que será transmitida pelo sinal.
                     Exemplo: [1, 0, 1, 0, 1]

    Returns:
        None: A função plota o gráfico diretamente.
    """
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
    st.markdown("""
O **NRZ Unipolar** (Non-Return to Zero) é um esquema de codificação de linha amplamente utilizado em sistemas de comunicação digital para transmitir dados binários. Ele é chamado de **Unipolar** porque usa apenas um nível de tensão (positivo ou zero), e **NRZ** porque o sinal não retorna ao valor zero entre os bits. 

### Explicação
No esquema NRZ Unipolar:
- Um bit '1' é representado por uma tensão positiva.
- Um bit '0' é representado pela ausência de tensão (ou seja, zero).

### Características
- **Baixa complexidade:** O NRZ Unipolar é fácil de implementar e requer apenas um nível de tensão, o que o torna barato em termos de hardware.
- **Baixa eficiência:** Um problema com o NRZ Unipolar é que ele não tem uma maneira eficaz de sincronizar o transmissor e o receptor, especialmente quando uma longa sequência de '0's é transmitida, o que pode fazer com que o sinal fique constante por muito tempo, perdendo a referência de sincronização.
- **Falta de componentes de alta frequência:** Como o sinal não muda durante uma sequência de '0's, ele pode não ter componentes de alta frequência suficientes para sincronizar um receptor.


### Vantagens e Desvantagens

#### **Vantagens**:
- **Simples de implementar**: Como ele usa apenas um nível de tensão, a implementação de hardware é simples.
- **Baixo custo**: Devido à simplicidade do esquema de codificação, o custo de implementação também é baixo.

#### **Desvantagens**:
- **Problema de sincronização**: Como mencionado, longas sequências de '0's podem causar perda de sincronização entre transmissor e receptor.
- **Baixa eficiência espectral**: O esquema NRZ Unipolar não possui componentes de alta frequência suficientes, o que pode levar à necessidade de canais de transmissão mais largos para compensar.

### Conclusão
O NRZ Unipolar é uma técnica simples de codificação digital, mas não é adequada para sistemas que exigem alta eficiência e sincronização robusta. Em geral, outros esquemas como o **NRZ Polar** ou o **Manchester** são mais eficientes para transmitir dados com maior robustez.
""")
    st.code("""
def grafico_NRZ(x, y, labels, high_level, low_level, bits):
    '''
    Plota um gráfico de sinal NRZ Unipolar utilizando os valores de tensão e bits fornecidos.

    Args:
        x (list or numpy.ndarray): Eixo x (tempo) do gráfico, representando os pontos de transição do sinal.
        y (list or numpy.ndarray): Eixo y (níveis de tensão), indicando os valores de tensão para cada bit.
        labels (list of tuples): Lista de tuplas contendo a posição no eixo x e o valor do bit a ser exibido como rótulo.
                                  Exemplo: [(x_pos, bit), ...], onde `x_pos` é a posição no eixo x e `bit` é o valor binário.
        high_level (float or int): Valor da tensão que representa um bit '1' (nível alto).
                                   Exemplo: 5 (representando 5V).
        low_level (float or int): Valor da tensão que representa um bit '0' (nível baixo).
                                  Geralmente é 0V.
        bits (list): Lista contendo a sequência de bits (0s e 1s) que será transmitida pelo sinal.
                     Exemplo: [1, 0, 1, 0, 1]

    Returns:
        None: A função plota o gráfico diretamente.
    '''
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
            
            """)
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