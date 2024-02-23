import sqlalchemy as sa

# Criador de sessão no sqlalchemy:
from sqlalchemy.orm import sessionmaker

# Vamos usar o Path criar diretorios e arquivos (só para o sqlite):
from pathlib import Path
from typing import Optional # Para tipagem

# Para criar objetos do tipo Session:
from sqlalchemy.orm import Session

# Para criar uma engine:
from sqlalchemy.future.engine import Engine

# Usado para cirar ou deletar as tabelas no banco de dados:
from models.model_base import ModelBase


# Criando uma variável global para a forma de conexão (SQLite, Postgres, etc)
__engine: Optional[Engine] = None

# Biblioteca para carregar ambientes
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")


def create_engine(sqlite: bool=False) -> Engine:
    """
    Função de configuração de conexão do sql alchemy com o banco de dados
    """

    # Avisando ao interpretador que essas variáveis são globais
    global __engine 
    global usuario
    global senha
    
    if __engine:  # Se a engine já estiver criada, encerra a função
        return
    
    if sqlite:  # Se quiser usar o SQLite, cria um diretório para a base de dados
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True) # Criando diretorio db a partir do pai, se já existir, não faz nada
        
        conn_str = f'sqlite:///{arquivo_db}' # Conexão com o SQLite
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False}) # Variável global __engine com o SQLite
    else:  # Se for Postgres
        conn_str = f"postgresql://{usuario}:{senha}@localhost:5432/picoles" # Conexão com o seu usuário do Postgresql
        __engine = sa.create_engine(url=conn_str, echo=False)
        
    return __engine


def create_session() -> Session:
    """
    Função para a criar sessão de conexão ao banco de dados
    """
    
    global __engine
    
    if not __engine:
        create_engine()  # Para sqlite: create_engine(sqlite=True)
    
    # Criando uma sessão com a engine disponibilizada
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    
    session: Session = __session()
    
    return session


def create_tables() -> None:
    global __engine
    
    if not __engine:
        create_engine()  # Para sqlite: create_engine(sqlite=True)
    
    import models.__all_models
    ModelBase.metadata.drop_all(__engine)  # Apagando todas as tabelas existentes nessa conexão
    ModelBase.metadata.create_all(__engine)  # Criando as tabelas