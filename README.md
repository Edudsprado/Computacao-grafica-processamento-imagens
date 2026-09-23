# 📚 Revisão — Computação Gráfica e Processamento de Imagens

## 🎓 Disciplina

**Universidade de Cuiabá — UNIC**
**Curso:** Superior de Tecnologia em Análise e Desenvolvimento de Sistemas — ADS
**Disciplina:** Computação Gráfica e Processamento de Imagens
**Professor:** MSc. João Francisco Borba

---

## 📌 Sobre a atividade

Esta atividade tem como objetivo desenvolver a capacidade de **ler, interpretar, analisar, depurar e melhorar códigos existentes**, principalmente relacionados à representação e manipulação de imagens utilizando Python.

O processo utilizado durante os exercícios foi:

```text
Código original
      ↓
Análise
      ↓
Previsão do comportamento
      ↓
Execução
      ↓
Identificação do problema
      ↓
Classificação
      ↓
Explicação técnica
      ↓
Correção
      ↓
Verificação
```

A atividade trabalha conceitos fundamentais de processamento de imagens, como:

* Matrizes;
* Pixels;
* Índices;
* Intensidade de pixels;
* Dimensões de imagens;
* Coordenadas;
* Máscaras;
* Canais RGB;
* Manipulação de regiões;
* Visualização de imagens.

---

# 🧪 Exercício 1 — Primeiros conceitos

### Objetivo

Verificar se uma sequência de valores associada a uma imagem em tons de cinza está sendo interpretada corretamente.

### Problema encontrado

As funções `min()` e `max()` estavam utilizadas de forma invertida:

```python
print("Menor intensidade:", max(imagem))
print("Maior intensidade:", min(imagem))
```

### Correção

```python
print("Menor intensidade:", min(imagem))
print("Maior intensidade:", max(imagem))
```

### Conceito aprendido

Um erro lógico pode ocorrer mesmo quando o programa executa normalmente.

Nesse caso:

```text
min(imagem) → menor valor → 0
max(imagem) → maior valor → 255
```

O problema não era de sintaxe, mas de lógica.

---

# 🧪 Exercício 2 — Pixels e representação

### Objetivo

Verificar se os índices utilizados para desenhar uma cruz no centro de uma imagem estavam corretos.

A imagem possui dimensão:

```python
imagem = np.zeros((9, 9))
```

Os índices possíveis são:

```text
0 1 2 3 4 5 6 7 8
```

Portanto, o centro está no índice `4`.

### Problema encontrado

O código original utilizava:

```python
imagem[4, :] = 1
imagem[:, 5] = 1
```

A linha estava corretamente posicionada no índice `4`, mas a coluna utilizava o índice `5`.

Como consequência, a cruz ficava deslocada para a direita.

### Correção

```python
imagem[4, :] = 1
imagem[:, 4] = 1
```

### Conceito aprendido

A indexação em Python começa em `0`.

Em uma matriz `9 × 9`, o índice central é `4`.

Também foi identificada uma oportunidade de melhoria na visualização, como a utilização de uma grade:

```python
plt.grid()
```

Isso facilita a identificação das posições dos pixels.

---

# 🧪 Exercício 3 — Matrizes, coordenadas e círculo

### Objetivo

Verificar as dimensões da imagem, as coordenadas do centro e a máscara utilizada para desenhar um círculo.

A imagem criada possui:

```python
imagem = np.zeros((100, 120))
```

Portanto:

```text
100 linhas
120 colunas
```

### Problema encontrado

O código utilizava:

```python
centro_x = 50
centro_y = 50
```

O valor de `y` estava correto, mas o valor de `x` não correspondia ao centro horizontal da imagem.

Como existem 120 colunas:

```text
120 / 2 = 60
```

O centro deveria ser:

```python
centro_x = 60
centro_y = 50
```

### Melhoria

Em vez de utilizar valores fixos, o centro pode ser calculado automaticamente:

```python
centro_y = imagem.shape[0] // 2
centro_x = imagem.shape[1] // 2
```

### Conceito aprendido

O uso de valores calculados a partir das dimensões torna o código mais flexível e reduz a possibilidade de erros manuais.

---

# 🧪 Exercício 4 — Cores, canais e manipulação de pixels

