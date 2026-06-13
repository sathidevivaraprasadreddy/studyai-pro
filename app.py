import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)

from werkzeug.utils import secure_filename

from orchestrator.pipeline import (run_agent_pipeline)

from utils.pdf_utils import (
    extract_text_from_pdf
)

from utils.chunking import (
    chunk_text
)

from utils.vector_store import (
    add_chunks
)

from werkzeug.exceptions import (
    RequestEntityTooLarge
)
from utils.validators import (
    allowed_file,
    sanitize_filename
)
from utils.ai_manager import generate_response

from agents.quiz_agent import generate_quiz_prompt
from agents.flashcard_agent import generate_flashcards_prompt
from agents.notes_agent import generate_notes_prompt
from agents.assessment_agent import assessment_prompt
from agents.roadmap_agent import roadmap_prompt
from utils.vector_store import load_chunks
from database.analytics import get_analytics
from memory.user_memory import get_memory_summary
from database.analytics import increment
from utils.logger import logger
from config import Config
from database.analytics import init_analytics
from database.database import (
    init_db
)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app = Flask(__name__)

app.config.from_object(Config)

init_db()

init_analytics()

app.config[
    "MAX_CONTENT_LENGTH"
] = Config.MAX_CONTENT_LENGTH

os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)

def get_all_content():
    chunks = load_chunks()

    return "\n".join(
        chunk["text"]
        for chunk in chunks[:100]
    )

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "GET":
        return render_template(
            "upload.html"
        )

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "error": "No file selected."
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "error": "Only PDF files are allowed."
        }), 400

    filename = sanitize_filename(
        file.filename
    )

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    try:

        file.save(filepath)

        pdf_data = extract_text_from_pdf(
            filepath
        )

        chunks = []

        for page in pdf_data["pages"]:

            page_chunks = chunk_text(
                page["content"]
            )

            for chunk in page_chunks:

                chunks.append({
                    "text": chunk,
                    "filename": filename,
                    "page": page["page"]
                })

        add_chunks(chunks)

        increment("uploads")

        from flask import flash
        
        flash("PDF uploaded successfully!")
        
        return redirect(url_for("home"))

    except Exception as e:

        logger.exception(str(e))

        return jsonify({
            "error": str(e)
        }), 500    


@app.route(
    "/chat",
    methods=["GET", "POST"]
)
def chat():

    answer = ""

    citations = []

    question = ""

    if request.method == "POST":

        question = request.form.get(
            "question"
        )

        result = run_agent_pipeline(
            question
        )

        answer = result["answer"]

        citations = result["context"]

        increment("chats")

    return render_template(
        "chat.html",
        answer=answer,
        citations=citations,
        question=question
    )

@app.route("/quiz")
def quiz():

    content = get_all_content()

    prompt = generate_quiz_prompt(content)

    result = generate_response(prompt)

    increment("quizzes")

    return render_template(
        "tool.html",
        title="Quiz",
        content=result
    )

@app.route("/flashcards")
def flashcards():

    content = get_all_content()

    prompt = generate_flashcards_prompt(
        content
    )

    result = generate_response(
        prompt
    )

    increment("flashcards")

    return render_template(
        "tool.html",
        title="Flashcards",
        content=result
    )
@app.route("/notes")
def notes():

    content = get_all_content()

    prompt = generate_notes_prompt(
        content
    )

    result = generate_response(
        prompt
    )

    increment("notes")

    return render_template(
        "tool.html",
        title="Revision Notes",
        content=result
    )

@app.route("/assessment")
def assessment():

    content = get_all_content()

    prompt = assessment_prompt(
        content
    )

    result = generate_response(
        prompt
    )

    increment("assessments")

    return render_template(
        "tool.html",
        title="Assessment",
        content=result
    )

@app.route("/roadmap")
def roadmap():

    topic = request.args.get(
        "topic",
        "General Study"
    )

    prompt = roadmap_prompt(
        topic
    )

    result = generate_response(
        prompt
    )

    increment("roadmaps")

    return render_template(
        "tool.html",
        title="Learning Roadmap",
        content=result
    )        


@app.route("/dashboard")
def dashboard():

    analytics = get_analytics()

    memory = get_memory_summary()

    return render_template(
        "dashboard.html",
        analytics=analytics,
        memory=memory
    )



@app.route("/test-error")
def test_error():
    1/0

@app.errorhandler(
    RequestEntityTooLarge
)
def handle_large_file(error):

    return render_template(
        "error.html",
        message=(
            "File too large. "
            "Maximum size is 50 MB."
        )
    ), 413


if __name__ == "__main__":
    print(app.url_map)

    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )












