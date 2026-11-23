# Bölüm 02 · Yapay Zekâya Hafıza Kazandırmak

**Seri:** Sıfırdan Kendi Yapay Zekâmızı İnşa Ediyoruz · **Sürüm:** `assistant.py · v0.2`  
**Benzetme:** Açık Kitap Sınavı

Kapalı kitap sınavında bilmediğin soruya bir şeyler uydurursun. Kitap açıksa önce doğru sayfayı bulur, cevabı oradan yazarsın. İşte RAG (Retrieval-Augmented Generation) tam olarak budur.

## Ne öğretiyor?

- Belgeleri parçalara bölmek (`rag.split`)
- Parçaları aranabilir hale getirmek (`rag.embed`)
- Soruya en yakın parçaları bulup modele bağlam olarak vermek (`db.search` + `llm.ask`)

`llm.py` ve `rag.py` öğretici taslaktır. Gerçek bir gömme API’si veya vektör veritabanı kullanılmaz. Örnek belge videodaki `docs/limits.md` dosyasıdır.

## Nasıl çalıştırılır?

```bash
cd 02-rag-hafiza
python assistant.py
```

Videodaki örnek çıktı:

```
İstek limiti aşıldı; 60 sn bekle.
```

## Kırılma

Artık bir hafızası vardır — ama “bu cevabı ekibe mail olarak at” deyince yapamaz, çünkü henüz elleri (araçları) yoktur. Bunun devamı [03-function-calling](../03-function-calling) bölümündedir.

Seriyi [@techlas_](https://instagram.com/techlas_) hesabından takip edebilirsin.
