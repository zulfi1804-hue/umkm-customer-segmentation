
import pandas as pd
import pytest

from src.preprocessing import (
    bersihkan_total_belanja,
    periksa_fitur_numerik,
)


def test_bersihkan_total_belanja():
    data = pd.DataFrame({
        "total_belanja_rp": [
            "Rp 350.000",
            "1,250,000",
            "500000",
        ]
    })

    hasil = bersihkan_total_belanja(data)

    assert hasil["total_belanja_rp"].tolist() == [
        350000,
        1250000,
        500000,
    ]


def test_periksa_fitur_numerik():
    data = pd.DataFrame({
        "jumlah_transaksi_6bln": [10],
        "total_belanja_rp": [350000],
        "hari_sejak_transaksi_terakhir": [12],
        "persen_pakai_promo": [80],
        "rating_rata": [4.5],
    })

    hasil = periksa_fitur_numerik(data)

    assert hasil.shape == (1, 5)


def test_menolak_fitur_numerik_kosong():
    data = pd.DataFrame({
        "jumlah_transaksi_6bln": [10],
        "total_belanja_rp": [350000],
        "hari_sejak_transaksi_terakhir": [12],
        "persen_pakai_promo": [80],
        "rating_rata": [None],
    })

    with pytest.raises(ValueError):
        periksa_fitur_numerik(data)
