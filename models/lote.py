import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
import sqlalchemy.orm as orm

class Lote(ModelBase):  # Herdando modelo base
    __tablename__: str = 'lotes' # Nome da tabela no banco de dados no plural
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) # Chave primária do model (tabela). Passado de forma automática
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) # Valor padrão é a hora exata em que o objeto foi criado
    quantidade: int = sa.Column(sa.Integer, nullable=False)
    
    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id')) # Chave estrangeira --> tabela.coluna 
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined') # Configuração interna do sqlalchemy necessária quando tem chave estrangeira
    

    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Revendedor: {self.id}>'
