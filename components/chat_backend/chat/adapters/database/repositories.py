from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select, insert, delete, update

from components.chat_backend.chat.adapters.database.tables import user
from components.chat_backend.chat.application.dataclasses import User
from components.chat_backend.chat.application.interfaces import UsersRepo


@component
class UsersRepo(BaseRepository, UsersRepo):
    def get_by_id(self, id: int) -> Optional[User]:
        query = select(User).where(User.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def get_all(self):
        query = select(User)
        return self.session.execute(query).scalars().all()

    def add(self, username, age):
        query = (
            insert(user).
                values(username=username, age=age)
        )
        self.session.execute(query)

    def delete(self, id):
        query = (
            delete(user).
                where(user.c.id == id)
        )
        self.session.execute(query)

    def update(self, id, username, age):
        query = (
            update(user).
                where(user.c.id == id).
                values(username=username, age=age)
        )
        self.session.execute(query)
