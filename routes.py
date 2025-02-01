from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TextRepository
from schemas import STextID, SText


router = APIRouter(
    prefix="/texts",
    tags=["Текст в боте"],
)


@router.get("")
async def all_texts() -> list[SText]:
    texts = await TextRepository.find_all()
    return texts


@router.put("/{text_id}")
async def edit_text(text_id: int, text: str) -> STextID:
    text_id = await TextRepository.edit_text(text_id, text)
    return text_id
