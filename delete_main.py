"""
1. Buscar o registro a ser atualizado
2. Fazer a exclusão no registro
3. Salvar o registro no banco de dados
"""
import asyncio
from sqlalchemy.future import select
from conf.db_session import create_session
from models.revendedor import Revendedor
from models.picole import Picole
from typing import Optional


async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        # Passo 1:
        picole: Optional[Picole] = (await session.execute(select(Picole).filter(Picole.id == id_picole))).unique().scalar_one_or_none()
        
        if picole:
            # Passo 2:
            await session.delete(picole)  # Método assincrono (diferente do '.add()')
            # Passo 3:
            await session.commit()
        else:
            print(f'Não encontrei picole com id {id_picole}')
            
            
async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        # Passo 1:
        revendedor: Revendedor = (await session.execute(select(Revendedor).filter(Revendedor.id == id_revendedor))).scalar_one_or_none()
        
        if revendedor:
            # Passo 2:
            await session.delete(revendedor)
            # Passo 3:
            await session.commit()
        else:
            print(f'Não encontrei revendedor com id {id_revendedor}')



if __name__ == '__main__':
    el = asyncio.get_event_loop()
    el.run_until_complete(deletar_picole(id_picole=1))
    el.run_until_complete(deletar_revendedor(id_revendedor=13)) # (impedimento por default) Erro pois o revendedor com id 2 tem referência na tabela notas_fiscais
    # Mas com cascata ele vai ser forçado a deletar (nesse caso setamos cascate=True em notas_fiscais)