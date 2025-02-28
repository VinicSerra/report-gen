from pydantic import BaseModel

class GenereteRequest(BaseModel):
    CodigoEmissao: int
    TipoServico: str