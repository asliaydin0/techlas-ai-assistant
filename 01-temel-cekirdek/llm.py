"""Öğretici taslak — gerçek bir dil modeline bağlanmaz, API anahtarı istemez.

`get_model("gpt-4o")` yalnızca videodaki örnek çağrıyı taklit eder.
Model adı bir etikettir; dışarıya istek gönderilmez.
"""


class _Yanit:
    def __init__(self, metin: str):
        self._metin = metin

    def text(self) -> str:
        return self._metin


class _Model:
    def prompt(self, q: str) -> _Yanit:
        soru = q.strip().lower()
        if "kimsin" in soru:
            return _Yanit(
                "Ben bir dil modeliyim. Her adımda\n"
                "en olası sonraki kelimeyi tahmin\n"
                "ederek yanıt üretiyorum."
            )
        return _Yanit("Bu öğretici taslak yalnızca videodaki örneği üretir.")


def get_model(name: str) -> _Model:
    return _Model()
