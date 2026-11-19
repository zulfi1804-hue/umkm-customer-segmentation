# Segmentasi Pelanggan UMKM (UMKM Customer Segmentation)

## 1. Gambaran Umum Proyek

Proyek ini menerapkan teknik *Unsupervised Machine Learning* untuk melakukan segmentasi pelanggan pada sebuah UMKM yang bergerak di bidang bakery dan kopi di Bandung, Indonesia.

Tujuan proyek ini adalah mengidentifikasi pola perilaku pembelian pelanggan, mengelompokkan pelanggan ke dalam beberapa segmen berdasarkan karakteristiknya, serta memberikan rekomendasi strategi pemasaran yang sesuai untuk setiap segmen.

Model akhir menggunakan algoritma **K-Means Clustering dengan 4 cluster** dan diintegrasikan ke dalam aplikasi Streamlit interaktif untuk memprediksi segmen pelanggan baru.

## 2. Permasalahan Bisnis

UMKM saat ini memberikan penawaran promosi yang relatif sama kepada seluruh pelanggan, padahal setiap pelanggan memiliki perilaku dan kebiasaan pembelian yang berbeda.

Proyek ini bertujuan meningkatkan efektivitas pemasaran dengan cara:

- Mengidentifikasi kelompok pelanggan berdasarkan perilaku pembelian.
- Memahami karakteristik masing-masing segmen pelanggan.
- Memberikan rekomendasi strategi pemasaran yang sesuai untuk setiap segmen.
- Mengembangkan aplikasi yang dapat menentukan segmen pelanggan baru berdasarkan data yang dimasukkan.

## 3. Dataset

Dataset berisi 10.000 data pelanggan unik yang mencakup informasi pendaftaran dan ringkasan transaksi selama enam bulan terakhir.

Informasi dalam dataset meliputi:

- Usia dan tanggal pendaftaran pelanggan.
- Kanal pembelian utama.
- Metode pembayaran dan kategori produk favorit.
- Jumlah transaksi selama enam bulan terakhir.
- Total nilai belanja pelanggan.
- Jumlah hari sejak transaksi terakhir.
- Persentase penggunaan promosi.
- Rata-rata rating pelanggan.

ID pelanggan dan tanggal pendaftaran digunakan untuk pengelolaan data serta rekayasa fitur (*feature engineering*). Model clustering akhir menggunakan enam fitur numerik.

## 4. Pendekatan Machine Learning

Proyek ini menggunakan pendekatan *Unsupervised Learning*, khususnya clustering, karena dataset tidak memiliki label segmen pelanggan yang telah ditentukan sebelumnya.

### K-Means Clustering

Algoritma K-Means digunakan sebagai metode utama clustering dan diuji melalui empat eksperimen dengan kombinasi pemilihan fitur yang berbeda.

Model final menggunakan enam fitur numerik:

1. `jumlah_transaksi_6bln`
2. `total_belanja_rp`
3. `hari_sejak_transaksi_terakhir`
4. `persen_pakai_promo`
5. `rating_rata`
6. `lama_bergabung_hari`

Model akhir dipilih berdasarkan hasil evaluasi metrik clustering internal serta kemudahan interpretasi karakteristik setiap segmen pelanggan.

### Evaluasi Model

Model final menggunakan K = 4 dan menghasilkan nilai evaluasi sebagai berikut:

| Metrik Evaluasi | Hasil |
|---|---:|
| Silhouette Score | 0,3696 |
| Davies-Bouldin Index | 1,1289 |
| Calinski-Harabasz Index | 5660,67 |
| Jumlah Cluster | 4 |

Hasil tersebut menunjukkan bahwa model terpilih memiliki pemisahan kelompok pelanggan yang cukup baik dan menghasilkan segmen yang dapat diinterpretasikan untuk kebutuhan bisnis.

## 5. Hasil Segmentasi Pelanggan

Model K-Means final menghasilkan empat segmen pelanggan:

