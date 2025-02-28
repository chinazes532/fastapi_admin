from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    'postgresql+asyncpg://gen_user:eZfIH)A%3A%7D9O%26%25k@94.241.143.46:5432/default_db',
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TextOrm(Model):
    __tablename__ = "texts"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

