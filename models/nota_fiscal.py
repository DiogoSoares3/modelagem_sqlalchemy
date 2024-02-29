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
    ModelBase.metadata, 
    sa.Column('id_nota_fiscal', sa.BigInteger, sa.ForeignKey('notas_fiscais.id')),  # Chave estrangeira
    sa.Column('id_lote', sa.BigInteger, sa.ForeignKey('lotes.id')),  # Chave estrangeira
    
)


class NotaFiscal(ModelBase):  
    __tablename__: str = 'notas_fiscais' 
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) 
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) 
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False) 
    numero_serie: str = sa.Column(sa.String(45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)

    id_revendedor: int = sa.Column(sa.BigInteger, sa.ForeignKey('revendedores.id', ondelete='CASCADE'))  # Efeito cascata quando ocorrer a exclusao de um revendedor ocorrer (default é impedimento). Temos a anulação como opção tbm
    revendedor: Revendedor = orm.relationship('Revendedor', lazy='joined', cascade='delete')  # Vai realizar o join para obter o relacionamento e vai deletar o registro todo quando houver cascade
    
    # Uma nota Fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    

    def __repr__(self) -> str:  # Método usado para definir a representação "oficial" de um objeto
        return f'<Nota Fiscal: {self.id}>'
