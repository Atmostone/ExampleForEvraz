from typing import Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component



from components.chat_backend.chat.application import interfaces, dataclasses


join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    username: str
    age: int


@component
class User:
    users_repo: interfaces.UsersRepo

    @join_point
    def add_user(self, username, age):
        self.users_repo.add(username, age)

    @join_point
    def delete_user(self, id):
        self.users_repo.delete(id)

    @join_point
    def update_user(self, id, username, age):
        self.users_repo.update(id, username, age)

    @join_point
    def get_user(self, id):
        user = self.users_repo.get_by_id(id)
        if not user:
            raise Exception
        return user

    @join_point
    def get_users(self):
        users = self.users_repo.get_all()
        if not users:
            raise Exception
        return users


