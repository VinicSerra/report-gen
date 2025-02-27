from lxml import etree
import weasyprint
from loguru import logger
from datetime import datetime
import os
from dotenv import load_dotenv

def load_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logger.info(f"Carregando conteúdo HTML de {file_path}")
            return file.read()
    except Exception as e:
        logger.error(f"Erro ao ler o arquivo {file_path}: {e}")
        raise

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

def main():
    load_dotenv()  
    output_directory = os.getenv('RELATORIO_DIR', os.getcwd()) 
    input_html = 'relatorio-tim.html'
    output_pdf = os.path.join(output_directory, generate_pdf_filename())

    try:
        html_content = load_html(input_html)
        convert_html_to_pdf(html_content, output_pdf)
    except Exception as e:
        logger.exception(f"Falha no processamento do relatório: {e}")

if __name__ == '__main__':
    main()
