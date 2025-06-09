from difflib import SequenceMatcher

def fuzzy_match(goal, keyword, threshold=0.3):
    score = SequenceMatcher(None, goal.lower(), keyword.lower()).ratio()
    print(f"🔍 Fuzzy match: '{goal}' vs '{keyword}' → score: {score:.2f}")
    return score >= threshold

def plan_tasks(context):
    print("🧠 Planning tasks...")
    goal = context.get("parsed_goal", "")
    tasks = []

    email_keywords = ["email", "invite", "send invites", "announcement", "notification"]
    calendar_keywords = ["calendar", "webinar", "schedule", "event", "meeting", "zoom"]
    social_keywords = ["linkedin", "post", "promotion", "social media", "share"]

    matched = False

    print("🧪 Checking email keywords...")
    for kw in email_keywords:
        if fuzzy_match(goal, kw):
            tasks.append({"name": "Send Email Invites", "tool": "email_sender"})
            matched = True
            break

    print("🧪 Checking calendar keywords...")
    for kw in calendar_keywords:
        if fuzzy_match(goal, kw):
            tasks.append({"name": "Schedule Webinar", "tool": "calendar_api"})
            matched = True
            break

    print("🧪 Checking social media keywords...")
    for kw in social_keywords:
        if fuzzy_match(goal, kw):
            tasks.append({"name": "Post on LinkedIn", "tool": "linkedin_poster"})
            matched = True
            break

    if not matched:
        print("⚠️ Couldn't infer tasks from your goal.")
        custom_task = input("📝 Please describe a task you want me to perform: ")
        tasks.append({"name": custom_task, "tool": "default_tool"})

    context["tasks"] = tasks
    return context
