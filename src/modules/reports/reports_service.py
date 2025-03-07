from loguru import logger
from datetime import datetime
import os
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from pyppeteer import launch  # Importando o Puppeteer
import traceback

class ReportService:
    
    @staticmethod
    def load_html(file_path):
        try:
            # Carrega o template HTML
            logger.info(f"Carregando conteúdo HTML de {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logger.error(f"Erro ao ler o arquivo {file_path}: {e}")
            raise
    
    @staticmethod
    def render_html_with_data(template_path, data):
        # Configuração do Jinja2 para carregar o template HTML
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
        template = env.get_template(os.path.basename(template_path))
        # Renderiza o template com os dados fornecidos
        rendered_html = template.render(data)
        return rendered_html
    
    @staticmethod
    async def convert_html_to_pdf(html_content, pdf_output_path):
        try:
            logger.info(f"Iniciando a conversão de HTML para PDF. Saída: {pdf_output_path}")
            # Inicializa o Puppeteer
            browser = await launch(headless=True)
            page = await browser.newPage()
            await page.setContent(html_content)
            await page.pdf({'path': pdf_output_path, 'format': 'A4'})
            await browser.close()
            logger.success(f"PDF gerado com sucesso em {pdf_output_path}")
        except Exception as e:
            logger.error(f"Erro ao gerar PDF: {e}")
            raise
    
    @staticmethod
    def generate_pdf_filename():
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"relatorio-{current_time}.pdf"
    
    @staticmethod
    async def generate_report():
        # Dados simulados (mocked data) para o relatório
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
        
        # Caminhos fixos
        input_html = r'E:\project\Report\report-gen-main\relatorio-tim.html'  # Caminho fixo para o HTML
        output_directory = r'E:\project\Report\report-gen-main\relatorios'  # Caminho fixo para o diretório de saída do PDF
        os.makedirs(output_directory, exist_ok=True)  # Cria a pasta 'relatorios' se não existir
        output_pdf = os.path.join(output_directory, ReportService.generate_pdf_filename())
        
        try:
            # Carrega o HTML do template e renderiza com os dados
            html_content = ReportService.render_html_with_data(input_html, data)
            # Converte o HTML renderizado em PDF
            await ReportService.convert_html_to_pdf(html_content, output_pdf)
            return output_pdf
        except Exception as e:
            logger.exception(f"Falha no processamento do relatório: {e}")
            raise
