class Fato:
    def __init__(self, nome, atributo, valor, veracidade):
        self.nome = nome
        self.atributo = atributo
        self.valor = valor
        self.veracidade = veracidade
    
    #imprime o fato
    def printFato(self):
        print(self.nome)
        print(self.atributo)
        print(self.valor)
        print(self.veracidade)
      
#imprime uma lista de Fatos
def PrintLista(Lista):
    for i in Lista:
        i.printFato()
        print()
    

#retorna os fatos vigentes sobre as entidades Fato na lista de input
def fatos_vigentes(lista):
    lista_verdadeira = []
    
    for a, cur in enumerate(lista):
        nome = cur.nome
        atributo = cur.atributo
        valor = cur.valor
        veracidade = cur.veracidade
            
        element_found = False
        for b, cur2 in enumerate(lista_verdadeira):
            #substitui o endereco por um novo verdadeiro
            if cur2.nome == nome and cur2.atributo == atributo and cur2.atributo == 'endereço' and cur2.veracidade == True:
                lista_verdadeira[b] = lista[a]
                element_found = True
            #deleta um telefone antigo que nao e mais verdadeiro   
            if cur2.nome == nome and cur2.atributo == atributo and cur2.atributo == 'telefone' and veracidade == False:
                del lista_verdadeira[b]
                element_found = True
        
        #se nao foi encontrado nenhum substituto na lista de output, appenda        
        if element_found == False and veracidade == True: 
            lista_verdadeira.append(cur)
    
    return lista_verdadeira



#Teste unitario da funcao de fatos_vigentes
def fatos_vigentes_unit_test():
    facts = [
    Fato('gabriel', 'endereço', 'av rio branco, 109', True),
    Fato('joão', 'endereço', 'rua alice, 10', True),
    Fato('joão', 'endereço', 'rua bob, 88', True),
    Fato('joão', 'telefone', '234-5678', True),
    Fato('joão', 'telefone', '91234-5555', True),
    Fato('joão', 'telefone', '234-5678', False),
    Fato('gabriel', 'telefone', '98888-1111', True),
    Fato('gabriel', 'telefone', '56789-1010', True),
    ]

    lista_verdadeira = fatos_vigentes(facts)	
    print('\nTeste unitario 1: ')
    PrintLista(lista_verdadeira)
   
def fatos_vigentes_unit_test2():
    facts = [
    Fato('gabriel', 'endereço', 'av rio branco, 109', True),
    Fato('joão', 'endereço', 'rua alice, 10', True),
    Fato('joão', 'endereço', 'rua bob, 88', True),
    Fato('joão', 'telefone', '234-5678', True),
    Fato('joão', 'telefone', '91234-5555', True),
    Fato('joão', 'telefone', '234-5678', False),
    Fato('gabriel', 'telefone', '98888-1111', True),
    Fato('gabriel', 'telefone', '56789-1010', True),
    Fato('joão', 'telefone', '91234-5555', False),
    Fato('joão', 'endereço', 'rua terceira, 99', True),

    ]

    lista_verdadeira = fatos_vigentes(facts)	
    print('\nTeste unitario 2: ')
    PrintLista(lista_verdadeira)
   
fatos_vigentes_unit_test()   
fatos_vigentes_unit_test2()   
