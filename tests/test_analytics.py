from database.analytics import (
    init_analytics,
    increment,
    get_analytics
)


def test_increment():

    init_analytics()

    before = get_analytics()[
        "uploads"
    ]

    increment("uploads")

    after = get_analytics()[
        "uploads"
    ]

    assert after == before + 1