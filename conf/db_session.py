from pathlib import Path
from typing import Optional

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from models.model_base import ModelBase

from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")

__async_engine: Optional[AsyncEngine] = None


def create_engine(sqlite: bool=False) -> AsyncEngine:
    """
    Função de configuração de conexão do sql alchemy com o banco de dados
    """
    global __async_engine
    
    if __async_engine:
        return
    
    if sqlite:  # Para SQLite
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite+aiosqlite:///{arquivo_db}'
        __async_engine = create_async_engine(
            url=conn_str,
            echo=False,
            connect_args={'check_same_thread': False}
        )
    else:
        # PostgreSQL
        conn_str = f'postgresql+asyncpg://{usuario}:{senha}@localhost:5432/picoles'
        __async_engine = create_async_engine(
            url=conn_str,
            echo=False,  # 'echo=True' imprime a consulta sql que o sqlalchemy faz 
        )
        
    return __async_engine
    


def create_session() -> AsyncSession:
    """
    Função para a criar sessão de conexão ao banco de dados.
    Sessões são conexões temporárias ao banco de dados. 
    Dentro das sessões podemos realizar o CRUD no banco de dados.
    """
    
    global __async_engine
    
    if not __async_engine:
        create_engine()
        
    __async_session = sessionmaker(
        __async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    
    session: AsyncSession = __async_session()
    
    return session
    

async def create_tables() -> None:
    global __async_engine
    
    if not __async_engine:
        create_engine()
        
    import models.__all_models
    async with __async_engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
        await conn.run_sync(ModelBase.metadata.create_all)