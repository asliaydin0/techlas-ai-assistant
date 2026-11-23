import llm, tools

box = [tools.mail, tools.calendar, tools.search]

def act(goal: str) -> str:
    step = llm.pick_tool(goal, box)
    return tools.run(step)

print(act("Bu özeti ekibe mail at"))
