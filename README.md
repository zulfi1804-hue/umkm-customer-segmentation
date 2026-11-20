# Segmentasi Pelanggan UMKM (UMKM Customer Segmentation) · Tim Selalu Sukses
**Kasus:** 05 - Segmentasi - UMKM · **Aplikasi:** https://umkm-customer-segmentation.streamlit.app/  · **Video:** [tautan video]

| Anggota | NIM | Bagian yang dikerjakan |
|---|---|---|
| Kholistiyani Zulfi | 2403118 | Pembuatan model dan laporan|
| Atsnaina Habibah | 2401340 | Pembuatan aplikasi dan video |

## Masalah dan pengguna

Proyek ini ditujukan untuk membantu pemilik dan pengelola UMKM bakery dan coffee di Bandung memahami karakteristik pelanggan berdasarkan perilaku transaksi. Model membantu mengelompokkan pelanggan ke dalam segmen yang berbeda sehingga UMKM dapat menentukan strategi pemasaran yang lebih tepat, seperti pemberian promo, program loyalitas, dan kampanye untuk pelanggan yang mulai tidak aktif.

## Data dan pembersihan

| Masalah yang ditemukan | Jumlah baris | Cara menangani |
|---|---|---|
| Duplikat identik | 90 | Dihapus menggunakan drop_duplicates() |
| ID pelanggan berulang | 150 baris berlebih Mempertahankan data dengan aktivitas transaksi paling baru berdasarkan hari_sejak_transaksi_terakhir |
| Missing value pada umur | 208 | Nilai kosong diisi menggunakan median (28) |
| Missing value pada rating | 812 | Nilai kosong diisi menggunakan median (4,2) |
 Nilai umur tidak valid | Tidak didokumentasikan secara terpisah | Nilai 0, 1, 99, dan 120 diubah menjadi missing value, kemudian diimputasi dengan median |
| Format total belanja tidak konsisten | Tidak didokumentasikan secara terpisah | Dibersihkan dan dikonversi menjadi tipe numerik |
| Format tanggal pendaftaran | - | Dikonversi menjadi datetime |

Feature engineering dilakukan dengan membuat fitur lama_bergabung_hari berdasarkan tanggal acuan 30 Juni 2026.

Enam fitur yang digunakan pada model akhir:

jumlah_transaksi_6bln

total_belanja_rp

hari_sejak_transaksi_terakhir

persen_pakai_promo

rating_rata

lama_bergabung_hari

## Hasil

Model menggunakan algoritma K-Means. Empat eksperimen dengan kombinasi fitur yang berbeda dibandingkan menggunakan metrik evaluasi internal clustering.

| Model | Silhouette Score | Davies–Bouldin Index | Calinski–Harabasz Index |
|---|---|---|---|
| *Baseline: Model 1 (K-Means, K=10)* [nama *baseline*] | 0,2095 | 1,8594 | 585,93 |
| Model final: Model 4 (K-Means, K=4) | 0,3696 | 1,1289 | 5.660,67 |

*Threshold* yang dipakai: Tidak berlaku. K-Means merupakan algoritma clustering yang tidak menggunakan threshold klasifikasi. Jumlah cluster akhir ditetapkan sebanyak 4 berdasarkan perbandingan metrik evaluasi dan interpretasi karakteristik pelanggan.

## Cara menjalankan

```bash
pip install -r requirements.txt
python -m streamlit run app/app.py #api dan aplikasi

```
Aplikasi juga dapat diakses secara online melalui:

https://umkm-customer-segmentation.streamlit.app/

## Struktur repositori

```
umkm-customer-segmentation/
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── model_final.joblib
├── notebooks/
│   └── 01_data_understanding.ipynb
├── reports/
│   └── figures/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```
Model akhir disimpan dalam format joblib di direktori models/. File tersebut memuat model dan komponen preprocessing yang dibutuhkan untuk melakukan prediksi.

## Keterbatasan

Dataset tidak memiliki label segmen pelanggan sehingga evaluasi menggunakan metrik internal clustering, bukan akurasi klasifikasi.

Hasil segmentasi bergantung pada fitur dan pola transaksi yang tersedia dalam dataset.

Data transaksi yang digunakan merangkum aktivitas selama enam bulan sehingga perubahan perilaku pelanggan setelah periode tersebut belum tentu tercermin.

Penentuan segmen tidak secara langsung membuktikan bahwa pelanggan akan melakukan churn.

Fitur lama bergabung menggunakan tanggal acuan 30 Juni 2026 sehingga penggunaan model pada periode lain perlu memperhatikan konsistensi perhitungan fitur tersebut.

Hasil prediksi untuk pelanggan dengan karakteristik yang jauh berbeda dari data pelatihan perlu ditafsirkan secara hati-hati.

## Daftar periksa sebelum dikumpulkan

- [ ] Repositori bersifat publik dan setiap anggota memiliki *commit*
- [ ] *Notebook* dapat dijalankan ulang dari awal sampai akhir tanpa galat
- [ ] *Baseline* wajib dilaporkan dan dibandingkan
- [ ] Data *test* hanya dibuka satu kali, di akhir
- [ ] `artifacts/metadata.json` berisi versi model, fitur masukan, *threshold*, dan metrik
- [ ] Aplikasi dapat dibuka orang lain melalui tautan, termasuk dari ponsel
- [ ] Aplikasi tidak berhenti mendadak ketika menerima masukan yang tidak wajar
- [ ] Laporan paling banyak 6 halaman dan video paling lama 5 menit