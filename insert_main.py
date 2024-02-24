from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


# 1. Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastro Aditivo Nutritivo')
    
    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')
    
    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(aditivo_nutritivo)  # Adicionando o objeto AditivoNutritivo
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Aditivo Nutritivo cadastrado com sucesso')

 
# 2. Sabor
def insert_sabor() -> None:
    print('Cadastro Sabor')
    
    nome: str = input('Informe o nome do Sabor: ')
    
    sabor: Sabor = Sabor(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(sabor)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Sabor cadastrado com sucesso')


# 3. Tipo Embalagem
def insert_tipo_embalagem() -> None:
    print('Cadastro Tipo Embalagem')
    
    nome: str = input('Informe o nome do Tipo da embalagem: ')
    
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(tipo_embalagem)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto
    
    print('Tipo Embalagem cadastrado com sucesso')



# 4. Tipo Picole
def insert_tipo_picole() -> None:
    print('Cadastro Tipo Picole')
    
    nome: str = input('Informe o nome do Tipo Picole: ')
    
    tipo_picole: TipoPicole = TipoPicole(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(tipo_picole)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Tipo Picole cadastrado com sucesso')


# 5. Ingrediente
def insert_ingrediente() -> None:
    print('Cadastro Ingrediente')
    
    nome: str = input('Informe o nome do Ingrediente: ')
    
    ingrediente: Ingrediente = Ingrediente(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(ingrediente)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Ingrediente cadastrado com sucesso')
    
    
# 5. Conservante
def insert_conservante() -> None:
    print('Cadastro Conservante')
    
    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')
    
    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(conservante)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Conservante cadastrado com sucesso')


# 5. Revendedor
def insert_revendedor() -> None:
    print('Cadastro Revendedor')
    
    cnpj: str = input('Informe o cnpj do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')
    
    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(revendedor)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Revendedor cadastrado com sucesso')



if __name__ == '__main__':
    insert_aditivo_nutritivo()
    insert_sabor()
    insert_tipo_embalagem()
    insert_tipo_picole()
    insert_ingrediente()
    insert_conservante()
    insert_revendedor()
