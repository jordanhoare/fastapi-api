from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl
