import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class TipoPicole(ModelBase):  # Herdando modelo base
    __tablename__: str = 'tipos_picole' # Nome da tabela no banco de dados no plural
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) # Chave primária do model (tabela). Passado de forma automática
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) # Valor padrão é a hora exata em que o objeto foi criado


    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Tipo Picole: {self.nome}>'
