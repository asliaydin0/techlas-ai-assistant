import llm, tools

def agent(goal: str) -> str:
    plan = llm.plan(goal)
    for step in plan:
        out = tools.run(step)
        if not llm.ok(out): retry(step)
    return "done"

print(agent("Teklifi hazırla ve mail at"))
