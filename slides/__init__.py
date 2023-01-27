from flask.app import Flask, request
from flask import make_response, render_template
import frontmatter

DEFAULT_METADATA = {
    "theme": "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.4.0/theme/white.min.css",
    "highlight_theme": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/"
    "default.min.css",
}

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/slides/")
def document() -> str:
    """
    Get the slides for the given markdown document.
    """
    if not (document := request.args.get("document")):
        return make_response("specify a document with ?document=markdown/path", 400)
    metadata = DEFAULT_METADATA | frontmatter.load(document).metadata
    if isinstance(css := metadata.setdefault("css", []), str):
        metadata["css"] = [css]
    return render_template("slides.html", document=document, **metadata)


@app.route("/markdown/")
def markdown() -> str:
    """
    Get the raw markdown code.
    """
    document = request.args["document"]
    return frontmatter.load(document).content
