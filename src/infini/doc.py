from typing import Dict, Optional, TypedDict

import json


class Annotation(TypedDict, total=False):
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

    def dumps(self) -> str:
        return json.dumps(
            {
                "pre_interceptors": self.pre_interceptors,
                "handlers": self.handlers,
                "events": self.events,
                "global_variables": self.global_variables,
                "interceptors": self.interceptors,
            }
        )
