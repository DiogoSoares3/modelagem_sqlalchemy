import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class Revendedor(ModelBase):  # Herdando modelo base
    __tablename__: str = 'revendedores' # Nome da tabela no banco de dados no plural
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) # Chave primária do model (tabela). Passado de forma automática
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) # Valor padrão é a hora exata em que o objeto foi criado
    cnpj: str = sa.Column(sa.String(45), unique=True, nullable=False) # Único e não nulo com limite de até 45 caracteres
    razao_social: str = sa.Column(sa.String(100), nullable=False) # Não nulo com limite de até 100 caracteres
    contato: str = sa.Column(sa.String(100), nullable=False) # Não nulo com limite de até 100 caracteres


    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Revendedor: {self.cnpj}>'
