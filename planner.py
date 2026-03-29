def plan_workflow(user_input):
    user_input = user_input.lower()

    if "employee" in user_input:
        return [
            "Collect employee documents",
            "Create employee account",
            "Assign onboarding tasks",
            "Send welcome email"
        ]

    elif "procurement" in user_input:
        return [
            "Receive purchase request",
            "Approve budget",
            "Select vendor",
            "Place order",
            "Process payment"
        ]

    elif "hospital" in user_input:
        return [
            "Register patient",
            "Assign doctor",
            "Conduct diagnosis",
            "Prescribe treatment",
            "Discharge patient"
        ]

    else:
        return [
            "Analyze request",
            "Break into steps",
            "Execute workflow",
            "Verify completion"
        ]