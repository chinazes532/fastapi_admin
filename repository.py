from sqlalchemy import select

from database import new_session, TextOrm
from schemas import STextID, SText


class TextRepository:

    @classmethod
    async def find_all(cls) -> list[SText]:
        async with new_session() as session:
            query = select(TextOrm)
            result = await session.execute(query)
            text_models = result.scalars().all()
            text_schemas = [SText.model_validate(text_model) for text_model in text_models]

            return text_models

    @classmethod
    async def edit_text(cls, text_id: int, text: str) -> STextID:
        async with new_session() as session:
            query = select(TextOrm).where(TextOrm.id == text_id)
            result = await session.execute(query)
            text_model = result.scalar()
            text_model.text = text
            await session.commit()

            return STextID(text_id=text_model.id)

    @classmethod
    async def get_text(cls, text_id: int) -> SText:
        async with new_session() as session:
            query = select(TextOrm).where(TextOrm.id == text_id)
            result = await session.execute(query)
            text_model = result.scalar()
            text_schema = SText.model_validate(text_model)

            return text_schema
