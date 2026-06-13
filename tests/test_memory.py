from memory.user_memory import (
    add_topic,
    load_memory
)


def test_add_topic():

    add_topic(
        "Machine Learning"
    )

    memory = load_memory()

    assert (
        "Machine Learning"
        in
        memory["topics_studied"]
    )