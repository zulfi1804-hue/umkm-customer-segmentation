
import pandas as pd
import pytest

from src.features import (
    FITUR_MODEL,
    siapkan_fitur_model,
)


def test_fitur_model_berjumlah_enam():
    assert len(FITUR_MODEL) == 6


def test_siapkan_fitur_model():
    data = pd.DataFrame([{
        "jumlah_transaksi_6bln": 10,
        "total_belanja_rp": 350000,
        "hari_sejak_transaksi_terakhir": 12,
        "persen_pakai_promo": 80,
        "rating_rata": 4.5,
        "lama_bergabung_hari": 450,
    }])

    hasil = siapkan_fitur_model(data)

    assert list(hasil.columns) == FITUR_MODEL
    assert hasil.shape == (1, 6)


def test_siapkan_fitur_model_menolak_nilai_kosong():
    data = pd.DataFrame([{
        "jumlah_transaksi_6bln": 10,
        "total_belanja_rp": 350000,
        "hari_sejak_transaksi_terakhir": 12,
        "persen_pakai_promo": 80,
        "rating_rata": None,
        "lama_bergabung_hari": 450,
    }])

    with pytest.raises(ValueError):
        siapkan_fitur_model(data)
