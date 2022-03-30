from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import User


class UsersRepo(ABC):
    @abstractmethod
    def add(self, username, age):
        ...

    @abstractmethod
    def get_by_id(self, id):
        ...

    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def delete(self, id):
        ...

    @abstractmethod
    def update(self, id, username, age):
        ...
