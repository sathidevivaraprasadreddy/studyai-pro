from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {
    "pdf"
}


def allowed_file(filename):
    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXTENSIONS
    )


def sanitize_filename(filename):
    return secure_filename(
        filename
    )