### Cluster 1 — Pelanggan Aktif dan Responsif terhadap Promo

- Jumlah pelanggan: 2.497 (24,97%)
- Rata-rata transaksi: 10,93 kali
- Rata-rata total belanja: Rp348.541
- Rata-rata hari sejak transaksi terakhir: 12,20 hari
- Rata-rata penggunaan promo: 81,54%

**Rekomendasi Strategi Bisnis:**

Memberikan voucher untuk pembelian berikutnya, promo bundling roti dan kopi, serta program loyalty stamp.

### Cluster 2 — Pelanggan Tidak Aktif / Berisiko Churn

- Jumlah pelanggan: 2.966 (29,66%)
- Rata-rata transaksi: 2,56 kali
- Rata-rata total belanja: Rp107.158
- Rata-rata hari sejak transaksi terakhir: 109,61 hari
- Rata-rata penggunaan promo: 34,64%

**Rekomendasi Strategi Bisnis:**

Melakukan kampanye win-back, memberikan penawaran produk favorit pelanggan, serta mengirimkan survei kepuasan pelanggan.

### Cluster 3 — Pelanggan Loyal Bernilai Tinggi

- Jumlah pelanggan: 3.023 (30,23%)
- Rata-rata transaksi: 27,88 kali
- Rata-rata total belanja: Rp1.353.954
- Rata-rata hari sejak transaksi terakhir: 5,15 hari
- Rata-rata penggunaan promo: 19,66%

**Rekomendasi Strategi Bisnis:**

Memberikan reward VIP, akses lebih awal terhadap menu baru, serta program apresiasi pelanggan tanpa terlalu bergantung pada diskon.

### Cluster 4 — Pelanggan Sesekali dengan Belanja Tinggi

- Jumlah pelanggan: 1.514 (15,14%)
- Rata-rata transaksi: 4,10 kali
- Rata-rata total belanja: Rp1.093.769
- Rata-rata hari sejak transaksi terakhir: 30,66 hari
- Rata-rata penggunaan promo: 12,56%

**Rekomendasi Strategi Bisnis:**

Menawarkan paket premium, kue ulang tahun, snack pack, serta pengingat untuk melakukan pre-order.

## 6. Alur Pengerjaan Proyek

Tahapan pengerjaan proyek meliputi:

1. Exploratory Data Analysis (EDA)
2. Pembersihan Data (*Data Cleaning*)
3. Rekayasa Fitur (*Feature Engineering*)
4. Pra-pemrosesan Data (*Data Preprocessing*)
5. Eksperimen Clustering K-Means
6. Evaluasi dan Pemilihan Model
7. Profiling Pelanggan
8. Penyusunan Rekomendasi Strategi Bisnis
9. Penyimpanan dan Pengujian Model
10. Pengembangan dan Deployment Aplikasi Streamlit

## 7. Aplikasi Streamlit

Model final diintegrasikan ke dalam aplikasi interaktif yang memungkinkan pengguna memasukkan informasi pelanggan dan memperoleh hasil prediksi segmen beserta rekomendasi strategi bisnis yang sesuai.

**Link Aplikasi:**

[UMKM Customer Segmentation — Buka Aplikasi](https://umkm-customer-segmentation.streamlit.app/)

## 8. Struktur Repository

```text
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
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## 9. Instalasi dan Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/zulfi1804-hue/umkm-customer-segmentation.git
cd umkm-customer-segmentation
```

### 2. Membuat Virtual Environment

```bash
python -m venv .venv
```

Aktifkan environment menggunakan Git Bash pada Windows:

```bash
source .venv/Scripts/activate
```

### 3. Instalasi Dependencies

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Aplikasi Streamlit

```bash
python -m streamlit run app/app.py
```

Aplikasi akan terbuka melalui browser.

## 10. Anggota Kelompok

- Anggota 1 — Atsnaina Habibah
- Anggota 2 — Kholistyani Zulfi
