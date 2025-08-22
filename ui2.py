import streamlit as st
from query_handle import fetch_order_info  # Certifique-se de que o arquivo query_handle.py está no mesmo diretório

# Função para buscar os dados
def buscar(chave_nfe):
    if not chave_nfe:
        st.error("Por favor, insira uma CHAVE NFE.")
        return None

    try:
        # Chama a função fetch_order_info passando a chave_nfe
        resultados = fetch_order_info(chave_nfe)
        return resultados
    except Exception as e:
        st.error(f"Erro ao buscar os dados: {e}")
        return None

# Interface Streamlit
st.title("Consulta de Nota Fiscal - Entrada Loja")

# Entrada para a CHAVE NFE
chave_nfe = st.text_input("Insira a CHAVE NFE:", "")

# Botão para buscar
if st.button("Buscar"):
    resultados = buscar(chave_nfe)
    if resultados:
        # Exibir os resultados
        st.success("Consulta realizada com sucesso!")
        col1, col2 = st.columns(2)
        campos = [
            "DOCUMENTO", "NF", "FORNECEDOR", "DATA AGENDAMENTO", 
            "HORA AGENDAMENTO", "PORTAL", "DOCA", "TIPO PRODUTO", "TIPO ENTREGA", 
            "COLECAO", "DATA ENTRADA LOJA", "SEMANA ENTRADA LOJA"
        ]
        for i, campo in enumerate(campos):
            with col1 if i % 2 == 0 else col2:
                st.text_input(campo, resultados[0][i], disabled=True)
    else:
        st.warning("Nenhum resultado encontrado para a chave fornecida.")

# Botão para limpar os campos
if st.button("Próxima NF"):
    st.experimental_rerun()

