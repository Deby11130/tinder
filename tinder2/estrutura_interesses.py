database = {} #um dicionário, que tem a chave interesses para o controle
#dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
#voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
#do seu código para usar essa váriavel
database['interesses'] = { 
    100: [101, 102, 103],
    200: [100]
}
database['PESSOA'] = [] #esse voce só faz se quiser guardar nessa lista os dicionários das pessoas

#em todo esse codigo que estou compartilhando, as variaveis interessado, alvo de interesse, pessoa, pessoa1 e pessoa2 sao sempre IDs de pessoas

class NotFoundError(Exception):
    pass
class IncompatibleError(Exception):
    pass

def todas_as_pessoas():
    return database['PESSOA']

def adiciona_pessoa(dic_pessoa):
    database['PESSOA'].append(dic_pessoa)
    database['interesses'][dic_pessoa['id']] = [] 


def localiza_pessoa(id_pessoa):
    list_pessoa = database['PESSOA']
    for pessoa in list_pessoa:
        if pessoa['id'] == id_pessoa:
            return pessoa
    raise NotFoundError

def reseta():
    database['PESSOA'] = []



def adiciona_interesse(id_interessado, id_alvo_de_interesse):
        dic_interessado = localiza_pessoa(id_interessado)
        dic_alvo = localiza_pessoa(id_alvo_de_interesse)
        if 'sexo' in dic_interessado:
            if dic_alvo['sexo'] not in  dic_interessado['buscando']:
                raise IncompatibleError
        database['interesses'][id_interessado].append(id_alvo_de_interesse)
    

def consulta_interesses(id_interessado):
    return database['interesses'][id_interessado]

def remove_interesse(id_interessado,id_alvo_de_interesse):
    lista_interessado = database['interesses']
    if id_interessado in lista_interessado:
        lista_interessado[id_interessado].remove(id_alvo_de_interesse)
    
    

#essa funcao diz se o 1 e o 2 tem match. (retorna True se eles tem, False se não)
#ela não está testada, só existe para fazer aquecimento para a próxima
def verifica_match(id1,id2):
    localiza_pessoa(id1)
    localiza_pessoa(id2)
    if id1 in database['interesses'][id2]:
        return True
    return False
       
      
def lista_matches(id_pessoa):
    localiza_pessoa(id_pessoa)
    if id_pessoa in database['interesses']:
        if database['interesses'][id_pessoa] == []:
            return []
        lista = [id_match for id_match in database['interesses'][id_pessoa] if verifica_match(id_pessoa, id_match)]
        return lista





