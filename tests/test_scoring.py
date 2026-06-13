from utils.scoring import calculate_score

def test_calculate_score():

    score = calculate_score(
        chats=5,
        quizzes=2,
        notes=3
    )

    assert score == 29