import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):  # Herdando modelo base
    __tablename__: str = 'aditivos_nutritivos' # Nome da tabela no banco de dados no plural
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) # Chave primária do model (tabela). Passado de forma automática
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) # Valor padrão é a hora exata em que o objeto foi criado
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False) # Único e não nulo com limite de até 45 caracteres
    formula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False) # Único e não nulo com limite de até 45 caracteres


    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Aditivo Nutritivo: {self.nome}>'
