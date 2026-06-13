MAX_MEMORY = 20

conversation_memory = []


def save_memory(user, ai):
    """
    Save conversation to runtime memory.
    """

    conversation_memory.append({
        "user": user,
        "ai": ai
    })

    if len(conversation_memory) > MAX_MEMORY:
        conversation_memory.pop(0)


def get_memory():
    """
    Get current runtime memory.
    """

    return conversation_memory


def clear_memory():
    """
    Clear runtime memory.
    """

    conversation_memory.clear()