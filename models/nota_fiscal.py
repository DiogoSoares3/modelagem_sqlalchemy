import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from typing import List
from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote


# Nota Fiscal pode ter vários Lotes (tabela de relacionamento muitos para muitos)
lotes_nota_fiscal = sa.Table(  # Criando a tabela de muitos para muitos
    'lotes_nota_fiscal',  # Nome da tabela
    ModelBase.metadata,  # 
    sa.Column('id_nota_fiscal', sa.BigInteger, sa.ForeignKey('notas_fiscais.id')),  # Chave estrangeira
    sa.Column('id_lote', sa.BigInteger, sa.ForeignKey('lotes.id')),  # Chave estrangeira
    
)


class NotaFiscal(ModelBase):  # Herdando modelo base
    __tablename__: str = 'notas_fiscais' # Nome da tabela no banco de dados no plural
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) # Chave primária do model (tabela). Passado de forma automática
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) # Valor padrão é a hora exata em que o objeto foi criado
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False) # Valor decimal com até 8 dígitos e 2 dígitos após a vírgula
    numero_serie: str = sa.Column(sa.String(45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)

    id_revendedor: int = sa.Column(sa.BigInteger, sa.ForeignKey('revendedores.id')) # Chave estrangeira --> tabela.coluna 
    revendedor: Revendedor = orm.relationship('Revendedor', lazy='joined') # Configuração interna do sqlalchemy necessária quando tem chave estrangeira
    
    # Uma nota Fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    

    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Nota Fiscal: {self.id}>'
