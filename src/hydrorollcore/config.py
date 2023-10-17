from pydantic import BaseModel


class Config(BaseModel):
    rule_dir: list = []
    rules: list = []

