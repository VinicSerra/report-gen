import sqlalchemy as sa
from src.database.session import Model

class MedicaoEmpreiteiraValor(Model):
    __tablename__ = "Medicao_Projeto_Empreiteira_valor"

    Codigo = sa.Column(sa.Integer, primary_key=True)
    Contrato = sa.Column(sa.String(250))
    PO = sa.Column(sa.String(250))
    Nome = sa.Column(sa.String(250))
    QtdEmpProjeto = sa.Column(sa.String(250))
    Quantidade = sa.Column(sa.String(250))
    Valor = sa.Column(sa.String(250))
    ItemContrato = sa.Column(sa.String(250))
    Custo = sa.Column(sa.String(250))
    TipoServicos = sa.Column(sa.String(250))
    Data = sa.Column(sa.String(250))
    Versao = sa.Column(sa.String(250))
    Status = sa.Column(sa.String(250))
    QtdValidada = sa.Column(sa.String(250))

class MedicaoProjetoEmpreiteira(Model):
    __tablename__ = "Medicao_Projeto_Empreiteira"

    Codigo = sa.Column(sa.Integer, primary_key=True)
    Contrato = sa.Column(sa.String(250))
    InformacoesDaObra = sa.Column(sa.String(250))
    Status = sa.Column(sa.String(250))
    EmpreiteiraProjeto = sa.Column(sa.String(250))
    EmpreiteiraConstrucao = sa.Column(sa.String(250))
    NetworkElement = sa.Column(sa.String(250))
    Medicao = sa.Column(sa.String(250))
    CapexSource = sa.Column(sa.String(250))
    ElementDetail = sa.Column(sa.String(250))
    LoteBOQ = sa.Column(sa.String(250))
    ReferenciaContrato = sa.Column(sa.String(250))
    Layer = sa.Column(sa.String(250))
    Description = sa.Column(sa.String(250))
    ValorTotalServicos = sa.Column(sa.String(250))
    ValorTotalMateriais = sa.Column(sa.String(250))
    GeradoPor = sa.Column(sa.String(250))
    Data = sa.Column(sa.String(250))
    PO = sa.Column(sa.String(250))