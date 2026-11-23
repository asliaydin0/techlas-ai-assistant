"""Öğretici taslak — gerçek bir gömme modeli veya vektör veritabanı kullanmaz.

Videodaki `rag.split` / `rag.embed` / `db.search` akışını yerelde taklit eder.
Belgeler `docs/` klasöründen okunur; benzerlik için basit kelime örtüşmesi kullanılır.
"""

from pathlib import Path

_KOK = Path(__file__).resolve().parent


def split(path: str) -> list[dict]:
    klasor = _KOK / path
    parcalar = []
    for dosya in sorted(klasor.rglob("*")):
        if dosya.is_file():
            parcalar.append(
                {
                    "source": dosya.relative_to(_KOK).as_posix(),
                    "text": dosya.read_text(encoding="utf-8"),
                }
            )
    return parcalar


class _Kutuphane:
    def __init__(self, parcalar: list[dict]):
        self.parcalar = parcalar

    def search(self, q: str, k: int = 3) -> list[dict]:
        kelimeler = set(q.lower().split())
        def skor(parca: dict) -> int:
            metin = parca["text"].lower()
            return sum(1 for kelime in kelimeler if kelime in metin)

        sirali = sorted(self.parcalar, key=skor, reverse=True)
        return [parca for parca in sirali[:k] if skor(parca) > 0] or sirali[:k]


def embed(parts: list[dict]) -> _Kutuphane:
    return _Kutuphane(parts)
