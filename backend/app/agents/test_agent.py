import json

class TestAutomationAgent:
    """LLM-agnostic agent. Replace generate_with_llm with your provider call."""

    def generate(self, requirement: str):
        r = requirement.lower()
        cases = [
            {"title":"Happy path","steps":["Open application","Perform the main user action"],"expected":"Action completes successfully"},
            {"title":"Validation","steps":["Open application","Submit incomplete/invalid data"],"expected":"Clear validation message is shown"},
            {"title":"Error handling","steps":["Trigger an invalid request"],"expected":"Application handles the error without crashing"},
        ]
        if "login" in r:
            cases += [
                {"title":"Valid login","steps":["Open login page","Enter valid credentials","Click Login"],"expected":"User reaches dashboard"},
                {"title":"Invalid password","steps":["Open login page","Enter valid email and wrong password","Click Login"],"expected":"Login is rejected with an error"},
            ]
        return cases
