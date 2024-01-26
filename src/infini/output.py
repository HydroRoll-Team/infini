from infini.typing import Literal


class Output:
    type: Literal["null", "text", "workflow"]
    name: str
    status: int
    block: bool

    @classmethod
    def empty(cls) -> "Output":
        output = cls()
        output.type = "null"
        output.status = 0
        output.block = True
        return output

    def is_empty(self) -> bool:
        return self.type == "null"
