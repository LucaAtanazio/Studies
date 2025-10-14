import streamlit as st

class Pilha:
    def __init__(self):
        self.itens = []
    
    def vazia(self):
        return len(self.itens) == 0
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.vazia():
            return self.itens.pop()
        return None 
    
    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        return None
    
    def tamanho(self):
        return len(self.itens)
    
    def mostrar_pilha(self):
        return self.itens.copy()

st.set_page_config(page_title="Visualizador de Pilha", page_icon="📚")

st.title("📚 Visualizador Interativo de Pilha (Stack)")

if 'pilha' not in st.session_state:
    st.session_state.pilha = Pilha()

with st.sidebar:
    st.header("Operações")
    operacao = st.radio(
        "Selecione a operação:",
        ("Push (Inserir)", "Pop (Remover)", "Visualizar")
    )


if operacao == "Push (Inserir)":
    st.subheader("Inserir Elemento na Pilha")
    elemento = st.text_input("Digite o elemento a ser inserido:")
    
    if st.button("Inserir (Push)"):
        if elemento:
            st.session_state.pilha.push(elemento)
            st.success(f"Elemento '{elemento}' inserido com sucesso!")
        else:
            st.warning("Por favor, digite um elemento para inserir.")

elif operacao == "Pop (Remover)":
    st.subheader("Remover Elemento do Topo")
    
    if st.session_state.pilha.vazia():
        st.warning("A pilha está vazia! Não há elementos para remover.")
    else:
        elemento_removido = st.session_state.pilha.topo()
        if st.button("Remover (Pop)"):
            elemento_removido = st.session_state.pilha.pop()
            st.success(f"Elemento '{elemento_removido}' removido com sucesso!")

else:
    st.subheader("Visualização da Pilha")
    
    if st.session_state.pilha.vazia():
        st.info("A pilha está vazia.")
    else:
        st.write("**Topo da Pilha**")
        st.code(f"{st.session_state.pilha.topo()}")
        
        st.write("**Conteúdo da Pilha (do topo para a base)**")
        
        # Exibe a pilha verticalmente com estilo
        pilha_display = st.session_state.pilha.mostrar_pilha()[::-1]  # Inverte para mostrar do topo para base
        
        for i, item in enumerate(pilha_display):
            if i == 0:
                st.markdown(f"<div style='background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; margin: 5px 0;'>Topo: {item}</div>", 
                            unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color: #f1f1f1; padding: 10px; border-radius: 5px; margin: 5px 0;'>{item}</div>", 
                            unsafe_allow_html=True)
        
        st.write(f"**Tamanho da Pilha:** {st.session_state.pilha.tamanho()}")

st.markdown("---")
st.caption("Desenvolvido para demonstração de estruturas de dados com Streamlit")