### Objetivo

Verificar a representação RGB e as operações de preenchimento das regiões da imagem.

A imagem foi criada com:

```python
imagem = np.zeros((100, 100, 3), dtype=np.uint8)
```

O `3` representa os três canais RGB:

```text
0 → R → Red → Vermelho
1 → G → Green → Verde
2 → B → Blue → Azul
```

### Problema encontrado

O código original possuía:

```python
imagem[50:, :, 3] = 255
```

O índice `3` não existe porque os canais disponíveis são somente:

```text
0, 1 e 2
```

Isso provoca um erro de índice (`IndexError`).

### Correção

Para produzir uma imagem com metade superior vermelha e metade inferior azul:

```python
imagem[:50, :, 0] = 255
imagem[50:, :, 2] = 255
```

### Regiões da imagem

A divisão das regiões estava correta:

```python
imagem[:50, :]
```

representa as primeiras 50 linhas.

```python
imagem[50:, :]
```

representa as 50 linhas restantes.

Assim, a imagem de 100 linhas é dividida corretamente em duas metades.

### Melhoria de legibilidade

Comentários podem tornar o código mais fácil de compreender:

```python
# Canal R (vermelho)
imagem[:50, :, 0] = 255

# Canal B (azul)
imagem[50:, :, 2] = 255
```

---

# 🧠 Reflexão Final

## 1. Importância de interpretar o código

É importante interpretar o código antes de modificá-lo porque precisamos entender o que ele faz, identificar o motivo da alteração e analisar seu comportamento durante a execução. Dessa forma, podemos corrigir o problema sem modificar partes que já estão funcionando corretamente.

## 2. Erro de sintaxe × erro lógico

Um erro de sintaxe está relacionado à escrita do código de forma que não segue as regras da linguagem.

Um erro lógico ocorre quando o código consegue executar, mas a lógica utilizada está incorreta e produz um resultado diferente do esperado.

## 3. Importância dos índices

As imagens são representadas por matrizes de pixels. Os índices permitem localizar e manipular cada elemento dessa matriz.

Por isso, compreender os índices é fundamental para trabalhar corretamente com posições, regiões e canais de uma imagem.

## 4. Matriz, pixel e imagem

Os exercícios mostraram que a matriz é uma forma de representar e interpretar o funcionamento e a geração de uma imagem.

Cada posição da matriz corresponde a um pixel, e seus valores determinam características da imagem, como intensidade ou cor.

## 5. Uso da Inteligência Artificial

A Inteligência Artificial pode ajudar na análise dos códigos atuando como uma espécie de professor, orientando o aluno por meio de perguntas, explicações e direcionamentos, sem entregar imediatamente a resposta.

Dessa forma, o aluno é estimulado a desenvolver o pensamento crítico, analisar o código e encontrar os problemas por conta própria.

Com instruções adequadas, a IA também pode ajudar a identificar pontos que poderiam passar despercebidos pelo aluno.

---

# 📂 Organização do repositório

A sugestão de organização é manter cada exercício em seu próprio arquivo Python:

```text
/
├── README.md
├── exercicio_01.py
├── exercicio_02.py
├── exercicio_03.py
└── exercicio_04.py
```

Essa organização permite estudar e executar cada exercício individualmente, mantendo o material separado e fácil de consultar.

---

# 📚 Principais conceitos revisados

* Python;
* NumPy;
* Matplotlib;
* Matrizes;
* Pixels;
* Índices;
* `min()` e `max()`;
* `shape`;
* Coordenadas `x` e `y`;
* Máscaras booleanas;
* Representação em tons de cinza;
* RGB;
* Canais de cor;
* Fatiamento (`slicing`);
* Erros de índice;
* Erros lógicos;
* Legibilidade;
* Parametrização;
* Depuração e análise de código.

---

## 🎯 Método de aprendizado utilizado

Durante a atividade, o foco não foi apenas corrigir os códigos.

O objetivo foi desenvolver a capacidade de:

**Ler → Prever → Testar → Diagnosticar → Explicar → Corrigir → Verificar**

Esse processo ajuda a compreender o funcionamento do código antes de modificá-lo e desenvolve maior autonomia na resolução de problemas de programação.
