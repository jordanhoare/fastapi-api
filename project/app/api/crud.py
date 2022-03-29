from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """A utility function to create new summaries
    - takes a payload object
    - creates a new TextSummary instance
    - returns the generated ID
    """
    summary = TextSummary(
        url=payload.url,
        summary="placeholder summary",
    )
    await summary.save()
    return summary.id
