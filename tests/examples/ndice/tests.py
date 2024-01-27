from infini.loader import Loader
from infini.input import Input
from pathlib import Path
from ipm import api
from ipm.models.ipk import InfiniProject

ipk = InfiniProject()
api.build(".")
api.install(f"dist/{ipk.default_name}", force=True)

loader = Loader()
loader.load("ndice")
loader.close()

core = loader.into_core()
for output in core.input(Input(".r20#d6")):
    print(output)
