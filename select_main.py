from typing import List
from sqlalchemy import func  # Funções de agregação
from conf.helpers import formata_data
from conf.db_session import create_session

# Select simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select complexos
from models.picole import Picole


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


def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()
        
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


def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()
    
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f"Nome: {sabor.nome}")

        

if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    select_filtro_sabor(21)
    