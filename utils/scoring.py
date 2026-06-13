def calculate_score(
    chats,
    quizzes,
    notes
):
    return (
        chats * 2
        + quizzes * 5
        + notes * 3
    )