from utils.validators import (
    allowed_file,
    sanitize_filename
)


def test_allowed_pdf():
    assert allowed_file("notes.pdf")


def test_reject_exe():
    assert not allowed_file("virus.exe")


def test_reject_docx():
    assert not allowed_file("notes.docx")


def test_secure_filename():
    filename = sanitize_filename(
        "../../../hack.pdf"
    )

    assert filename == "hack.pdf"