def execute_tasks(context):
    print("🔧 Executing tasks...")
    mock_mode = context.get("mock_mode", True)
    for task in context.get("tasks", []):
        if mock_mode:
            print(f"✅ [MOCK] Executed: {task['name']} via {task['tool']}")
        else:
            print(f"🚀 Actually running: {task['name']} with tool {task['tool']}")
    return context
