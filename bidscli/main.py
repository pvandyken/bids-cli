from bids import BIDSLayout, BIDSLayoutIndexer
from pathlib import Path
import typer

app = typer.Typer()

@app.command()
def main(root: Path, entities: list[str]):
    matches = [re.match(r"^([^\d\W]\w*)=(?!.*=)(.*)$", value) for value in entities]
    layout = BIDSLayout(
        root,
        validate=False,
        indexer=BIDSLayoutIndexer(validate=False, index_metadata=False),
        database_path=".pydb"
    )
    if all(matches):
        for obj in layout.get(
            **{str(m.group(1)): str(m.group(2)) for m in matches},  # type: ignore
        ):
            print(obj.path)

