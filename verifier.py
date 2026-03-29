def verify_step(step, result):
    if result["status"] == "success":
        return True
    return False