audit_log = []

def log_action(step, decision, result):
    audit_log.append({
        "step": step,
        "decision": decision,
        "result": result
    })