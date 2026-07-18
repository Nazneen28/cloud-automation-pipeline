"""
GitFlow Portfolio — Demo App
Author: Nazneen
Phase 1 | Week 4 | Cloud Engineering Roadmap
"""

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Cloud Engineering."

def add(a: int, b: int) -> int:
    return a + b

def get_status() -> dict:
    return {
        "project": "GitFlow Portfolio",
        "author": "Nazneen",
        "phase": "Phase 1 - Foundations",
        "week": "Week 4 - Git & GitHub",
        "status": "active"
    }

if __name__ == "__main__":
    print(greet("Nazneen"))
    print(get_status())