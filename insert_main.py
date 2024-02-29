import asyncio

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
async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastro Aditivo Nutritivo')
    
    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')
    
    aditivo_nutritivo: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
    
    async with create_session() as session:  # Criando um contexto na variável session
        # Se eu não estivesse em uma sessão, seria necessário fechar a sessão com session.close()
        session.add(aditivo_nutritivo)  # 'session.add()' não é um método async
        
        await asyncio.sleep(1)
        
        # Commita para o banco de dados todas as operações que ocorreram dentro da sessão de uma vez só
        await session.commit() # O commit é realizado em batch contendo todas as operações que foram realizadas dentro do contexto
        # 'session.commit()' é um método
        
    print('Aditivo Nutritivo cadastrado com sucesso')
    print('=============================')
    
    return aditivo_nutritivo

 
# 2. Sabor
async def insert_sabor() -> Sabor:
    print('Cadastro Sabor')
    
    nome: str = input('Informe o nome do Sabor: ')
    
    sabor: Sabor = Sabor(nome=nome)
    
    async with create_session() as session:  
        session.add(sabor)  
        
        await session.commit() 

    print('Sabor cadastrado com sucesso')
    print('=============================')
    
    return sabor


# 3. Tipo Embalagem
async def insert_tipo_embalagem() -> TipoEmbalagem:
    print('Cadastro Tipo Embalagem')
    
    nome: str = input('Informe o nome do Tipo da embalagem: ')
    
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)
    
    async with create_session() as session:  
        session.add(tipo_embalagem) 
        
        await asyncio.sleep(1)
        
        await session.commit() 
    
    print('Tipo Embalagem cadastrado com sucesso')
    print('=============================')

    return tipo_embalagem


# 4. Tipo Picole
async def insert_tipo_picole() -> TipoPicole:
    print('Cadastro Tipo Picole')
    
    nome: str = input('Informe o nome do Tipo Picole: ')
    
    tipo_picole: TipoPicole = TipoPicole(nome=nome)
    
    async with create_session() as session: 
        session.add(tipo_picole)  
        
        await asyncio.sleep(1)
        
        await session.commit()

    print('Tipo Picole cadastrado com sucesso')
    print('=============================')

    return tipo_picole
    

# 5. Ingrediente
async def insert_ingrediente() -> Ingrediente:
    print('Cadastro Ingrediente')
    
    nome: str = input('Informe o nome do Ingrediente: ')
    
    ingrediente: Ingrediente = Ingrediente(nome=nome)
    
    async with create_session() as session: 
        session.add(ingrediente)
        
        await asyncio.sleep(1)
        
        await session.commit()

    print('Ingrediente cadastrado com sucesso')
    print('=============================')
    
    return ingrediente
    
    
# 6. Conservante
async def insert_conservante() -> Conservante:
    print('Cadastro Conservante')
    
    nome: str = input('Informe o nome do Conservante: ')
    descricao: str = input('Informe a descrição do Conservante: ')
    
    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
    
    async with create_session() as session:  
        session.add(conservante)
        
        await asyncio.sleep(1)
        
        await session.commit()

    print('Conservante cadastrado com sucesso')
    print('=============================')
    
    return conservante


# 7. Revendedor
async def insert_revendedor() -> Revendedor:
    print('Cadastro Revendedor')
    
    cnpj: str = input('Informe o cnpj do Revendedor: ')
    razao_social: str = input('Informe a razão social do Revendedor: ')
    contato: str = input('Informe o contato do Revendedor: ')
    
    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
    
    async with create_session() as session:
        session.add(revendedor)
        
        await asyncio.sleep(1)
        
        await session.commit()

    print('Revendedor cadastrado com sucesso')
    print('=============================')
    
    return revendedor


# 8. Lote
async def insert_lote() -> Lote:
    print('Cadastro Lote')
    
    id_tipo_picole: int = int(input('Informe o ID do tipo do picole: '))
    quantidade: int = int(input('Informe a quantidade: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
    
    async with create_session() as session:  
        session.add(lote) 
        
        await asyncio.sleep(1)
        
        await session.commit() 

    print('Lote cadastrado com sucesso')
    print('=============================')
    
    return lote


# 9. Nota Fiscal
async def insert_nota_fiscal() -> NotaFiscal:
    print('Cadastro Nota Fiscal')
    
    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o numero de série da nota fiscal: ')
    descricao: str = input('Informe a descrição da nota fiscal: ')
    id_revendedor: int = int(input('Informe o ID do revendedor: '))

    nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
    
    lote1 = await insert_lote()
    nota_fiscal.lotes.append(lote1)
    
    lote2 = await insert_lote()
    nota_fiscal.lotes.append(lote2)
    
    async with create_session() as session:
        session.add(nota_fiscal)
                
        await session.commit()
        await session.refresh(nota_fiscal)  # Para podermos acessa-lo por completo (já que a versão do banco não é atualizada automaticamente)

    print('Nota Fiscal cadastrada com sucesso')
    print('=============================')
    
    return nota_fiscal


# 10. Picole
async def insert_picole() -> Picole:
    print('Cadastro de Picole')
    
    preco: float = float(input('Informe o preço do picolé: '))
    id_sabor: int = int(input('Informe o id do sabor do picolé: '))
    id_tipo_embalagem: int = int(input('Informe o id da embalagem do picolé: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo do picolé: '))

    picole: Picole = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
    
    ingrediente1 = await insert_ingrediente()  # Obrigatório
    picole.ingredientes.append(ingrediente1)
    
    conservante1 = await insert_conservante()  # Opcional
    picole.conservantes.append(conservante1)
    
    aditivos_nutritivo1 = await insert_aditivo_nutritivo()  # Opcional
    picole.aditivos_nutritivos.append(aditivos_nutritivo1)
    
    async with create_session() as session:  
        session.add(picole)
                
        await session.commit()
        await session.refresh(picole)  # Para podermos acessa-lo por completo (conservantes, ingredientes e aditivos)

    print('Picole cadastrado com sucesso')
    print('=============================')
    
    return picole



if __name__ == '__main__':
    event = asyncio.get_event_loop()
    # tarefa1 = event.create_task(insert_aditivo_nutritivo())
    # tarefa2 = event.create_task(insert_sabor())
    # tarefa3 = event.create_task(insert_tipo_embalagem())
    # tarefa4 = event.create_task(insert_tipo_picole())
    # tarefa5 = event.create_task(insert_ingrediente())
    # tarefa6 = event.create_task(insert_conservante())
    # tarefa7 = event.create_task(insert_revendedor())
    # tarefa8 = event.create_task(insert_lote())
    tarefa9 = event.create_task(insert_nota_fiscal())
    tarefa10 = event.create_task(insert_picole())
    tarefas = asyncio.gather(tarefa9, tarefa10)  # tarefa1, tarefa2, tarefa3, tarefa4, tarefa5, tarefa6, tarefa7, tarefa8, 
    event.run_until_complete(tarefas)
    
    # pic = asyncio.run(insert_picole())