"""
1. Buscar o registro a ser atualizado
2. Fazer as alterações no registro
3. Salvar o registro no banco de dados
"""
from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole

def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        # Passo 1:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        if sabor:
            # Passo 2:
            sabor.nome = novo_nome
            # Passo 3:
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')
            

def atualizar_picole(id_picole: int, novo_preco: float, novo_id_sabor: int=None):
    with create_session() as session:
        # Passo 1:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            # Passo 2:
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também...
            if novo_id_sabor:
                picole.id_sabor = novo_id_sabor
            # Passo 3:
            session.commit()
        else:
            print(f'Não existe picole com ID {id_picole}')
    


if __name__ == '__main__':
    #atualizar_sabor(id_sabor=42, novo_nome='namee')
    atualizar_picole(id_picole=30, novo_preco=3.45, novo_id_sabor=12)