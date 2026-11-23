"""Öğretici taslak — gerçek bir arama, yazma veya e-posta servisine bağlanmaz.

Videodaki `tools.run` ve `retry` çağrılarını yerelde taklit eder.
`assistant.py` ekranda `retry(step)` diye geçer; tools içe aktarılınca
bu isim öğretici olarak görünür hale gelir. Gerçek servis çağrısı yoktur.
"""

import builtins

_adimlar: list[str] = []


def run(step: str) -> str:
    _adimlar.append(step)
    cikti = f"tool: {step}\nstatus: ok"
    if len(_adimlar) == 3:
        zincir = " → ".join(_adimlar)
        print(f"loop: {zincir} · done")
    return cikti


def retry(step: str) -> str:
    """Başarısız sayılan adımı videodaki gibi yeniden dener."""
    return run(step)


# Ekrandaki kod `import llm, tools` sonrası doğrudan retry(step) yazar.
# Bu kayıt yalnızca o satırın API'siz çalışması içindir.
builtins.retry = retry
