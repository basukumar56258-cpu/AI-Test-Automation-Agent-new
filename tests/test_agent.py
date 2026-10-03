from backend.app.agents.test_agent import TestAutomationAgent

def test_generates_login_cases():
    cases=TestAutomationAgent().generate("login page")
    assert any("Valid login" in x["title"] for x in cases)
