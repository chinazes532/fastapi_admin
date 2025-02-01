from typing import Optional

from pydantic import BaseModel, ConfigDict


class STextAdd(BaseModel):
    text: str


class SText(STextAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STextID(BaseModel):
    ok: bool = True
    text_id: int