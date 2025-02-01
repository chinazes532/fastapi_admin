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


@router.put("/{id}")
async def edit_text(id: int, text: str) -> STextID:
    id = await TextRepository.edit_text(id, text)
    return id
