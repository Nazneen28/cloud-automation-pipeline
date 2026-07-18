"""
Cloud Automation Pipeline
Author: Nazneen
Phase 1 | Week 4 | Cloud Engineering Roadmap
"""

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Cloud Engineering."

def add(a: int, b: int) -> int:
    return a + b

def get_status() -> dict:
    return {
        "project": "Cloud Automation Pipeline",
        "author": "Nazneen",
        "phase": "Phase 1 - Cloud Foundations",
        "week": "Week 4 - Git & CI/CD",
       
        "status": "active"
    }

if __name__ == "__main__":
    print(greet("Nazneen"))
    print(get_status())