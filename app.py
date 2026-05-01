from flask import Flask, request, send_file
import subprocess, uuid, os

app = Flask(__name__)

@app.route("/compile", methods=["POST"])
def compile_typst():
    content = request.data.decode()
    name = str(uuid.uuid4())

    typ_file = f"/tmp/{name}.typ"
    pdf_file = f"/tmp/{name}.pdf"

    with open(typ_file, "w") as f:
        f.write(content)

    subprocess.run(["typst", "compile", typ_file, pdf_file])

    return send_file(pdf_file, mimetype="application/pdf")
