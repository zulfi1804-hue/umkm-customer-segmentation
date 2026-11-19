
import numpy as np

from src.clustering import (
    latih_kmeans,
    evaluasi_clustering,
)


def test_latih_kmeans():
    data = np.array([
        [1, 2],
        [1, 3],
        [10, 11],
        [10, 12],
    ])

    model, label = latih_kmeans(data, jumlah_cluster=2)

    assert model.n_clusters == 2
    assert len(label) == 4
    assert len(set(label)) == 2


def test_evaluasi_clustering():
    data = np.array([
        [1, 2],
        [1, 3],
        [10, 11],
        [10, 12],
    ])

    model, label = latih_kmeans(data, jumlah_cluster=2)
    hasil = evaluasi_clustering(data, label)

    assert "silhouette_score" in hasil
    assert "davies_bouldin_score" in hasil
    assert "calinski_harabasz_score" in hasil
