from typing import Dict, Optional, TypedDict


class Annotation(TypedDict):
    usage: Optional[str]
    description: Optional[str]
    epilog: Optional[str]


class Doc:
    pre_interceptors: Dict[str, Annotation]
    handlers: Dict[str, Annotation]
    events: Dict[str, Annotation]
    global_variables: Dict[str, Annotation]
    interceptors: Dict[str, Annotation]

    def __init__(self) -> None:
        self.pre_interceptors = {}
        self.handlers = {}
        self.events = {}
        self.global_variables = {}
        self.interceptors = {}
