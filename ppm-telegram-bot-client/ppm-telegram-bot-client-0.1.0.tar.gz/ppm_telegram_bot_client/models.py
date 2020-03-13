from typing import Any  # noqa
from typing import List, Optional

from pydantic import BaseModel, Field


class HTTPValidationError(BaseModel):
    detail: "Optional[List[ValidationError]]" = Field(None, alias="detail")


class TalkInfo(BaseModel):
    speaker_name: "str" = Field(..., alias="speaker_name")
    talk_name: "str" = Field(..., alias="talk_name")
    talk_dates: "str" = Field(..., alias="talk_dates")
    notion_url: "str" = Field(..., alias="notion_url")


class ValidationError(BaseModel):
    loc: "List[str]" = Field(..., alias="loc")
    msg: "str" = Field(..., alias="msg")
    type: "str" = Field(..., alias="type")
