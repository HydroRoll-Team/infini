from infini.typing import Literal


class Output:
    type: Literal["null", "text", "workflow"]
    name: str
    status: int
    block: bool

    def __init__(
        self,
        type: Literal["null", "text", "workflow"],
        name: str,
        *,
        status: int = 0,
        block: bool = False,
    ) -> None:
        self.type = type
        self.name = name
        self.status = status
        self.block = block

    @classmethod
    def empty(cls) -> "Output":
        return cls("null", "null", status=0, block=True)

    def is_empty(self) -> bool:
        return self.type == "null"
