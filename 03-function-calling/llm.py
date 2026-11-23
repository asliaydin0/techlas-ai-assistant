"""Öğretici taslak — gerçek bir dil modeline bağlanmaz, API anahtarı istemez.

`pick_tool`, hedef metnine bakarak videodaki gibi bir araç seçer.
"""


def pick_tool(goal: str, box: list) -> str:
    metin = goal.lower()
    if "mail" in metin or "e-posta" in metin or "eposta" in metin:
        return "mail.send"
    if "takvim" in metin or "calendar" in metin or "toplantı" in metin:
        return "calendar.check"
    if "ara" in metin or "search" in metin:
        return "search.query"
    if box:
        return f"{box[0].name}.run"
    return "unknown"
