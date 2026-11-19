
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score,
)


def latih_kmeans(data, jumlah_cluster=4, random_state=42):
    """
    Melatih model K-Means pada data yang sudah melalui scaling.
    """
    model = KMeans(
        n_clusters=jumlah_cluster,
        random_state=random_state,
        n_init=10,
    )

    label = model.fit_predict(data)

    return model, label


def evaluasi_clustering(data, label):
    """
    Menghitung metrik evaluasi hasil clustering.
    """
    jumlah_cluster = len(set(label))

    if jumlah_cluster < 2:
        raise ValueError("Evaluasi membutuhkan minimal dua cluster.")

    hasil = {
        "silhouette_score": silhouette_score(data, label),
        "davies_bouldin_score": davies_bouldin_score(data, label),
        "calinski_harabasz_score": calinski_harabasz_score(data, label),
    }

    return hasil
