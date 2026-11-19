import base64
import streamlit as st
import pandas as pd
import joblib
import numpy as np
from pathlib import Path
from datetime import date

# ==========================================
# 1. KONFIGURASI APLIKASI
# ==========================================

st.set_page_config(
    page_title="UMKM Customer Segmentation",
    page_icon="☕",
    layout="wide",
)

# ==========================================
# 2. STYLE
# Palet: #FBFDEE #F6F3C2 #EBEBA6 #DCE57A #C3DC4E #AED135 #8BBB43 #689B40 #4B7536 #35502A + hitam #121510
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=DM+Sans:wght@400;500;600&display=swap');

:root {
  color-scheme: light;
  --cream: #FBFDEE;
  --butter: #F6F3C2;
  --pale: #EBEBA6;
  --lime-soft: #DCE57A;
  --lime-1: #C3DC4E;
  --lime: #AED135;
  --green: #8BBB43;
  --green-2: #689B40;
  --green-3: #4B7536;
  --forest: #35502A;
  --black: #121510;
  --muted: #5B6650;
}

html, body, .stApp, [data-testid="stAppViewContainer"] {
  background-color: var(--cream) !important;
  background-image: radial-gradient(#E3E7A0 1.4px, transparent 1.4px);
  background-size: 24px 24px;
  color: var(--black);
}

.stApp p, .stApp label, .stApp input, .stApp button, .stApp li, .stApp td, .stApp th,
[data-testid="stMarkdownContainer"] p, [data-testid="stWidgetLabel"] p {
  font-family: 'DM Sans', sans-serif !important;
}

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }

/* jarak halaman bagian atas dirapatkan */
.block-container,
[data-testid="stMainBlockContainer"] {
  max-width: 1120px;
  padding-top: 1rem !important;
  padding-bottom: 3rem;
}

/* ---------- HERO ---------- */
.hero {
  display: flex; align-items: center; justify-content: space-between; gap: 32px;
}
.hero-text { flex: 1; min-width: 0; }
.app-eyebrow {
  font-family: 'DM Sans', sans-serif; font-size: 12px; letter-spacing: .16em;
  text-transform: uppercase; color: var(--green-3); font-weight: 600; margin-bottom: 8px;
}
.app-title {
  font-family: 'Fraunces', serif; font-weight: 600; font-size: 42px;
  line-height: 1.1; margin: 0 0 12px 0; padding: 0; color: var(--black);
}
.app-desc { color: var(--muted) !important; max-width: 560px; font-size: 16px; line-height: 1.65; margin-bottom: 0; }
.hero-art {
  display: flex; align-items: center; padding: 14px 18px;
  background: var(--butter); border: 1.5px solid var(--black); border-radius: 14px;
  box-shadow: 6px 6px 0 var(--lime);
}
.hero-art img { margin: 0 -6px; }
@media (max-width: 900px) { .hero-art { display: none; } }

/* ---------- ORNAMEN PEMBATAS ---------- */
.ornament { display: flex; align-items: center; gap: 12px; margin: 18px 0 20px; }
.ornament .line { flex: 1; height: 1.5px; background: var(--lime-1); }

