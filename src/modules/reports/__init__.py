from fastapi import Depends
from typing_extensions import Annotated

from src.modules.reports import reports_service as service 
ReportService = Annotated[service.ReportService, Depends(service.ReportService)]
 
from src.modules.reports.reports_router import router