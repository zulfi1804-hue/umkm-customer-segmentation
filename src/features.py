
import pandas as pd

FITUR_MODEL = [
    "jumlah_transaksi_6bln",
    "total_belanja_rp",
    "hari_sejak_transaksi_terakhir",
    "persen_pakai_promo",
    "rating_rata",
    "lama_bergabung_hari",
]

TANGGAL_ACUAN = pd.Timestamp("2026-06-30")


def tambah_fitur_lama_bergabung(df):
    """
    Menambahkan fitur lama bergabung berdasarkan tanggal pendaftaran.
    Menggunakan tanggal acuan yang sama dengan proses training model.
    """
    hasil = df.copy()
    hasil["tanggal_daftar"] = pd.to_datetime(
        hasil["tanggal_daftar"], errors="coerce"
    )

    hasil["lama_bergabung_hari"] = (
        TANGGAL_ACUAN - hasil["tanggal_daftar"]
    ).dt.days

    return hasil


def siapkan_fitur_model(df):
    """
    Mengambil enam fitur numerik sesuai urutan fitur model final.
    """
    kolom_tidak_ada = [
        kolom for kolom in FITUR_MODEL if kolom not in df.columns
    ]

    if kolom_tidak_ada:
        raise ValueError(
            f"Kolom fitur tidak ditemukan: {kolom_tidak_ada}"
        )

    hasil = df[FITUR_MODEL].copy()

    if hasil.isnull().any().any():
        raise ValueError("Data fitur masih mengandung nilai kosong.")

    return hasil
