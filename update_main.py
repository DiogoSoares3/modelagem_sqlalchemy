"""
1. Buscar o registro a ser atualizado
2. Fazer as alterações no registro
3. Salvar o registro no banco de dados
"""
import asyncio
from sqlalchemy.future import select
from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole

async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    async with create_session() as session:
        # Passo 1:
        sabor: Sabor = (await session.execute(select(Sabor).filter(Sabor.id == id_sabor))).scalar_one_or_none()
        
        if sabor:
            # Passo 2:
            sabor.nome = novo_nome
            # Passo 3:
            await session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')
            

async def atualizar_picole(id_picole: int, novo_preco: float, novo_id_sabor: int=None):
    async with create_session() as session:
        # Passo 1:
        picole: Picole = (await session.execute(select(Picole).filter(Picole.id == id_picole))).scalars().unique().one_or_none()
                
        if picole:
            # Passo 2:
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também...
            if novo_id_sabor:
                picole.id_sabor = novo_id_sabor
            # Passo 3:
            await session.commit()
        else:
            print(f'Não existe picole com ID {id_picole}')
    


if __name__ == '__main__':
    #asyncio.run(atualizar_sabor(id_sabor=3, novo_nome='oalal'))
    asyncio.run(atualizar_picole(id_picole=30, novo_preco=3.45, novo_id_sabor=14))