/* ---------- JUDUL SEKSI ---------- */
.sec { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.section-title {
  font-family: 'Fraunces', serif; font-size: 25px; font-weight: 500; color: var(--black); margin: 0;
}

/* ---------- FORM ---------- */
[data-testid="stForm"] {
  background: #FFFFFF !important; border: 1.5px solid var(--black);
  border-radius: 12px; padding: 26px 26px 22px; box-shadow: 6px 6px 0 var(--lime-soft);
}
label p, [data-testid="stWidgetLabel"] p {
  font-size: 13px !important; font-weight: 500 !important; color: var(--muted) !important;
  line-height: 1.4 !important; margin: 0 !important;
}
/* tinggi label dibuat sama (cukup untuk 2 baris) supaya kolom kiri-kanan sejajar */
[data-testid="stForm"] [data-testid="stHorizontalBlock"] [data-testid="stWidgetLabel"] {
  min-height: 40px !important;
  display: flex !important;
  align-items: flex-end !important;
}

div[data-baseweb="input"],
div[data-baseweb="base-input"],
div[data-baseweb="input"] > div,
[data-testid="stNumberInputContainer"],
[data-testid="stNumberInputContainer"] > div,
[data-testid="stDateInputField"] {
  background: #FFFFFF !important; border-radius: 8px !important;
}
div[data-baseweb="input"] { border: 1.5px solid var(--black) !important; }
div[data-baseweb="input"]:focus-within,
div[data-baseweb="input"]:has(input:focus) {
  border-color: var(--green-2) !important; box-shadow: 0 0 0 3px rgba(174, 209, 53, .45) !important;
}

/* ANGKA / TEKS DI DALAM INPUT: hijau tua, selalu terlihat */
.stApp input,
.stApp input[type="number"],
.stApp input[type="text"],
[data-testid="stNumberInputField"],
[data-testid="stDateInputField"] input,
div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input {
  background: transparent !important;
  color: var(--forest) !important;
  -webkit-text-fill-color: var(--forest) !important;
  opacity: 1 !important;
  caret-color: var(--forest) !important;
  font-size: 15px !important;
  font-weight: 600 !important;
}
.stApp input:disabled {
  color: var(--forest) !important;
  -webkit-text-fill-color: var(--forest) !important;
  opacity: 1 !important;
}
.stApp input::placeholder {
  color: var(--green-2) !important;
  -webkit-text-fill-color: var(--green-2) !important;
  opacity: .7 !important;
}
[data-testid="stDateInputField"] svg, [data-testid="stDateInput"] svg { color: var(--forest) !important; }

[data-testid="stNumberInputStepUp"], [data-testid="stNumberInputStepDown"] {
  background: var(--butter) !important; color: var(--forest) !important;
  border-left: 1.5px solid var(--black) !important;
}
[data-testid="stNumberInputStepUp"]:hover, [data-testid="stNumberInputStepDown"]:hover {
  background: var(--lime) !important; color: var(--black) !important;
}

/* tombol */
.stFormSubmitButton button {
  background: var(--black) !important; border: 1.5px solid var(--black) !important;
  border-radius: 8px; padding: 12px 0; transition: background .15s ease, transform .1s ease;
}
.stFormSubmitButton button:hover { background: var(--forest) !important; transform: translateY(-1px); }
.stFormSubmitButton button p {
  color: var(--lime-1) !important; font-weight: 600 !important; font-size: 15px !important;
  letter-spacing: .02em;
}

/* ---------- HASIL ---------- */
.empty-state {
  border: 2px dashed var(--green); border-radius: 12px; padding: 40px 28px;
  text-align: center; color: var(--muted); background: var(--butter);
  font-size: 15px; line-height: 1.6; font-family: 'DM Sans', sans-serif;
}
.empty-state img { margin-bottom: 8px; }
.result-card {
  position: relative; background: #FFFFFF; border: 1.5px solid var(--black);
  border-radius: 12px; padding: 26px 28px;
}
.result-head { padding-right: 96px; min-height: 84px; }
.result-ico { position: absolute; top: 18px; right: 20px; }
.badge {
  display: inline-block; font-family: 'DM Sans', sans-serif; font-size: 12px; font-weight: 600;
  letter-spacing: .1em; text-transform: uppercase; padding: 4px 10px; border-radius: 4px;
  margin-bottom: 12px; border: 1.5px solid var(--black);
}
.result-name {
  font-family: 'Fraunces', serif; font-size: 26px; font-weight: 600;
  line-height: 1.2; margin: 0 0 8px; color: var(--black);
}
.result-desc { color: var(--muted) !important; line-height: 1.65; margin: 0 0 22px; }
.mini-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5px;
  background: var(--black); border: 1.5px solid var(--black); border-radius: 8px;
  overflow: hidden; margin: 22px 0 24px;
}
.mini { background: var(--cream); padding: 14px 16px; font-family: 'DM Sans', sans-serif; }
.mini .k { font-size: 12px; color: var(--muted); margin-bottom: 4px; }
.mini .v { font-size: 18px; font-weight: 600; color: var(--black); }
.reco-title {
  font-family: 'DM Sans', sans-serif; font-size: 12px; letter-spacing: .12em;
  text-transform: uppercase; color: var(--green-3); font-weight: 600; margin-bottom: 8px;
}
.reco-box {
  background: var(--butter); border: 1.5px solid var(--lime-soft); border-radius: 8px; padding: 14px 16px;
}
.reco-text { margin: 0; line-height: 1.75; color: var(--black) !important; }

