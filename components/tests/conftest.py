import pytest
from unittest.mock import Mock


from components.chat_backend.chat.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def user():
    return dataclasses.User(
        id=1,
        username='alex',
        age=10,
    )

@pytest.fixture(scope='function')
def users_repo(user):
    users_repo = Mock(interfaces.UsersRepo)
    users_repo.add_user = Mock(return_value=user)
    return users_repo
