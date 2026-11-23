"""Öğretici taslak — gerçek bir dil modeline bağlanmaz, API anahtarı istemez.

`plan`, videodaki üç adımlı agent döngüsünü üretir: search → write → mail.
`ok`, adım çıktısının başarılı sayılıp sayılmayacağına karar verir.
"""


def plan(goal: str) -> list[str]:
    print("plan: 3 adım")
    return ["search", "write", "mail"]


def ok(out: str) -> bool:
    metin = (out or "").lower()
    return "fail" not in metin and "error" not in metin
