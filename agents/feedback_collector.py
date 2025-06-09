def collect_feedback(context):
    print("🗣️ Collecting feedback from user...")
    if context.get("mock_mode", True):
        context["feedback"].append("Looks good")
        context["workflow_done"] = True if len(context["feedback"]) >= 1 else False
    else:
        # Replace with real user input
        context["workflow_done"] = False
    return context
