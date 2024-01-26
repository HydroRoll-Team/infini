from infini.typing import Dict, Any, Generic, T


class Input(Generic[T]):
    plain_data: T
    variables: Dict[str, Any]

    def __init__(self, plain_data: T, variables: Dict[str, Any] | None = None) -> None:
        self.plain_data = plain_data
        self.variables = variables or {}

    def get_session_id(self) -> str:
        if session_id := self.variables.get("session_id"):
            return session_id

        user_id = self.variables.get("user_id", "unknown")
        group_id = self.variables.get("group_id", "unknown")
        return f"session_{group_id}_{user_id}"

    def get_plain_text(self) -> str:
        return str(self.plain_data)
