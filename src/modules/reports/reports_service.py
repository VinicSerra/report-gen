from lxml import etree
import weasyprint
from loguru import logger
from datetime import datetime
import os
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
class ReportService:
    def load_html(file_path):
        try:
            # Carrega o template HTML
            logger.info(f"Carregando conteúdo HTML de {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Erro ao ler o arquivo {file_path}: {e}")
            raise
    def render_html_with_data(template_path, data):
        # Configuração do Jinja2 para carregar o template HTML
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
        template = env.get_template(os.path.basename(template_path))
        # Renderiza o template com os dados fornecidos
        rendered_html = template.render(data)
        return rendered_html
    def convert_html_to_pdf(html_content, pdf_output_path):
        try:
            logger.info(f"Iniciando a conversão de HTML para PDF. Saída: {pdf_output_path}")
            weasyprint.HTML(string=html_content).write_pdf(pdf_output_path)
            logger.success(f"PDF gerado com sucesso em {pdf_output_path}")
        except Exception as e:
            logger.error(f"Erro ao gerar PDF: {e}")
            raise
    def generate_pdf_filename():
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"relatorio-{current_time}.pdf"
    def generate_report():
        load_dotenv()  # Carrega as variáveis do arquivo .env
        output_directory = os.getenv('RELATORIO_DIR', os.getcwd())  # Usa a variável de ambiente ou o diretório atual
        input_html = 'relatorio-template.html'
        output_pdf = os.path.join(output_directory, ReportService.generate_pdf_filename())
        # Dados a serem inseridos no template
        data = {
            'logoURL': 'path/to/logo.png',
            'id': 123,
            'projeto': 'Projeto X',
            'remanejamento': 'Remanejamento Y',
            'etapa': 'Etapa Z',
            'construcao': 'Construção A',
            'parte': 'Parte B',
            'status': 'Ativo',
            'contrato': 'Contrato 456',
            'refContrato': 'Ref. 789',
            'empresaProjeto': 'Empresa Y',
            'capexSource': 'CAPEX X',
            'layer': 'Layer A',
            'empresaConstrucao': 'Construtora B',
            'elementoDetalhado': 'Detalhamento X',
            'descricao': 'Descrição detalhada',
            'networkElement': 'Elemento X',
            'loteBOQ': 'Lote 123',
            'po': 'PO 456',
            'itensAcumulados': [
                {'nome': 'Item 1', 'quantidadeProjeto': 10, 'quantidadeMedida': 8, 'quantidadeValidada': 7, 'valor': 100, 'codigo': '001', 'custo': 50},
                {'nome': 'Item 2', 'quantidadeProjeto': 15, 'quantidadeMedida': 12, 'quantidadeValidada': 10, 'valor': 150, 'codigo': '002', 'custo': 75},
            ],
            'itensAtuais': [
                {'nome': 'Item 3', 'quantidadeProjeto': 20, 'quantidadeMedida': 18, 'quantidadeValidada': 15, 'valor': 200, 'codigo': '003', 'custo': 100},
                {'nome': 'Item 4', 'quantidadeProjeto': 25, 'quantidadeMedida': 22, 'quantidadeValidada': 20, 'valor': 250, 'codigo': '004', 'custo': 125},
            ],
            'dataEmissao': datetime.now().strftime('%Y-%m-%d'),
            'responsavel': 'Responsável X',
            'validacao': 'Validado',
            'observacoes': 'Sem observações',
            'aprovacao': 'Aprovado',
            'assinatura': 'Assinatura Y',
        }
        try:
            # Carrega o HTML do template e renderiza com os dados
            html_content = ReportService.render_html_with_data(input_html, data)
            # Converte o HTML renderizado em PDF
            ReportService.convert_html_to_pdf(html_content, output_pdf)
        except Exception as e:
            logger.exception(f"Falha no processamento do relatório: {e}")