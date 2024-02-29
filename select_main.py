import asyncio

from typing import List
from sqlalchemy import func, desc  # Funções de agregação
from sqlalchemy.future import select
from conf.helpers import formata_data
from conf.db_session import create_session

# Select simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select complexos
from models.picole import Picole
from models.lote import Lote
from models.tipo_picole import TipoPicole


# Select simples -> SELECT * FROM aditivos_nutritivos
async def select_todos_aditivos_nutritivos() -> None:    
    async with create_session() as session:
        query = select(AditivoNutritivo)
        result = await session.execute(query)
        
        await asyncio.sleep(2)
        
        aditivos_nutritivos: List[AditivoNutritivo] = result.scalars().all()  # 'scalars()' porque retorna uma lista (sempre). Só é usado em assincronia
        
        # Jeito com '.scalars()'
        # for aditivo in aditivos_nutritivos:
        #     print(f'ID: {aditivo.id}')
        #     print(f'Data de criação: {formata_data(aditivo.data_criacao)}')
        #     print(f'Nome: {aditivo.nome}')
        #     print(f'Fórmula química: {aditivo.formula_quimica}')
            
        # Jeito sem '.scalars()'
        # for aditivo in aditivos_nutritivos:
        #     print(f'ID: {aditivo[0].id}')
        #     print(f'Data de criação: {formata_data(aditivo[0].data_criacao)}')
        #     print(f'Nome: {aditivo[0].nome}')
        #     print(f'Fórmula química: {aditivo[0].formula_quimica}')
        
        print('Consulta 1 Concluida')
            

# Select simples -> SELECT * FROM sabores WHERE id = <id_sabor>
async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        result = await session.execute(query)
        
        await asyncio.sleep(3)

        
        # Forma 1  (None caso não encontre)
        #sabor: Sabor = result.scalars().first()

        # # Forma 2  (None caso não encontre)
        #sabor: Sabor = result.scalars().one_or_none() 
        
        # # Forma 3  (exec.NoResultFound caso não encontre)
        #sabor: Sabor = result.scalars().one()
        
        # # # Forma 4  (None caso não encontre)
        sabor: Sabor = result.scalar_one_or_none() # Recomendado

        # print(f'ID: {sabor.id}')
        # print(f'Data de criação: {formata_data(sabor.data_criacao)}')
        # print(f'Nome: {sabor.nome}')
        
        print('Consulta 2 Concluida')


# SELECT * FROM picoles
async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        result = await session.execute(query)
        
        await asyncio.sleep(1)
        
        picoles: List[Picole] = result.scalars().unique().all() # Unique() porque tem join com outras tabelas (lazy='joined')
        
        # for picole in picoles:
        #     print(f'ID: {picole.id}')
        #     print(f'Data de criação: {formata_data(picole.data_criacao)}')
        #     print(f'Preço: {picole.preco}')
            
        #     print(f'ID sabor: {picole.id_sabor}')
        #     print(f'Nome do sabor: {picole.sabor.nome}')
            
        #     print(f'ID tipo embalagem: {picole.id_tipo_embalagem}')
        #     print(f'Tipo embalagem: {picole.tipo_embalagem.nome}')
            
        #     print(f'ID tipo picole: {picole.id_tipo_picole}')
        #     print(f'Tipo embalagem: {picole.tipo_picole.nome}')
            
        #     print(f'Ingredientes: {picole.ingredientes}')
        #     print(f'Aditivos nutritivos: {picole.aditivos_nutritivos}')
        #     print(f'Conservantes: {picole.conservantes}')
        
        print('Consulta 3 Concluida')


# SELECT * FROM sabores ORDER BY data_criacao DESC
async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        result = await session.execute(query)
        sabores: List[Sabor] = result.scalars().all()
    
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f"Nome: {sabor.nome}")


# SELECT * FROM picoles GROUP BY id, id_tipo_picole
async def select_groupby_picole() -> None:
    async with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        result = await session.execute(query)
        picoles: List[Picole] = result.scalars().unique().all() # 'unique()' já que 'picoles' tem join com outras tabelas 

        for picole in picoles:
            print(f"ID: {picole.id}")
            print(f"Tipo picole: {picole.tipo_picole.nome}")
            print(f"Sabor: {picole.sabor.nome}")
            print(f"Preço: {picole.preco}")


async def select_limit(limite: int=5) -> None:
    async with create_session() as session:
        query = select(Sabor).limit(limite)
        sabores: List[Sabor] = (await session.execute(query)).scalars().all()
        

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Sabor: {sabor.nome}")
    
    
async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        quantidade: int = (await session.execute(query)).scalars().first()
        
        print(f'Quantidade de revendedores: {quantidade}')

    
