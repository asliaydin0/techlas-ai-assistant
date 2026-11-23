"""Öğretici taslak — gerçek bir e-posta, takvim veya arama servisine bağlanmaz.

Videodaki `tools.mail`, `tools.calendar`, `tools.search` ve `tools.run`
çağrılarını yerelde taklit eder. Gerçek mail gönderilmez.
"""


class Tool:
    def __init__(self, name: str):
        self.name = name


mail = Tool("mail")
calendar = Tool("calendar")
search = Tool("search")


def run(step: str) -> str:
    if step == "mail.send":
        return "tool: mail.send\nstatus: sent · 3 alıcı"
    if step == "calendar.check":
        return "tool: calendar.check\nstatus: 2 boşluk bulundu"
    if step == "search.query":
        return "tool: search.query\nstatus: 5 sonuç"
    return f"tool: {step}\nstatus: ok"
