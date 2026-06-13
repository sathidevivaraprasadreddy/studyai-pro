import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from orchestrator.pipeline import (
    run_agent_pipeline
)

query = input(
    "Question: "
)

result = run_agent_pipeline(
    query
)

print("\nPLAN:\n")
print(result["plan"])

print("\nANSWER:\n")
print(result["answer"])

print("\nCITATIONS:\n")

for item in result["context"]:

    print(
        f"{item['filename']} "
        f"(Page {item['page']})"
    )