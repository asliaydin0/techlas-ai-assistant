import llm, rag

parts = rag.split("docs/")
db = rag.embed(parts)

def ask(q: str) -> str:
    ctx = db.search(q, k=3)
    return llm.ask(q, context=ctx)

print(ask("429 hatası ne demek?"))
