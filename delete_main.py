"""
1. Buscar o registro a ser atualizado
2. Fazer a exclusão no registro
3. Salvar o registro no banco de dados
"""
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole
from typing import Optional


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        # Passo 1:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            # Passo 2:
            session.delete(picole)
            # Passo 3:
            session.commit()
            print('====================')
            print(picole)
            print('====================')
        else:
            print(f'Não encontrei picole com id {id_picole}')
            
            
def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        # Passo 1:
        revendedor: Revendedor = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        
        if revendedor:
            # Passo 2:
            session.delete(revendedor)
            # Passo 3:
            session.commit()
        else:
            print(f'Não encontrei revendedor com id {id_revendedor}')



if __name__ == '__main__':
    #deletar_picole(id_picole=1)
    deletar_revendedor(id_revendedor=2) # (impedimento) Erro pois o revendedor com id 2 tem referência na tabela notas_fiscais
    # Mas com cascata ele vai ser forçado a deletar