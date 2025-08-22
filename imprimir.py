from espelho import gerar_espelho, imprimir_espelho
from query_handle import fetch_order_info


def imprimir_espelho_por_chave(chave):
    resultado = fetch_order_info(chave)
    if not resultado:
        print("Nenhum resultado encontrado para a chave informada.")
        return False

    row = resultado[0]

    # Ajuste os índices abaixo conforme a sua query
    # Com a remoção de DATA_AGENDAMENTO, os índices mudaram.
    # Se a query agora retorna 15 colunas (len=15),
    # os índices válidos vão de 0 a 14.
    # PRODUTO (referencia) era 13, depois 12, agora é 12 (se TIPO_ENTREGA permaneceu antes)
    # TIPO_ENTREGA (canal) era 8, depois 7, agora é 7
    # NUMERO_SEMANA (semana) era 12, depois 11, agora é 11
    # MARCA era 16, depois 15, agora é 14 (o último índice válido para len=15)

    referencia = str(row[12]) # PRODUTO
    canal = str(row[7])       # TIPO_ENTREGA
    semana = str(row[11])     # NUMERO_SEMANA
    marca = str(row[14])      # MARCA (AJUSTADO DE 15 PARA 14)

    tmp_doc = gerar_espelho(referencia, canal, semana, marca)
    imprimir_espelho(tmp_doc)
    return True