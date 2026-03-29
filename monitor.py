def monitor_workflow(step_result):
    if step_result["status"] != "success":
        return "retry"
    return "ok"