/* expander */
[data-testid="stExpander"] {
  border: 1.5px solid var(--black) !important; border-radius: 10px !important;
  background: #FFFFFF !important; margin-top: 22px;
}
[data-testid="stExpander"] summary, [data-testid="stExpander"] summary p {
  font-size: 14px; color: var(--black) !important;
}

/* tabel data */
.table-wrap { overflow-x: auto; }
.data-table { width: 100%; border-collapse: collapse; font-family: 'DM Sans', sans-serif; font-size: 13px; }
.data-table th {
  text-align: left; color: var(--forest); font-weight: 600;
  padding: 8px 10px; border-bottom: 1.5px solid var(--black); background: var(--butter);
}
.data-table td { padding: 8px 10px; color: var(--black); }

/* ---------- FOOTER ---------- */
.app-footer {
  margin-top: 48px; padding: 14px 22px; background: var(--black); border-radius: 10px;
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
  color: var(--lime-1); font-size: 13px; font-family: 'DM Sans', sans-serif; letter-spacing: .02em;
}
.foot-ico { display: flex; gap: 6px; }
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. ILUSTRASI (SVG DI DALAM KODE)
# ==========================================

LN = 'stroke="#121510" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
LN2 = 'stroke="#121510" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'

_SVG = {}

_SVG["cupcake"] = (
    f'<path d="M26 54 L74 54 L67 88 Q66.5 90 64 90 L36 90 Q33.5 90 33 88 Z" fill="#689B40" {LN}/>'
    f'<path d="M40 60 L42 86 M50 60 L50 86 M60 60 L58 86" fill="none" {LN2}/>'
    f'<path d="M22 54 C18 42 28 36 34 36 C34 26 42 20 50 18 C58 20 66 26 66 36 C72 36 82 42 78 54 Z" fill="#DCE57A" {LN}/>'
    f'<path d="M38 46 L42 43 M56 42 L60 45 M48 50 L53 50" fill="none" stroke="#4B7536" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="50" cy="12" r="6" fill="#35502A" {LN}/>'
)

_SVG["croissant"] = (
    f'<ellipse cx="20" cy="64" rx="9" ry="16" transform="rotate(-55 20 64)" fill="#DCE57A" {LN}/>'
    f'<ellipse cx="80" cy="64" rx="9" ry="16" transform="rotate(55 80 64)" fill="#DCE57A" {LN}/>'
    f'<ellipse cx="32" cy="52" rx="12" ry="20" transform="rotate(-32 32 52)" fill="#EBEBA6" {LN}/>'
    f'<ellipse cx="68" cy="52" rx="12" ry="20" transform="rotate(32 68 52)" fill="#EBEBA6" {LN}/>'
    f'<ellipse cx="50" cy="46" rx="14" ry="22" fill="#F6F3C2" {LN}/>'
    f'<path d="M43 33 L57 35 M41 45 L59 47 M43 57 L57 59" fill="none" {LN2}/>'
)

_SVG["milk"] = (
    f'<path d="M40 20 L40 30 C28 36 26 44 26 54 L26 84 C26 88 29 90 33 90 L67 90 C71 90 74 88 74 84 L74 54 C74 44 72 36 60 30 L60 20 Z" fill="#FFFFFF" {LN}/>'
    f'<rect x="37" y="10" width="26" height="10" rx="3" fill="#AED135" {LN}/>'
    f'<rect x="32" y="56" width="36" height="24" rx="4" fill="#AED135" {LN2}/>'
    f'<circle cx="50" cy="68" r="5.5" fill="#FFFFFF" {LN2}/>'
    f'<path d="M32 44 L32 50" fill="none" stroke="#DCE57A" stroke-width="3" stroke-linecap="round"/>'
)

