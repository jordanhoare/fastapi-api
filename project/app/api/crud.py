from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import Stock_Pydantic
from app.summariser import generate_summary


async def get(id: int) -> Union[dict, None]:
    summary = await Stock_Pydantic.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await Stock_Pydantic.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await Stock_Pydantic.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = await Stock_Pydantic.filter(id=id).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        updated_summary = await Stock_Pydantic.filter(id=id).first().values()
        return updated_summary
    return None


async def post(payload: SummaryPayloadSchema) -> int:
    """
    A utility function to create new summaries
    - takes a payload object
    - creates a new Stock_Pydantic instance
    - returns the generated ID
    """
    summary = Stock_Pydantic(url=payload.url, summary="")
    await summary.save()
    return summary.id
