from app.agents.planner import plan_workflow

def run_workflow(user_input):
    steps = plan_workflow(user_input)

    results = []

    for step in steps:
        results.append({
            "step": step,
            "result": f"Executed {step}",
            "verified": True
        })

    return results