_SVG["cake"] = (
    f'<ellipse cx="50" cy="88" rx="40" ry="6" fill="#689B40" {LN}/>'
    f'<rect x="18" y="64" width="64" height="18" rx="3" fill="#DCE57A" {LN}/>'
    f'<rect x="18" y="58" width="64" height="7" fill="#FFFFFF" {LN}/>'
    f'<rect x="18" y="42" width="64" height="17" fill="#DCE57A" {LN}/>'
    f'<path d="M18 42 Q18 30 34 30 L66 30 Q82 30 82 42 Z" fill="#FBFDEE" {LN}/>'
    f'<circle cx="50" cy="21" r="7" fill="#35502A" {LN}/>'
    f'<path d="M50 14 Q54 7 61 8" fill="none" {LN2}/>'
)

_SVG["coffee"] = (
    f'<path d="M36 14 Q30 22 36 28 M50 10 Q44 20 50 28 M64 14 Q58 22 64 28" fill="none" {LN2}/>'
    f'<path d="M20 40 L76 40 L76 62 C76 76 66 84 48 84 C30 84 20 76 20 62 Z" fill="#AED135" {LN}/>'
    f'<path d="M76 46 C92 46 92 68 74 68" fill="none" {LN}/>'
    f'<path d="M20 52 L76 52" fill="none" {LN2}/>'
    f'<ellipse cx="48" cy="90" rx="34" ry="5" fill="#35502A" {LN}/>'
)

_SVG["bread"] = (
    f'<path d="M16 56 C10 40 24 28 50 28 C76 28 90 40 84 56 L84 76 C84 80 82 82 78 82 L22 82 C18 82 16 80 16 76 Z" fill="#DCE57A" {LN}/>'
    f'<path d="M34 40 L40 54 M48 38 L54 54 M62 40 L68 54" fill="none" {LN2}/>'
)


def ikon(nama, w=64, style=""):
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">' + _SVG[nama] + "</svg>"
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f'<img src="data:image/svg+xml;base64,{b64}" width="{w}" height="{w}" style="{style}" alt="">'


# ==========================================
# 4. MEMUAT MODEL FINAL
# ==========================================

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "model_final.joblib"
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    paket_model = load_model()

    model = paket_model["model"]
    scaler = paket_model["scaler"]
    fitur = paket_model["fitur"]

    # Kolom yang di-log1p saat training (harus sama dengan notebook).
    # Jika paket model menyimpan "kolom_log", itu yang dipakai.
    kolom_log = paket_model.get(
        "kolom_log",
        [
            "jumlah_transaksi_6bln",
            "total_belanja_rp",
            "hari_sejak_transaksi_terakhir",
        ],
    )

except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()


# ==========================================
# 5. INFORMASI SEGMEN PELANGGAN
# ==========================================

nama_segmen = {
    0: "Pelanggan Aktif dan Responsif terhadap Promo",
    1: "Pelanggan Tidak Aktif / Berisiko Churn",
    2: "Pelanggan Loyal Bernilai Tinggi",
    3: "Pelanggan Sesekali dengan Belanja Tinggi",
}

