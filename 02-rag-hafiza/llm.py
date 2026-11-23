"""Öğretici taslak — gerçek bir dil modeline bağlanmaz, API anahtarı istemez.

`ask(q, context=...)` verilen belge parçalarına bakarak videodaki örneği üretir.
"""


def ask(q: str, context: list[dict] | None = None) -> str:
    birlesik = "\n".join(parca.get("text", "") for parca in (context or []))
    metin = f"{q}\n{birlesik}".lower()
    if "429" in metin or "limit" in metin or "istek" in q.lower():
        return "İstek limiti aşıldı; 60 sn bekle."
    if context:
        return context[0]["text"].strip().splitlines()[0]
    return "Bu öğretici taslak yalnızca videodaki örneği üretir."
