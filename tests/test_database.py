from database.database import (
    init_db,
    save_chat,
    get_chats
)

init_db()


def test_save_chat():

    save_chat(
        "Hello",
        "Hi"
    )

    chats = get_chats()

    assert len(chats) > 0

    assert chats[0][1] == "Hello"