from typing import Optional

import attr


@attr.dataclass
class User:
    username: str
    age: int
    id: Optional[int] = None
