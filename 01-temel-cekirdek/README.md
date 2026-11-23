# Bölüm 01 · Yapay Zekâ Aslında Nasıl Düşünür?

**Seri:** Sıfırdan Kendi Yapay Zekâmızı İnşa Ediyoruz · **Sürüm:** `assistant.py · v0.1`  
**Benzetme:** Tahmin Makinesi

Yapay zekâ bir kâhin gibi “düşünmez”; her adımda en olası sonraki kelimeyi tahmin eder. Bu klasör, videoda kurulan çekirdeği gösterir: tek bir model çağrısı ve dönen yanıt.

## Ne öğretiyor?

- Bir dil modelini almak (`llm.get_model`)
- Ona bir soru sormak (`model.prompt(q).text()`)
- Yanıtın token token üretilen bir tahmin olduğunu görmek

`llm.py` bir öğretici taslaktır. Gerçek bir API’ye bağlanmaz.

## Nasıl çalıştırılır?

```bash
cd 01-temel-cekirdek
python assistant.py
```

Videodaki örnek çıktı:

```
Ben bir dil modeliyim. Her adımda
en olası sonraki kelimeyi tahmin
ederek yanıt üretiyorum.
```

## Kırılma

Motor çalışır — ama kendi belgelerimizi sorduğumuzda uydurur, çünkü henüz bir hafızası yoktur. Bunun devamı [02-rag-hafiza](../02-rag-hafiza) bölümündedir.

Seriyi [@techlas_](https://instagram.com/techlas_) hesabından takip edebilirsin.
