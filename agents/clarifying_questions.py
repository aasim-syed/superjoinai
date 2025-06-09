def ask_clarifying_questions(context):
    if context.get("needs_clarification", False):
        print("❓ Your goal seems a bit vague.")
        refined = input("🔁 Please refine your goal: ")
        context["parsed_goal"] = refined.lower()
        context["needs_clarification"] = False
    return context
