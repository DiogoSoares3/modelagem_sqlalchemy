from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


# 1. Aditivo Nutritivo
def insert_aditivo_nutritivo() -> AditivoNutritivo:
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
    
    return aditivo_nutritivo

 
# 2. Sabor
def insert_sabor() -> Sabor:
    print('Cadastro Sabor')
    
    nome: str = input('Informe o nome do Sabor: ')
    
    sabor: Sabor = Sabor(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(sabor)  # Adicionando o objeto Sabor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Sabor cadastrado com sucesso')
    
    return sabor


# 3. Tipo Embalagem
def insert_tipo_embalagem() -> TipoEmbalagem:
    print('Cadastro Tipo Embalagem')
    
    nome: str = input('Informe o nome do Tipo da embalagem: ')
    
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(tipo_embalagem)  # Adicionando o objeto TipoEmbalagem
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto
    
    print('Tipo Embalagem cadastrado com sucesso')

    return tipo_embalagem


# 4. Tipo Picole
def insert_tipo_picole() -> TipoPicole:
    print('Cadastro Tipo Picole')
    
    nome: str = input('Informe o nome do Tipo Picole: ')
    
    tipo_picole: TipoPicole = TipoPicole(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(tipo_picole)  # Adicionando o objeto TipoPicole
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Tipo Picole cadastrado com sucesso')

    return tipo_picole
    

# 5. Ingrediente
def insert_ingrediente() -> Ingrediente:
    print('Cadastro Ingrediente')
    
    nome: str = input('Informe o nome do Ingrediente: ')
    
    ingrediente: Ingrediente = Ingrediente(nome=nome)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(ingrediente)  # Adicionando o objeto Ingrediente
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Ingrediente cadastrado com sucesso')
    
    return ingrediente
    
    
# 6. Conservante
def insert_conservante() -> Conservante:
    print('Cadastro Conservante')
    
    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')
    
    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(conservante)  # Adicionando o objeto Conservante
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Conservante cadastrado com sucesso')
    
    return conservante


# 7. Revendedor
def insert_revendedor() -> Revendedor:
    print('Cadastro Revendedor')
    
    cnpj: str = input('Informe o cnpj do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')
    
    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(revendedor)  # Adicionando o objeto Revendedor
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Revendedor cadastrado com sucesso')
    
    return revendedor


# 8. Lote
def insert_lote() -> Lote:
    print('Cadastro Lote')
    
    id_tipo_picole: int = int(input('Informe o ID do tipo do picole: '))
    quantidade: int = int(input('Informe a quantidade: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(lote)  # Adicionando o objeto Lote
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Lote cadastrado com sucesso')
    
    return lote


# 9. Nota Fiscal
def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastro Nota Fiscal')
    
    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o numero de série da nota fiscal: ')
    descricao: str = input('Informe a descrição da nota fiscal: ')
    id_revendedor: int = int(input('Informe o ID do revendedor: '))

    nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
    
    lote1 = insert_lote()
    nota_fiscal.lotes.append(lote1)
    
    lote2 = insert_lote()
    nota_fiscal.lotes.append(lote2)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(nota_fiscal)  # Adicionando o objeto NotaFiscal
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Nota Fiscal cadastrada com sucesso')
    
    return nota_fiscal


# 10. Picole
def insert_picole() -> Picole:
    print('Cadastro de Picole')
    
    preco: float = float(input('Informe o preço do picolé: '))
    id_sabor: int = int(input('Informe o id do sabor do picolé: '))
    id_tipo_embalagem: int = int(input('Informe o id da embalagem do picolé: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo do picolé: '))

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
    
    ingrediente1 = insert_ingrediente()  # Obrigatório
    picole.ingredientes.append(ingrediente1)
    
    conservante1 = insert_conservante()  # Opcional
    picole.conservantes.append(conservante1)
    
    aditivos_nutritivo1 = insert_aditivo_nutritivo()  # Opcional
    picole.aditivos_nutritivos.append(aditivos_nutritivo1)
    
    with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(picole)  # Adicionando o objeto Picole
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto

    print('Picole cadastrado com sucesso')
    
    return picole



if __name__ == '__main__':
    # insert_aditivo_nutritivo()
    # insert_sabor()
    # insert_tipo_embalagem()
    # insert_tipo_picole()
    # insert_ingrediente()
    # insert_conservante()
    # revendedor = insert_revendedor()
    # print(revendedor.cnpj)
    # lote = insert_lote()
    # print(lote.id)
    # print(lote.id_tipo_picole)
    # picole = insert_picole()
    # print(picole.id)
    
    picole = insert_picole()
    print(picole.sabor.nome)
    print(picole.tipo_embalagem.nome)
    print(picole.tipo_picole.nome)
    print(picole.ingredientes)
    print(picole.conservantes)
    print(picole.aditivos_nutritivos)

