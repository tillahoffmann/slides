from flask.app import Flask, request
from flask import render_template, Response, send_from_directory
import frontmatter
from pathlib import Path
import yaml
from .util import apply_defaults_and_validate


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Return a landing page to select and launch slides without the browser toolbar.
    """
    # Return the landing page if there is no document.
    document = request.args.get("document")
    if not document:
        document_options = [document.name for document in Path.cwd().glob("*.md")]
        return render_template("index.html", document_options=document_options)

    # Process the document and render it as slides.
    with open(Path(__file__).parent / "frontmatter.schema.yaml") as fp:
        schema = yaml.safe_load(fp)
    metadata = apply_defaults_and_validate(frontmatter.load(document).metadata, schema)
    # Apply non-trivial transformations.
    if isinstance(css := metadata.setdefault("css", []), str):
        metadata["css"] = [css]
    metadata.setdefault("title", document)
    return render_template("slides.html", document=document, **metadata)


@app.route("/md/<document>/")
def markdown_content(document: str) -> str:
    """
    Get the raw markdown content.
    """
    return frontmatter.load(document).content


@app.route('/<path:filename>')
def assets(filename: Path) -> Response:
    """
    Send assets as is if the pattern is not matched by another handler.
    """
    return send_from_directory(Path.cwd(), filename)
