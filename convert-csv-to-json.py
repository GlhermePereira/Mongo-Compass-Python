import csv
import json

def csv_para_json(arquivo_csv, arquivo_json):
    #abre o arquivo CSV e le o conteudo
    with open(arquivo_csv, encoding='utf-8') as csv_file:
        leitor_csv = csv.DictReader(csv_file)

        #converte cada linha do csv para um dicionario e adiciona a uma lista
        dados = [linha for linha in leitor_csv]

    #Escreve a lista de dicionarios em um arquivo JSOn
    with open(arquivo_json, 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)
    print(f"Arquivo JSON '{arquivo_json}' criado com sucesso!")

#exemplo de uso

#csv_para_json('full_grouped.csv', 'full_grouped.json')

csv_para_json('country_wise_latest.csv', 'country_wise_latest.json')
