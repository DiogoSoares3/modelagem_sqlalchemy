from typing import List
from sqlalchemy import func, desc  # Funções de agregação
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
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # Forma 1
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)
        
        # Forma 2
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        
        for aditivo in aditivos_nutritivos:
            print(f'ID: {aditivo.id}')
            print(f'Data de criação: {formata_data(aditivo.data_criacao)}')
            print(f'Nome: {aditivo.nome}')
            print(f'Fórmula química: {aditivo.formula_quimica}')
            

# Select simples -> SELECT * FROM sabores WHERE id = <id_sabor>
def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # Forma 1: Retorna None caso não encontre
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()  # 'first()' para não retornar a query em si, e sim o resultado dela
        
        # # Forma 2: Retorna None caso não encontre (Recomendado)
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        # # Forma 3: Exception exec.NoResultFound caso não encontre
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        
        # # Forma 4: Usando where ao invés de filter (utilizando one(), one_or_none() ou first())
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one()
        
        # Forma com mais filtros
        #sabor: Sabor = session.query(Sabor.id, Sabor.nome).where(Sabor.id == id_sabor).one()


        
        print(f'ID: {sabor.id}')
        print(f'Data de criação: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')


# SELECT * FROM picoles
def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()
        print(picoles)
        
        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data de criação: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')
            
            print(f'ID sabor: {picole.id_sabor}')
            print(f'Nome do sabor: {picole.sabor.nome}')
            
            print(f'ID tipo embalagem: {picole.id_tipo_embalagem}')
            print(f'Tipo embalagem: {picole.tipo_embalagem.nome}')
            
            print(f'ID tipo picole: {picole.id_tipo_picole}')
            print(f'Tipo embalagem: {picole.tipo_picole.nome}')
            
            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')


# SELECT * FROM sabores ORDER BY data_criacao DESC
def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()
    
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f"Nome: {sabor.nome}")


# SELECT * FROM picoles GROUP BY id, id_tipo_picole
def select_groupby_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

        for picole in picoles:
            print(f"ID: {picole.id}")
            print(f"Tipo picole: {picole.tipo_picole.nome}")
            print(f"Sabor: {picole.sabor.nome}")
            print(f"Preço: {picole.preco}")


def select_limit(limite: int=5) -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(limite)

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Sabor: {sabor.nome}")
    
    
def select_count_revendedor() -> None:
    with create_session() as session:
        quantidade: int = session.query(Revendedor).distinct().count()  # Não precisa de distinct

        print(f'Quantidade de revendedores: {quantidade}')

    
def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        ).all()
        
        print(f'A soma de todos os picoles é {resultado[0][0]}')
        print(f'A média de todos os picoles é {resultado[0][1]}')
        print(f'O picole mais barato de todos é {resultado[0][2]}')
        print(f'O picole mais caro de todos é {resultado[0][3]}')

        print('==========')
        print(resultado)
        
        
# Teste complexo: 
    """
    SELECT quantidade, preco FROM lotes
    JOIN tipos_picole ON lotes.id_tipo_picole = tipos_picole.id
    JOIN picoles ON picoles.id_tipo_picole = tipos_picole.id 
    WHERE preco > 5 AND quantidade > 30
    """
def select_preco_picole_quantidade_lote() -> None:
    with create_session() as session:
        preco_quantidade: List = session.query(Lote.quantidade, Picole.preco)\
            .join(TipoPicole, Lote.id_tipo_picole == TipoPicole.id)\
            .join(Picole, Picole.id_tipo_picole == TipoPicole.id)\
            .where(Lote.quantidade > 30).where(Picole.preco > 5).all()
        
        for row in preco_quantidade:
            print(row[0], row[1])
            
            
# Consulta com subquery retornando apenas a quantidade de lotes em que o preco do picole é maior que 5:
    """
    select quantidade from lotes where id_tipo_picole in 
    (select id, preco from tipos_picole where id in 
    (select id_tipo_picole from picoles where preco > 5))
    """
def select_quantidade_lote() -> None:
    with create_session() as session:
        subquery1 = session.query(Picole.id_tipo_picole).where(Picole.preco > 5)
        subquery2 = session.query(TipoPicole.id).where(TipoPicole.id.in_(subquery1))
        
        quantidade: List = session.query(Lote.quantidade)\
            .where(Lote.id_tipo_picole.in_(subquery2))

        for row in quantidade:
            print(row[0])
    
    
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
def super_consulta() -> None:
    with create_session() as session:
        result: List = session.query(Lote.quantidade, func.avg(Picole.preco), func.count(Lote.quantidade).label('contador'))\
            .join(TipoPicole, Lote.id_tipo_picole == TipoPicole.id)\
            .join(Picole, Picole.id_tipo_picole == TipoPicole.id)\
            .where(Picole.preco > 5).where(Lote.quantidade > 30)\
            .group_by(Lote.quantidade)\
            .order_by(desc('contador'))\
            .limit(10)
        
        for row in result:
            print(row)
    
    
    

if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    select_complexo_picole()
    #select_groupby_picole()
    #select_limit()
    #select_count_revendedor()
    #select_agregacao()
    #select_preco_picole_quantidade_lote()
    #select_quantidade_lote()
    #super_consulta()