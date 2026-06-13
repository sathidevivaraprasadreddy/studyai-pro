import json
import os

MEMORY_FILE = "memory/user_memory.json"

DEFAULT_MEMORY = {
    "topics_studied": [],
    "weak_topics": [],
    "quiz_scores": [],
    "learning_level": "Beginner",
    "last_roadmap": "",
    "preferred_subjects": []
}


def init_memory():
    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump(
                DEFAULT_MEMORY,
                f,
                indent=4
            )


def load_memory():
    init_memory()

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(
            data,
            f,
            indent=4
        )


def add_topic(topic):
    memory = load_memory()

    if topic not in memory["topics_studied"]:
        memory["topics_studied"].append(topic)

    save_memory(memory)


def add_weak_topic(topic):
    memory = load_memory()

    if topic not in memory["weak_topics"]:
        memory["weak_topics"].append(topic)

    save_memory(memory)


def add_quiz_score(score):
    memory = load_memory()

    memory["quiz_scores"].append(score)

    save_memory(memory)


def update_learning_level():
    memory = load_memory()

    scores = memory["quiz_scores"]

    if not scores:
        level = "Beginner"
    else:
        average = sum(scores) / len(scores)

        if average >= 85:
            level = "Advanced"
        elif average >= 60:
            level = "Intermediate"
        else:
            level = "Beginner"

    memory["learning_level"] = level

    save_memory(memory)


def save_roadmap(roadmap):
    memory = load_memory()

    memory["last_roadmap"] = roadmap

    save_memory(memory)


def get_memory_summary():
    memory = load_memory()

    scores = memory["quiz_scores"]

    average = (
        sum(scores) / len(scores)
        if scores else 0
    )

    return {
        "topics_studied": memory["topics_studied"],
        "weak_topics": memory["weak_topics"],
        "average_score": round(average, 2),
        "learning_level": memory["learning_level"],
        "last_roadmap": memory["last_roadmap"],
        "preferred_subjects": memory["preferred_subjects"]
    }


def reset_memory():
    save_memory(DEFAULT_MEMORY)