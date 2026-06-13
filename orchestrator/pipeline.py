from agents.planner_agent import (
    plan_query
)

from agents.retrieval_agent import (
    retrieve_context
)

from agents.tutor_agent import (
    tutor_prompt
)

from agents.verifier_agent import (
    verify_prompt
)

from utils.ai_manager import (
    generate_response
)

from database.database import (
    save_chat
)

from database.analytics import (
    increment
)

from memory.runtime_memory import (
    save_memory
)


def run_agent_pipeline(
    user_query
):

    increment("agent_calls")

    plan = plan_query(
        user_query
    )

    context = retrieve_context(
        user_query,
        k=5
    )

    answer_prompt = tutor_prompt(
        user_query,
        context
    )

    answer = generate_response(
        answer_prompt
    )

    verification_prompt = verify_prompt(
        answer
    )

    final_answer = generate_response(
        verification_prompt
    )

    save_chat(
        user_query,
        final_answer,
        "pipeline"
    )

    save_memory(
        user_query,
        final_answer
    )

    increment("chats")

    return {
        "plan": plan,
        "context": context,
        "answer": final_answer
    }