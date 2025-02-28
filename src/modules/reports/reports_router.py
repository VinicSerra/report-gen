from fastapi import APIRouter
from src.modules.reports import reports_schemas as schemas

router = APIRouter(
    prefix = "/reports",
    tags = ["Reports"]
)

@router.get("/")
def generete_report(data:schemas.GenereteRequest):
    try:
        generete_report = data
        return generete_report
    except Exception as e:
        raise e