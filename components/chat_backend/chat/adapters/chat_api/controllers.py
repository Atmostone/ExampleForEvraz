import json

from classic.components import component

from .join_points import join_point
from ...application import services


@component
class User:
    user: services.User

    @join_point
    def on_post_create(self, request, response):
        self.user.add_user(**request.media)

    @join_point
    def on_post_delete(self, request, response):
        self.user.delete_user(**request.media)

    @join_point
    def on_post_put(self, request, response):
        self.user.update_user(**request.media)

    @join_point
    def on_post_patch(self, request, response):
        id = request.media['id']
        user = self.user.get_user(id)
        username = user.username
        age = user.age
        if 'username' in request.media:
            username = request.media['username']
        if 'age' in request.media:
            age = request.media['age']
        self.user.update_user(id, username, age)

    @join_point
    def on_get_get_by_id(self, request, response):
        user = self.user.get_user(**request.media)
        user = {"id": user.id, "username": user.username, "age": user.age}
        response.media = {"user": str(user)}

    @join_point
    def on_get_get_all(self, request, response):
        users = self.user.get_users()
        users = [{"id": i.id, "username": i.username, "age": i.age} for i in users]
        response.media = {"users": str(users)}
