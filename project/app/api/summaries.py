from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """Define a handler that expects a payload (SummaryPayloadSchema), with a URL.

    When the route is hit with a POST request, FastAPI will read the body of the request and validate the data:
    Valid -> the data will be available in the payload parameter.
    Invalid -> an error is immediately returned.
    """
    summary_id = await crud.post(payload)

    response_object = {"id": summary_id, "url": payload.url}
    return response_object
