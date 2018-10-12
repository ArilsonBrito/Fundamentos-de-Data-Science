# coding: utf-8

# Começando com os imports
import csv
import sys
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
data_list = []
try:
    with open("chicago.csv", "r") as file_read:
        reader = csv.reader(file_read)
        data_list = list(reader)
        print("Ok!")
except Exception as ex:
    print("Ocorreu um erro inexperado na leitura do arquivo!", ex)
    sys.exit()

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

def column_to_list(data, index) -> list:
    """
    Função retornar a lista de uma coluna específica do csv.

    Argumentos:
      data: A lista de gêneros.
      index: Índice da coluna(poição).

    Retorna:
      Retorna uma lista com os valores da coluna solicitada.

    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for item in data:
        column_list.append(item[index])
    return column_list


def count_for_gender(data, gender) -> int:
    """
    Função para conta a quntidade  de ocorrências
    de gêneros na lista.

    Argumentos:
      data: A lista de gêneros.
      gender: O gênero que se deseja contar (M - Masculino, F - Feminino).

    Retorna:
      Quantidade total do gênero informado.

    """
    data = column_to_list(data_list, -2)
    count = 0
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for item in data:
        if (gender == "" or gender == None):
            if (item == "" or item == None):
                count += 1
        elif (item.startswith(gender)):
            count += 1

    return count
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
male = count_for_gender(data_list,"M")
female = count_for_gender(data_list,"F")
undefined = count_for_gender(data_list,"")

# Verificando o resultado
print("\n\nTAREFA 4: Imprimindo quantos masculinos, femininos e não informados nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female, "\nNão informado: ", undefined)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784 and undefined == 316867, "TAREFA 4: A conta não bate."
# -----------------------------------------------------


input("\n\nAperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data) -> list:
    """
    Função para contar as ocorrências de gêneros.

    Argumentos:
      data: A lista de informações do aquivo csv.

    Retorna:
        Retorna uma lista com o total de ocorrências para cada gêneros válido.

    """
    #recuperando apenas a colnuna de gêneros
    data = column_to_list(data, -2)
    male = count_for_gender(data,"M")
    female = count_for_gender(data,"F")
    undefined = count_for_gender(data,"")
    return [male, female, undefined]


print("\n\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 3, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784 and count_gender(data_list)[2] == 316867, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female", ""]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("\n\nAperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\n\nTAREFA 7: Verifique o gráfico!")

input("\n\nAperte Enter para finalizar...")
