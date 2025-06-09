def parse_goal(context):
    goal = context.get("user_goal", "")
    print(f"🎯 Parsing goal: {goal}")
    if len(goal.split()) < 6:
        context["needs_clarification"] = True
    else:
        context["parsed_goal"] = goal.lower()
        context["needs_clarification"] = False
    return context
