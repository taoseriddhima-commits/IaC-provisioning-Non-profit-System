# Entry Point

from backend.agents.orchestrator import TriageOrchestrator


if __name__ == "__main__":
    sample_message = (
        "Hi, my name is Sarah Johnson. "
        "I donated $200 on January 5th but the payment failed. "
        "Please contact me at sarah@email.com."
    )

    orchestrator = TriageOrchestrator()
    result = orchestrator.run(sample_message)

    print("FINAL OUTPUT:")
    print(result)
