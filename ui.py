import tkinter as tk
from query_handle import fetch_order_info
from imprimir import imprimir_espelho_por_chave


def buscar():
    chave_nfe = entrada_chave.get()
    if not chave_nfe:
        atualizar_mensagem("Por favor, insira uma CHAVE NFE.")
        return

    try:
        resultados = fetch_order_info(chave_nfe)

        if resultados:
            # Mapeamento dos campos que queremos exibir e suas posições na tupla de resultados
            mapeamento_campos = {
                "DOCUMENTO": 0,
                "NF": 1,
                "FORNECEDOR": 2,
                "HORA AGENDAMENTO": 4,
                "PORTAL": 5,
                "DOCA": 6,
                "TIPO PRODUTO": 7,
                "TIPO ENTREGA": 8,
                "COLECAO": 9,
                "SEMANA ENTRADA LOJA": 11,
                "MARCA": 14,
                "QTDE AGENDADA": 15
            }

            for campo_nome, indice_resultado in mapeamento_campos.items():
                if campo_nome in entradas:  # Verifica se o campo existe na UI
                    entradas[campo_nome].delete(0, tk.END)
                    valor = resultados[0][indice_resultado]
                    if valor is None:
                        valor = ""
                    entradas[campo_nome].insert(0, str(valor))
            atualizar_mensagem("Consulta realizada com sucesso!")
        else:
            atualizar_mensagem("Nenhum resultado encontrado para a chave fornecida.")
    except Exception as e:
        atualizar_mensagem(f"Erro ao buscar os dados: {e}")


def imprimir():
    chave_nfe = entrada_chave.get()
    if not chave_nfe:
        atualizar_mensagem("Por favor, insira uma CHAVE NFE antes de imprimir.")
        return

    try:
        sucesso = imprimir_espelho_por_chave(chave_nfe)
        if sucesso:
            atualizar_mensagem("Espelho gerado e enviado para a impressora.")
        else:
            atualizar_mensagem("Nenhum resultado para imprimir.")
    except Exception as e:
        atualizar_mensagem(f"Erro ao imprimir: {e}")


def limpar_campos():
    entrada_chave.delete(0, tk.END)
    for campo in entradas.values():
        campo.delete(0, tk.END)
    atualizar_mensagem("Pronto para uma nova consulta.")


def atualizar_mensagem(mensagem):
    label_mensagem.config(text=mensagem)


root = tk.Tk()
root.title("Consulta de Nota Fiscal - Entrada Loja")

label_chave = tk.Label(root, text="Insira a CHAVE NFE:")
label_chave.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_chave = tk.Entry(root, width=40)
entrada_chave.grid(row=0, column=1, padx=10, pady=5, sticky="w")

botao_buscar = tk.Button(root, text="Buscar", command=buscar)
botao_buscar.grid(row=0, column=2, padx=10, pady=5)

frame_campos = tk.Frame(root)
frame_campos.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

campos = [
    "DOCUMENTO", "NF", "FORNECEDOR",
    "HORA AGENDAMENTO", "PORTAL", "DOCA", "TIPO PRODUTO", "TIPO ENTREGA",
    "COLECAO", "SEMANA ENTRADA LOJA", "MARCA", "QTDE AGENDADA"
]

entradas = {}

for i, campo in enumerate(campos):
    label = tk.Label(frame_campos, text=campo + ":")
    label.grid(row=i // 2, column=(i % 2) * 2, padx=10, pady=5, sticky="e")
    entrada = tk.Entry(frame_campos, width=30)
    entrada.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=10, pady=5, sticky="w")
    entradas[campo] = entrada

botao_limpar = tk.Button(root, text="Próxima NF", command=limpar_campos)
botao_limpar.grid(row=2, column=0, pady=10)

botao_imprimir = tk.Button(root, text="Imprimir Espelho", command=imprimir)
botao_imprimir.grid(row=2, column=1, pady=10)

label_mensagem = tk.Label(root, text="", fg="red", anchor="w")
label_mensagem.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="w")

root.mainloop()
