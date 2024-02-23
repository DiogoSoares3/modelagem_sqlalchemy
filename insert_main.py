from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo


# 1. Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastro Aditivo Nutritivo')
    
    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')
    
    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(an)  # Adicionando o objeto AditivoNutritivo
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Aditivo Nutritivo cadastrado com sucesso')
    print(f'ID: {an.id}')
    print(f'Data de criação: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Fórmula química: {an.formula_quimica}')



if __name__ == '__main__':
    insert_aditivo_nutritivo()
