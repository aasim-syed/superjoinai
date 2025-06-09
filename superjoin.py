from langgraph.graph import StateGraph
from agents.parse_goal import parse_goal
from agents.clarifying_questions import ask_clarifying_questions
from agents.task_planner import plan_tasks
from agents.execute_task import execute_tasks
from agents.feedback_collector import collect_feedback


def build_workflow_graph():
    graph = StateGraph(dict)

    graph.add_node("ParseGoal", parse_goal)
    graph.add_node("AskQuestions", ask_clarifying_questions)
    graph.add_node("PlanTasks", plan_tasks)
    graph.add_node("ExecuteTasks", execute_tasks)
    graph.add_node("CollectFeedback", collect_feedback)

    graph.set_entry_point("ParseGoal")
    graph.add_edge("ParseGoal", "AskQuestions")
    graph.add_edge("AskQuestions", "PlanTasks")
    graph.add_edge("PlanTasks", "ExecuteTasks")
    graph.add_edge("ExecuteTasks", "CollectFeedback")

    graph.add_conditional_edges(
        "CollectFeedback",
        lambda context: "Stop" if context.get("workflow_done") else "AskQuestions",
        {"AskQuestions": "AskQuestions", "Stop": "__end__"}
    )

    return graph.compile()


if __name__ == "__main__":
    user_goal = input("📝 What would you like to achieve today? > ")

    context = {
        "user_goal": user_goal,
        "tools": ["email_sender", "linkedin_poster", "calendar_api"],
        "memory": {},
        "feedback": [],
        "mock_mode": True
    }
    workflow = build_workflow_graph()
    final_context = workflow.invoke(context)
    print("\n✅ FINAL CONTEXT:\n", final_context)
