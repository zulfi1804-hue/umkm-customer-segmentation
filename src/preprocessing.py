
import pandas as pd


KOLOM_NUMERIK = [
    "jumlah_transaksi_6bln",
    "total_belanja_rp",
    "hari_sejak_transaksi_terakhir",
    "persen_pakai_promo",
    "rating_rata",
]


def bersihkan_total_belanja(data):
    """
    Mengubah nilai total belanja menjadi numerik.
    Mendukung format angka dengan pemisah ribuan dan simbol mata uang.
    """
    hasil = data.copy()

    hasil["total_belanja_rp"] = pd.to_numeric(
        hasil["total_belanja_rp"]
        .astype(str)
        .str.replace(r"[^0-9]", "", regex=True),
        errors="coerce",
    )

    return hasil


def periksa_fitur_numerik(data):
    """
    Memeriksa keberadaan dan kelengkapan fitur numerik model.
    """
    kolom_tidak_ada = [
        kolom for kolom in KOLOM_NUMERIK
        if kolom not in data.columns
    ]

    if kolom_tidak_ada:
        raise ValueError(
            f"Kolom berikut tidak ditemukan: {kolom_tidak_ada}"
        )

    if data[KOLOM_NUMERIK].isnull().any().any():
        raise ValueError("Fitur numerik masih mengandung nilai kosong.")

    return data.copy()
