import llm

model = llm.get_model("gpt-4o")

def ask(q: str) -> str:
    return model.prompt(q).text()

print(ask("Sen kimsin?"))