deskripsi_segmen = {
    0: {
        "karakteristik": "Sering bertransaksi dan memiliki penggunaan promo yang tinggi.",
        "rekomendasi": (
            "Berikan voucher pembelian berikutnya, promo bundling roti dan kopi, "
            "serta program loyalty stamp."
        ),
    },
    1: {
        "karakteristik": "Frekuensi transaksi rendah dan sudah cukup lama tidak bertransaksi.",
        "rekomendasi": (
            "Lakukan kampanye win-back, berikan penawaran produk favorit, "
            "dan kirim survei kepuasan."
        ),
    },
    2: {
        "karakteristik": "Memiliki frekuensi transaksi dan total belanja tinggi serta relatif aktif.",
        "rekomendasi": (
            "Berikan reward VIP, akses awal menu baru, dan apresiasi pelanggan "
            "tanpa terlalu bergantung pada diskon."
        ),
    },
    3: {
        "karakteristik": "Frekuensi transaksi relatif rendah, tetapi nilai belanjanya tinggi.",
        "rekomendasi": (
            "Tawarkan paket premium, kue ulang tahun, snack pack, "
            "dan pengingat pre-order."
        ),
    },
}

# (warna bayangan kartu & badge, warna teks badge)
warna_segmen = {
    0: ("#C3DC4E", "#121510"),
    1: ("#35502A", "#FBFDEE"),
    2: ("#8BBB43", "#121510"),
    3: ("#DCE57A", "#121510"),
}

# ikon tiap segmen
ikon_segmen = {0: "cupcake", 1: "milk", 2: "croissant", 3: "cake"}


def rupiah(x):
    return "Rp " + f"{x:,.0f}".replace(",", ".")


# ==========================================
# 6. HEADER
# ==========================================

hero = (
    '<div class="hero"><div class="hero-text">'
    '<div class="app-eyebrow">K-Means Clustering</div>'
    '<h1 class="app-title">UMKM Customer Segmentation</h1>'
    '<p class="app-desc">Aplikasi segmentasi pelanggan untuk membantu UMKM memahami karakteristik '
    "pelanggan dan menentukan strategi pemasaran yang tepat. Masukkan data pelanggan, lalu model "
    "akan menempatkannya ke dalam segmen.</p></div>"
    '<div class="hero-art">'
    + ikon("croissant", 92, "transform:rotate(-8deg)")
    + ikon("cupcake", 88, "transform:translateY(-8px) rotate(5deg)")
    + ikon("milk", 84, "transform:rotate(-4deg)")
    + ikon("cake", 92, "transform:translateY(6px) rotate(6deg)")
    + "</div></div>"
)
st.markdown(hero, unsafe_allow_html=True)

ornamen = (
    '<div class="ornament"><span class="line"></span>'
    + ikon("bread", 34)
    + ikon("cupcake", 34)
    + ikon("coffee", 34)
    + '<span class="line"></span></div>'
)
st.markdown(ornamen, unsafe_allow_html=True)

kiri, kanan = st.columns([5, 6], gap="large")

# ==========================================
# 7. FORM INPUT PELANGGAN
# ==========================================

with kiri:
    st.markdown(
        '<div class="sec"><div class="section-title">Input data pelanggan</div>'
        + ikon("coffee", 46)
        + "</div>",
        unsafe_allow_html=True,
    )

    with st.form("form_prediksi"):
        c1, c2 = st.columns(2)

        jumlah_transaksi = c1.number_input(
            "Jumlah transaksi (6 bulan)", min_value=0, max_value=1000, value=15, step=1
        )
        hari_terakhir = c2.number_input(
            "Hari sejak transaksi terakhir", min_value=0, value=10, step=1
        )

        total_belanja = st.number_input(
            "Total belanja (Rp)", min_value=0, value=750000, step=10000, format="%d"
        )

        c3, c4 = st.columns(2)

        persen_promo = c3.number_input(
            "Persentase penggunaan promo (%)", min_value=0, max_value=100, value=25, step=1
        )
        rating = c4.number_input(
            "Rating rata-rata", min_value=1.0, max_value=5.0, value=4.5, step=0.1, format="%.1f"
        )

        tanggal_daftar = st.date_input(
            "Tanggal bergabung",
            value=date(2025, 9, 1),
            max_value=date(2026, 6, 30),
            format="DD/MM/YYYY",
        )

        tombol_prediksi = st.form_submit_button(
            "Prediksi segmen pelanggan", use_container_width=True
        )

# ==========================================
# 8. PROSES PREDIKSI
# ==========================================

