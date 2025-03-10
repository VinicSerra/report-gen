from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from src.modules.reports import reports_schemas as schemas
from datetime import datetime
from src.modules.reports import ReportService
from traceback import format_exception
from io import BytesIO
from xhtml2pdf import pisa
from jinja2 import Template

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/{codigo}")
def find_by_codigo(codigo: str, service: ReportService):
    medicao = service.find_by_codigo_medicao(codigo)
    return medicao

@router.get("/")
async def generate_report(service: ReportService):
    try:
        data_relatorio_formatada = datetime.strptime("2025-03-05", "%Y-%m-%d").strftime("%d/%m/%Y")
        
        relatorio_data = {
            "logo_url": "https://via.placeholder.com/150",
            "projeto_id": "12345",
            "descricao_projeto": "Projeto de Teste",
            "metadata": {
                "Status": "Fechamento Final",
                "Contrato": "4600033844 TNE LD",
                "Ref. Contrato": "TNE LD",
                "Emp. Projeto": "WUHAN FIBERHOME INTERNACIONAL",
                "Capex Source": "TRANSPORT",
                "Layer": "Novas Rotas - Rede Externa",
                "Emp. Construção": "WUHAN FIBERHOME INTERNACIONAL",
                "Element Detai": "Transnordestina",
                "Description": "Obrigações Institucionais - TransNordestina Fase II e III [Const]",
                "Network Elemen": "Transmission / KM LD / KM LD / PxQ",
                "Lote BOQ": "414284",
                "PO": "4503938693",
                "LPU NOVA": ""
            },
            "medicao_acumulada": [
                {"nome": "Item A", "quant_emp_projeto": 10, "quant_medida": 8, "quant_validada": 8, "valor": 100, "item": "001", "custo": 80},
                {"nome": "Item B", "quant_emp_projeto": 20, "quant_medida": 15, "quant_validada": 14, "valor": 200, "item": "002", "custo": 180}
            ],
            "medicao_atual": [
                {"nome": "Item C", "quant_emp_projeto": 15, "quant_medida": 12, "quant_validada": 11, "valor": 150, "item": "003", "custo": 130}
            ],
            "total_acumulado": 500,
            "total_atual": 150,
            "gerado_por": "João Silva",
            "data_relatorio": data_relatorio_formatada  # Usando a data formatada
        }
        with open("src/templates/timhtml.html", "r", encoding="utf-8") as f:
            html_template = f.read()

        template = Template(html_template)
        html_content = template.render(**relatorio_data)

        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

        if pisa_status.err:
            raise HTTPException(status_code=500, detail="Erro ao gerar o PDF")

        pdf_file.seek(0)
        return StreamingResponse(pdf_file, media_type='application/pdf', headers={"Content-Disposition": "attachment; filename=relatorio.pdf"})
    except Exception as e:
        formatted_exception = "".join(format_exception(type(e), e, e.__traceback__))
        raise HTTPException(status_code=500, detail=f"Erro ao gerar o relatório: {formatted_exception}")