async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),  # Como estamos executando vários parametros dentro do select, não iremos usar o 'scalars()'
            func.avg(Picole.preco).label('media'), # O 'scalars()' serve para descompactar uma lista de resultados retornados somente por um parâmetro do select
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        )
        
        resultado = (await session.execute(query)).all()

        
        print(f'A soma de todos os picoles é {resultado[0][0]}')
        print(f'A média de todos os picoles é {resultado[0][1]}')
        print(f'O picole mais barato de todos é {resultado[0][2]}')
        print(f'O picole mais caro de todos é {resultado[0][3]}S')

        print('==========')
        print(resultado)



# Teste complexo: 
    """
    SELECT quantidade, preco FROM lotes
    JOIN tipos_picole ON lotes.id_tipo_picole = tipos_picole.id
    JOIN picoles ON picoles.id_tipo_picole = tipos_picole.id 
    WHERE preco > 5 AND quantidade > 30
    """
async def select_preco_picole_quantidade_lote() -> None:
    async with create_session() as session: 
        query = select(Lote.quantidade, Picole.preco)\
            .join(TipoPicole, Lote.id_tipo_picole == TipoPicole.id)\
            .join(Picole, Picole.id_tipo_picole == TipoPicole.id)\
            .where(Lote.quantidade > 30).where(Picole.preco > 5)
            
        preco_quantidade: List[tuple] = (await session.execute(query)).all() # Com 'scalars()' ele iria desfazer as tuplas, pegando somente o primeiro elemento, no caso quantidade
        
        print(preco_quantidade)
        
        for row in preco_quantidade:
            print(row[0], row[1])
            


async def select_preco_picole_join_lote_test() -> None:
    async with create_session() as session: 
        query = select(Picole.preco)\
            .join(TipoPicole, Picole.id_tipo_picole == TipoPicole.id)\
            .join(Lote, TipoPicole.id == Lote.id_tipo_picole)\
            .where(Lote.quantidade > 30).where(Picole.preco > 5)
            
        preco: List[tuple] = (await session.execute(query)).scalars().all()  # O 'scalars()' retira a tuplas de dentro da lista, deixando só os escalares. Como só temos um parâmemetro no select, não temos perdas
        
        print(preco)
        
        for row in preco:
            print(row[0])




# Consulta com subquery retornando apenas a quantidade de lotes em que o preco do picole é maior que 5:
    """
    select quantidade from lotes where id_tipo_picole in 
    (select id, preco from tipos_picole where id in 
    (select id_tipo_picole from picoles where preco > 5))
    """
async def select_quantidade_lote() -> None:
    async with create_session() as session:  # Selecionando por subquery
        subquery1 = select(Picole.id_tipo_picole).where(Picole.preco > 5)
        subquery2 = select(TipoPicole.id).where(TipoPicole.id.in_(subquery1))
        query = select(Lote.quantidade).where(Lote.id_tipo_picole.in_(subquery2))
        
        quantidade: List[int] = (await session.execute(query)).scalars().all()

        # print(quantidade)
        
        # for row in quantidade:
        #     print(row)


# Super consulta
    """
    SELECT quantidade, avg(preco), count(quantidade) as contador FROM lotes
    JOIN tipos_picole ON lotes.id_tipo_picole = tipos_picole.id
    JOIN picoles ON picoles.id_tipo_picole = tipos_picole.id 
    WHERE preco > 5 AND quantidade > 30
	GROUP BY quantidade
	ORDER BY contador DESC
    LIMIT 10
    """
async def super_consulta() -> None:
    async with create_session() as session:
        result: List[float] = (await session.execute(select(Lote.quantidade, func.avg(Picole.preco), func.count(Lote.quantidade).label('contador'))\
            .join(TipoPicole, Lote.id_tipo_picole == TipoPicole.id)\
            .join(Picole, Picole.id_tipo_picole == TipoPicole.id)\
            .where(Picole.preco > 5).where(Lote.quantidade > 30)\
            .group_by(Lote.quantidade)\
            .order_by(desc('contador'))\
            .limit(10))).all()  # Se usasse '.scalars()', cortaria outros elementos da tupla e deixaria só o primeiro 
        
        print(result)  # Quantidade do lote, avg do preço do picole e contador da quantidade do lote
        
        for row in result:
            print(row[0], row[1], row[2])  # Quantidade do lote, avg do preço do picole e contador da quantidade do lote
    

async def main():
    await asyncio.gather(select_todos_aditivos_nutritivos(), select_filtro_sabor(21), select_complexo_picole())
    

if __name__ == '__main__':
    #asyncio.run(select_todos_aditivos_nutritivos())
    #asyncio.run(select_filtro_sabor(21))
    #asyncio.run(select_complexo_picole())
    #asyncio.run(select_order_by_sabor())
    #asyncio.run(select_groupby_picole())
    #asyncio.run(select_limit())
    #asyncio.run(select_count_revendedor())
    #asyncio.run(select_agregacao()
    #asyncio.run(select_preco_picole_quantidade_lote())
    #asyncio.run(select_preco_picole_join_lote_test())
    #asyncio.run(select_quantidade_lote())
    #asyncio.run(super_consulta())
    
    el = asyncio.get_event_loop()
    el.run_until_complete(main())