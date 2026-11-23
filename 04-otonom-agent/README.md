# Bölüm 04 · Kendi Kararını Veren Yapay Zekâ

**Seri:** Sıfırdan Kendi Yapay Zekâmızı İnşa Ediyoruz · **Sürüm:** `assistant.py · v0.4`  
**Benzetme:** Stajyer vs. Proje Yöneticisi

Stajyer her adımda sana sorar. Proje yöneticisi hedefi parçalar, sırayla yapar, sonucu kontrol eder, gerekirse yeniden dener. İşte agent döngüsü tam olarak budur.

## Ne öğretiyor?

- Hedefi bir plana çevirmek (`llm.plan`)
- Adımları sırayla çalıştırmak (`tools.run`)
- Sonucu kontrol edip gerekirse yeniden denemek (`llm.ok`, `retry`)

`llm.py` ve `tools.py` öğretici taslaktır. Gerçek bir modele veya servise bağlanmazlar.

Videoda `retry(step)` ayrıca import edilmeden görünür. `tools` içe aktarılınca bu isim öğretici olarak tanımlanır; böylece ekrandaki kod olduğu gibi çalışır.

## Nasıl çalıştırılır?

```bash
cd 04-otonom-agent
python assistant.py
```

Videodaki terminal özeti:

```
plan: 3 adım
loop: search → write → mail · done
```

`agent` fonksiyonu ekrandaki gibi `"done"` döner; bu yüzden çalıştırınca son satırda bir de `done` görürsün.

## Kırılma

Zekâsı vardır, planlar ve araç kullanır — ama hâlâ siyah bir terminal ekranındadır, bir yüzü (arayüzü) yoktur. Bunun devamı [05-canli-urun](../05-canli-urun) bölümünde olacak.

Seriyi [@techlas_](https://instagram.com/techlas_) hesabından takip edebilirsin.
