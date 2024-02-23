import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from typing import List
from typing import Optional
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente


# Picole pode ter vários ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_ingrediente',sa.BigInteger, sa.ForeignKey('ingredientes.id')),
    sa.Column('id_picole',sa.BigInteger, sa.ForeignKey('picoles.id'))
)

# Picole pode ter vários conservantes
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_conservante',sa.BigInteger, sa.ForeignKey('conservantes.id')),
    sa.Column('id_picole',sa.BigInteger, sa.ForeignKey('picoles.id'))
)

# Picole pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_aditivo_nutritivo',sa.BigInteger, sa.ForeignKey('aditivos_nutritivos.id')),
    sa.Column('id_picole',sa.BigInteger, sa.ForeignKey('picoles.id'))
)


class Picole(ModelBase):  
    __tablename__: str = 'picoles' 
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True) 
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True) 
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    
    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id')) # Chave estrangeira --> tabela.coluna 
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined') # Configuração interna do sqlalchemy necessária quando tem chave estrangeira
    
    id_sabor: int = sa.Column(sa.BigInteger, sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship('Sabor', lazy='joined') 
    
    id_tipo_embalagem: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined') 
    
    # Um picole pode ter vários ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')
    
    # Um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservante', secondary=conservantes_picole, backref='conservante', lazy='joined')
    
    # Um picole pode ter vários aditivos nutritivos ou mesmo nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')
    

    def __repr__(self) -> str:  
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