if tombol_prediksi:
    tanggal_acuan = pd.Timestamp("2026-06-30")
    lama_bergabung = (tanggal_acuan - pd.Timestamp(tanggal_daftar)).days

    data_baru = pd.DataFrame([{
        "jumlah_transaksi_6bln": jumlah_transaksi,
        "total_belanja_rp": total_belanja,
        "hari_sejak_transaksi_terakhir": hari_terakhir,
        "persen_pakai_promo": persen_promo,
        "rating_rata": rating,
        "lama_bergabung_hari": lama_bergabung,
    }])

    # Mengikuti urutan fitur saat training
    data_baru = data_baru[fitur]  # tetap angka asli, untuk ditampilkan

    # Samakan dengan training: kolom skewed di-log1p SEBELUM scaling
    data_model = data_baru.copy().astype(float)
    kolom_log_dipakai = [k for k in kolom_log if k in data_model.columns]
    data_model[kolom_log_dipakai] = np.log1p(data_model[kolom_log_dipakai])

    data_scaled = scaler.transform(data_model)
    hasil_cluster = int(model.predict(data_scaled)[0])

    st.session_state["hasil"] = {"cluster": hasil_cluster, "data": data_baru}

# ==========================================
# 9. MENAMPILKAN HASIL PREDIKSI
# ==========================================

with kanan:
    st.markdown(
        '<div class="sec"><div class="section-title">Hasil segmentasi pelanggan</div>'
        + ikon("bread", 46)
        + "</div>",
        unsafe_allow_html=True,
    )

    hasil = st.session_state.get("hasil")

    if not hasil:
        st.markdown(
            '<div class="empty-state">'
            + ikon("cake", 96)
            + "<br>Hasil akan muncul di sini.<br>"
            "Isi data pelanggan di sebelah kiri, lalu klik <b>Prediksi segmen pelanggan</b>.</div>",
            unsafe_allow_html=True,
        )
    else:
        cl = hasil["cluster"]
        info = deskripsi_segmen[cl]
        warna, teks_badge = warna_segmen[cl]
        d = hasil["data"].iloc[0]

        html = (
            f'<div class="result-card" style="box-shadow:6px 6px 0 {warna};">'
            f'<div class="result-ico">{ikon(ikon_segmen[cl], 72)}</div>'
            '<div class="result-head">'
            f'<div class="badge" style="background:{warna};color:{teks_badge};">Cluster {cl}</div>'
            f'<div class="result-name">{nama_segmen[cl]}</div>'
            "</div>"
            f'<p class="result-desc">{info["karakteristik"]}</p>'
            '<div class="mini-grid">'
            f'<div class="mini"><div class="k">Transaksi</div><div class="v">{int(d["jumlah_transaksi_6bln"])}x</div></div>'
            f'<div class="mini"><div class="k">Total belanja</div><div class="v">{rupiah(d["total_belanja_rp"])}</div></div>'
            f'<div class="mini"><div class="k">Terakhir belanja</div><div class="v">{int(d["hari_sejak_transaksi_terakhir"])} hari lalu</div></div>'
            "</div>"
            '<div class="reco-title">Rekomendasi strategi bisnis</div>'
            f'<div class="reco-box"><p class="reco-text">{info["rekomendasi"]}</p></div>'
            "</div>"
        )
        st.markdown(html, unsafe_allow_html=True)

        with st.expander("Lihat data yang diproses"):
            tabel = hasil["data"].to_html(index=False, border=0, classes="data-table")
            st.markdown(f'<div class="table-wrap">{tabel}</div>', unsafe_allow_html=True)

# ==========================================
# 10. FOOTER
# ==========================================

st.markdown(
    '<div class="app-footer"><span>UMKM Customer Segmentation &nbsp;&copy;&nbsp; '
    "B &amp; Z Machine Learning</span>"
    '<span class="foot-ico">'
    + ikon("milk", 30)
    + ikon("croissant", 30)
    + ikon("cake", 30)
    + "</span></div>",
    unsafe_allow_html=True,
)