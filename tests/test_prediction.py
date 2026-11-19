
import pandas as pd
import joblib
import pytest

from src.prediction import (
    prediksi_cluster,
    prediksi_satu_pelanggan,
)


@pytest.fixture
def model_bundle():
    return joblib.load("models/model_final.joblib")


@pytest.fixture
def data_pelanggan():
    return pd.DataFrame([{
        "jumlah_transaksi_6bln": 10,
        "total_belanja_rp": 350000,
        "hari_sejak_transaksi_terakhir": 12,
        "persen_pakai_promo": 80,
        "rating_rata": 4.5,
        "lama_bergabung_hari": 450,
    }])


def test_prediksi_satu_pelanggan(model_bundle, data_pelanggan):
    hasil = prediksi_satu_pelanggan(
        data_pelanggan,
        model_bundle["model"],
        model_bundle["scaler"],
    )

    assert isinstance(hasil, int)
    assert hasil in [0, 1, 2, 3]


def test_prediksi_cluster(model_bundle, data_pelanggan):
    hasil = prediksi_cluster(
        data_pelanggan,
        model_bundle["model"],
        model_bundle["scaler"],
    )

    assert len(hasil) == 1
    assert int(hasil[0]) in [0, 1, 2, 3]


def test_prediksi_satu_pelanggan_menolak_banyak_data(
    model_bundle,
    data_pelanggan,
):
    data_dua = pd.concat(
        [data_pelanggan, data_pelanggan],
        ignore_index=True,
    )

    with pytest.raises(ValueError):
        prediksi_satu_pelanggan(
            data_dua,
            model_bundle["model"],
            model_bundle["scaler"],
        )
