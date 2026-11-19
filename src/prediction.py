
import pandas as pd

from src.features import siapkan_fitur_model


def prediksi_cluster(data, model, scaler):
    """
    Memprediksi cluster pelanggan menggunakan model K-Means final.

    Parameters
    ----------
    data : pandas.DataFrame
        Data pelanggan yang memiliki enam fitur model.
    model : objek model K-Means
        Model clustering yang sudah dilatih.
    scaler : objek scaler
        Scaler yang sudah di-fit pada data training.

    Returns
    -------
    list
        Label cluster untuk setiap pelanggan.
    """
    fitur = siapkan_fitur_model(data)
    fitur_scaled = scaler.transform(fitur)

    hasil_prediksi = model.predict(fitur_scaled)

    return hasil_prediksi


def prediksi_satu_pelanggan(data, model, scaler):
    """
    Memprediksi cluster untuk satu pelanggan.
    """
    if len(data) != 1:
        raise ValueError("Fungsi ini hanya menerima satu data pelanggan.")

    return int(prediksi_cluster(data, model, scaler)[0])
