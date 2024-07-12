import matplotlib.pyplot as plt


def grafico_auxilio():
    x = [0, 1, 1, 2]
    y = [-1, -1, 1, 1]

    fig = plt.figure(figsize=(2, 2))

    # Desenhando o gráfico de passos
    plt.step(x, y, where='post', color='#FF00FF', linewidth=2)

    # Linha horizontal em y=0
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)

    # Definindo limites dos eixos
    plt.ylim(-1.5, 1.5)
    plt.xlim(-0.03, len(x)/2)

    # Rótulos dos eixos
    plt.xlabel('Tempo')
    plt.ylabel('Nível de Tensão')

    # Área destacada com quadrado
    plt.fill_between(x=[0.25, 0.75], y1=-1.25, y2=-0.75, color='red', alpha=0.3, label='Highlighted region')
    plt.fill_between(x=[1.25, 1.75], y1=0.75, y2=1.25, color='red', alpha=0.3, label='Highlighted region')
    # Configurando ticks e rótulos do eixo X
    plt.xticks(range(0, 2, 1))
    plt.yticks([-1, 0, 1],['-V','0','V'])
    return fig