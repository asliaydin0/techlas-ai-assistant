# Bölüm 03 · Yapay Zekâya El Kol Vermek

**Seri:** Sıfırdan Kendi Yapay Zekâmızı İnşa Ediyoruz · **Sürüm:** `assistant.py · v0.3`  
**Benzetme:** Danışmandan Asistana

Bir danışman sana ne yapman gerektiğini söyler. Bir asistan söyler ve yapar: mail atar, takvime bakar, arama yapar. İşte tool / function calling tam olarak budur.

## Ne öğretiyor?

- Modele kullanılabilir araçlar tanıtmak (`box = [tools.mail, tools.calendar, tools.search]`)
- Hedefe göre doğru aracı seçmek (`llm.pick_tool`)
- Seçilen adımı çalıştırmak (`tools.run`)

`llm.py` ve `tools.py` öğretici taslaktır. Gerçek mail gönderilmez, API anahtarı istenmez.

## Nasıl çalıştırılır?

```bash
cd 03-function-calling
python assistant.py
```

Videodaki örnek çıktı:

```
tool: mail.send
status: sent · 3 alıcı
```

## Kırılma

Elleri vardır — ama “müşteriye teklifi hazırla ve mail at” gibi birden fazla adımlı bir hedefte takılır, çünkü henüz bir planı yoktur. Bunun devamı [04-otonom-agent](../04-otonom-agent) bölümündedir.

Seriyi [@techlas_](https://instagram.com/techlas_) hesabından takip edebilirsin.
