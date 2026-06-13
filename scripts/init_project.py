from database import (
    init_db,
    init_analytics
)

from memory.user_memory import (
    init_memory
)

print("Initializing...")

init_db()
init_analytics()
init_memory()

print("Done.")