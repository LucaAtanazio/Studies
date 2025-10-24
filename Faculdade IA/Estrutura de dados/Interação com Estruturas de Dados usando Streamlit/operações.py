# Importa o módulo do Streamlit para criar a interface web
import streamlit as st # type: ignore

# Título da aplicação
st.title("Calculadora")

# Campo de entrada do primeiro número (tipo float, valor padrão = 0.0)
numero1 = st.number_input("Digite o primeiro número:", value=0.0)

# Campo de entrada do segundo número
numero2 = st.number_input("Digite o segundo número:", value=0.0)

# Menu suspenso para o usuário escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Somar", "Multiplicar", "Dividir")  # Opções disponíveis
)

# Botão para calcular o resultado
if st.button("Calcular"):
    # Verifica qual operação foi escolhida
    if operacao == "Somar":
        resultado = numero1 + numero2
        # Exibe o resultado da soma
        st.success(f"A soma de {numero1} + {numero2} é {resultado}")

    elif operacao == "Multiplicar":
        resultado = numero1 * numero2
        # Exibe o resultado da multiplicação
        st.success(f"A multiplicação de {numero1} * {numero2} é {resultado}")

    elif operacao == "Dividir":
        # Verifica se o segundo número é diferente de zero
        if numero2 != 0:
            resultado = numero1 / numero2
            # Exibe o resultado da divisão
            st.success(f"A divisão de {numero1} / {numero2} é {resultado}")
        else:
            # Mostra uma mensagem de erro se tentar dividir por zero
            st.error("Erro: não é possível dividir por zero.")
