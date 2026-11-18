import os
import streamlit as st
import mysql.connector
import pandas as pd
from html import escape
from urllib.parse import quote
from uuid import uuid4
from database import connect_db, get_secret

WHATSAPP_PHONE = str(
    get_secret("WHATSAPP_PHONE", os.getenv("WHATSAPP_PHONE", ""))
).strip()

st.set_page_config(
    page_title="Dashboard - Kafe Nusantara",
    page_icon="☕",
    layout="wide",
)

if not st.session_state.get("authenticated", False):
    st.switch_page("login.py")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: "Plus Jakarta Sans", sans-serif; }
.stApp {
  background:
    radial-gradient(circle at 90% 0%, rgba(218,167,111,.16), transparent 24rem),
    linear-gradient(145deg, #fbf7f0 0%, #fffdf9 70%);
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }
.block-container { max-width: 1320px !important; padding-top: 2.2rem !important; }

.hero {
  position: relative;
  overflow: hidden;
  margin-bottom: 22px;
  padding: 34px 38px;
  border-radius: 24px;
  color: white;
  background:
    linear-gradient(100deg, rgba(61,42,32,.96), rgba(137,91,60,.82)),
    url("https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1600&q=80") center 58%/cover;
  box-shadow: 0 18px 44px rgba(79,52,37,.16);
  animation: riseIn .65s cubic-bezier(.2,.75,.25,1) both;
}
.hero::after {
  content: "";
  position: absolute;
  width: 180px;
  height: 180px;
  right: -70px;
  top: -90px;
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 50%;
  box-shadow: 0 0 0 28px rgba(255,255,255,.025), 0 0 0 56px rgba(255,255,255,.02);
  animation: orbit 14s linear infinite;
}
.hero-kicker {
  margin: 0 0 7px;
  color: #f0c99f;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
}
.hero h1 {
  margin: 0;
  color: white;
  font-size: 34px;
  letter-spacing: -1.5px;
}
.hero p { margin: 8px 0 0; color: rgba(255,255,255,.78); }

.metric-card {
  height: 132px;
  padding: 20px 22px;
  border: 1px solid #eee3d7;
  border-radius: 18px;
  background: rgba(255,255,255,.78);
  box-shadow: 0 10px 30px rgba(99,73,54,.07);
  animation: riseIn .65s cubic-bezier(.2,.75,.25,1) both;
}
.metric-card:nth-child(2) { animation-delay: .08s; }
.metric-card:nth-child(3) { animation-delay: .16s; }
.metric-icon {
  width: 38px;
  height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  border-radius: 12px;
  background: #f4e7d8;
  font-size: 18px;
}
.metric-label { color: #9b8878; font-size: 12px; font-weight: 700; }
.metric-value { margin-top: 2px; color: #463226; font-size: 25px; font-weight: 800; }

.menu-panel {
  margin-top: 18px;
  padding: 24px;
  border: 1px solid #eee3d7;
  border-radius: 22px;
  background: rgba(255,255,255,.82);
  box-shadow: 0 14px 38px rgba(99,73,54,.06);
  animation: riseIn .7s .18s cubic-bezier(.2,.75,.25,1) both;
}
.menu-title {
  margin: 0 0 4px;
  color: #463226;
  font-size: 19px;
  font-weight: 800;
}
.menu-subtitle { margin: 0 0 18px; color: #9b8878; font-size: 13px; }

.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
  border-radius: 12px !important;
  border-color: #e8dccf !important;
  background: #fff !important;
}
.stButton button {
  border: 1px solid #eadfd3;
  border-radius: 12px;
  background: #fff;
  color: #654936;
  transition: all .2s ease;
}
.stButton button:hover {
  border-color: #c98558;
  background: #c98558;
  color: white;
  transform: translateY(-2px);
}
[data-testid="stDataFrame"] {
  border: 1px solid #eee5dc;
  border-radius: 14px;
  overflow: hidden;
}
.menu-card {
  position: relative;
  min-height: 154px;
  margin: 0 0 14px;
  padding: 18px;
  overflow: hidden;
  border: 1px solid #eee3d7;
  border-radius: 17px;
  background: linear-gradient(145deg, #fff 0%, #fffaf4 100%);
  box-shadow: 0 8px 24px rgba(99,73,54,.06);
  transition: transform .22s ease, box-shadow .22s ease;
}
.menu-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 32px rgba(99,73,54,.13);
}
.menu-card-icon {
  display: inline-flex;
  width: 40px;
  height: 40px;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  border-radius: 13px;
  background: #f4e7d8;
  font-size: 20px;
}
.menu-card-name {
  margin: 0 0 5px;
  color: #463226;
  font-size: 15px;
  font-weight: 800;
}
.menu-card-category {
  color: #9b8878;
  font-size: 11px;
  font-weight: 700;
  text-transform: capitalize;
}
.menu-card-price {
  margin-top: 12px;
  color: #b66f43;
  font-size: 16px;
  font-weight: 800;
}
.st-key-order-panel {
  margin-top: 18px;
  padding: 24px;
  border: 1px solid #eee3d7;
  border-radius: 22px;
  background: rgba(255,255,255,.82);
  box-shadow: 0 14px 38px rgba(99,73,54,.06);
  animation: riseIn .7s .12s cubic-bezier(.2,.75,.25,1) both;
}
.order-total {
  margin: 8px 0 14px;
  color: #b66f43;
  font-size: 20px;
  font-weight: 800;
}
.st-key-orders-list {
  margin-top: 18px;
  padding: 24px;
  border: 1px solid #eee3d7;
  border-radius: 22px;
  background: rgba(255,255,255,.82);
  box-shadow: 0 14px 38px rgba(99,73,54,.06);
}
.order-card {
  min-height: 205px;
  margin: 8px 0;
  padding: 20px;
  border: 1px solid #eee5dc;
  border-radius: 18px;
  background: linear-gradient(145deg, #fff 0%, #fffaf5 100%);
  box-shadow: 0 8px 24px rgba(99,73,54,.06);
  animation: riseIn .45s ease both;
  transition: transform .2s ease, box-shadow .2s ease;
}
.order-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 30px rgba(99,73,54,.12);
}
.order-card-header, .order-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.order-id {
  color: #a98264;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1px;
}
.order-time {
  margin-top: 4px;
  color: #aa9b8e;
  font-size: 11px;
}
.order-status {
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  white-space: nowrap;
}
.order-status-new { background: #fff0d9; color: #a96a19; }
.order-status-processing { background: #e8efff; color: #4567a8; }
.order-status-completed { background: #e4f5ea; color: #378153; }
.order-status-cancelled { background: #fce8e7; color: #b74b43; }
.order-customer {
  margin: 18px 0 3px;
  color: #463226;
  font-size: 17px;
  font-weight: 800;
}
.order-item {
  color: #806d5e;
  font-size: 13px;
}
.order-lines {
  display: grid;
  gap: 7px;
  margin-top: 12px;
}
.order-line {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  color: #806d5e;
  font-size: 12px;
}
.order-line-name { overflow-wrap: anywhere; }
.order-line-price { color: #604b3b; font-weight: 700; white-space: nowrap; }
.order-table {
  margin-top: 3px;
  color: #aa9b8e;
  font-size: 11px;
}
.order-category {
  display: inline-block;
  margin-left: 5px;
  padding: 3px 8px;
  border-radius: 999px;
  background: #f4e7d8;
  color: #8d6244;
  font-size: 10px;
  font-weight: 700;
  text-transform: capitalize;
}
.order-note {
  margin-top: 12px;
  padding: 8px 10px;
  border-left: 2px solid #d5a176;
  border-radius: 0 8px 8px 0;
  background: #fbf3ea;
  color: #806d5e;
  font-size: 11px;
  overflow-wrap: anywhere;
}
.order-card-footer {
  margin-top: 15px;
  padding-top: 12px;
  border-top: 1px solid #f0e8df;
}
.order-quantity {
  color: #9b8878;
  font-size: 12px;
  font-weight: 600;
}
.order-total-value {
  color: #b66f43;
  font-size: 17px;
  font-weight: 800;
}

@keyframes riseIn {
  from { opacity: 0; transform: translateY(18px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes orbit { to { transform: rotate(360deg); } }

@media (max-width: 760px) {
  .block-container { padding: 1rem 12px !important; }
  .hero { padding: 28px 24px; }
  .hero h1 { font-size: 28px; }
  .metric-card { height: 118px; margin-bottom: 8px; }
}
</style>
""", unsafe_allow_html=True)

username = escape(str(st.session_state.get("username", "Admin")))

st.markdown(f"""
<section class="hero">
  <p class="hero-kicker">Dashboard utama</p>
  <h1>Selamat datang, {username} 👋</h1>
  <p>Kelola dan temukan menu kafe Anda dalam satu tampilan.</p>
</section>
""", unsafe_allow_html=True)

data = pd.DataFrame()
database_error = None

try:
    db = connect_db()
    try:
        cursor = db.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pesanan (
                    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nama_pelanggan VARCHAR(100) NOT NULL,
                    nama_menu VARCHAR(100) NOT NULL,
                    kategori VARCHAR(50) NOT NULL,
                    jumlah INT UNSIGNED NOT NULL,
                    harga_satuan INT UNSIGNED NOT NULL,
                    total_harga BIGINT UNSIGNED NOT NULL,
                    kode_pesanan VARCHAR(36) NULL,
                    nomor_meja INT UNSIGNED NULL,
                    catatan VARCHAR(500) NULL,
                    status VARCHAR(30) NOT NULL DEFAULT 'baru',
                    dibuat_pada TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    INDEX idx_pesanan_kode_pesanan (kode_pesanan)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """)
            cursor.execute("SHOW COLUMNS FROM pesanan")
            order_columns = {column[0] for column in cursor.fetchall()}
            if "kode_pesanan" not in order_columns:
                cursor.execute(
                    "ALTER TABLE pesanan ADD COLUMN kode_pesanan VARCHAR(36) NULL"
                )
            if "nomor_meja" not in order_columns:
                cursor.execute(
                    "ALTER TABLE pesanan ADD COLUMN nomor_meja INT UNSIGNED NULL"
                )
            cursor.execute("SHOW INDEX FROM pesanan")
            order_indexes = {index[2] for index in cursor.fetchall()}
            if "idx_pesanan_kode_pesanan" not in order_indexes:
                cursor.execute(
                    "ALTER TABLE pesanan ADD INDEX idx_pesanan_kode_pesanan (kode_pesanan)"
                )
        finally:
            cursor.close()
        data = pd.read_sql("SELECT * FROM menu", db)
    finally:
        db.close()
except Exception as exc:
    database_error = exc

if database_error:
    st.error(f"Tidak dapat memuat data menu: {database_error}")
else:
    lower_columns = {str(column).lower(): column for column in data.columns}

    name_col = lower_columns.get("nama_menu") or lower_columns.get("nama") or lower_columns.get("menu")
    price_col = lower_columns.get("harga") or lower_columns.get("price")
    category_col = lower_columns.get("kategori") or lower_columns.get("category")

    menu_data = data.drop_duplicates().copy()
    price_values = pd.to_numeric(menu_data[price_col], errors="coerce") if price_col else pd.Series(dtype="float")
    total_menu = len(menu_data)
    average_price = price_values.mean() if not price_values.dropna().empty else 0
    category_count = menu_data[category_col].nunique(dropna=True) if category_col else 0

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">🍽️</div><div class="metric-label">TOTAL MENU</div><div class="metric-value">{total_menu}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">💰</div><div class="metric-label">RATA-RATA HARGA</div><div class="metric-value">Rp {average_price:,.0f}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">🏷️</div><div class="metric-label">JUMLAH KATEGORI</div><div class="metric-value">{category_count}</div></div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown('<div class="menu-title">Daftar Menu</div><div class="menu-subtitle">Cari dan filter pilihan menu kafe Anda.</div>', unsafe_allow_html=True)

        filter_col1, filter_col2, action_col = st.columns([2, 1.2, .5])
        with filter_col1:
            search = st.text_input("Cari menu", placeholder="Ketik nama menu...")
        with filter_col2:
            category = "Semua kategori"
            if category_col:
                categories = ["Semua kategori"] + sorted(menu_data[category_col].dropna().astype(str).unique().tolist())
                category = st.selectbox("Kategori", categories)
            else:
                st.selectbox("Kategori", ["Semua kategori"], disabled=True)
        with action_col:
            st.write("")
            st.write("")
            if st.button("Keluar", use_container_width=True):
                st.session_state["authenticated"] = False
                st.session_state.pop("username", None)
                st.session_state.pop("order_basket", None)
                st.session_state.pop("last_order_confirmation", None)
                st.switch_page("login.py")

        filtered = menu_data.copy()
        if search and name_col:
            filtered = filtered[
                filtered[name_col].astype(str).str.contains(search, case=False, na=False)
            ]
        if category != "Semua kategori" and category_col:
            filtered = filtered[filtered[category_col].astype(str) == category]

        if not filtered.empty and name_col and price_col and category_col:
            cards_per_row = 3
            menu_rows = filtered.to_dict("records")
            for start in range(0, len(menu_rows), cards_per_row):
                cards = st.columns(cards_per_row)
                for card, row in zip(cards, menu_rows[start:start + cards_per_row]):
                    category_name = str(row[category_col])
                    icon = "☕" if category_name.lower() == "minuman" else "🍽️"
                    menu_name = escape(str(row[name_col]))
                    safe_category = escape(category_name)
                    price = pd.to_numeric(row[price_col], errors="coerce")
                    price_text = f"Rp {price:,.0f}" if pd.notna(price) else "Harga belum tersedia"
                    with card:
                        st.markdown(
                            f'<div class="menu-card">'
                            f'<div class="menu-card-icon">{icon}</div>'
                            f'<div class="menu-card-name">{menu_name}</div>'
                            f'<div class="menu-card-category">{safe_category}</div>'
                            f'<div class="menu-card-price">{price_text}</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )
        elif not filtered.empty:
            st.dataframe(filtered, use_container_width=True, hide_index=True)
        else:
            st.info("Menu tidak ditemukan untuk filter yang dipilih.")

    with st.container(key="order-panel", border=True):
        st.markdown('<div class="menu-title">Buat Pesanan</div><div class="menu-subtitle">Pilih beberapa menu untuk satu meja dan simpan sekaligus.</div>', unsafe_allow_html=True)

        if menu_data.empty or not name_col or not price_col or not category_col:
            st.info("Belum ada data menu yang dapat dipesan.")
        else:
            order_options = menu_data[[name_col, category_col, price_col]].drop_duplicates().to_dict("records")
            customer_name = st.text_input(
                "Nama pelanggan",
                max_chars=100,
                key="order_customer_name",
            )
            table_number = st.number_input(
                "Nomor meja",
                min_value=1,
                step=1,
                value=1,
                key="order_table_number",
            )
            order_note = st.text_area(
                "Catatan untuk seluruh pesanan (opsional)",
                max_chars=500,
                key="order_note",
            )

            add_col, quantity_col = st.columns([2, 1])
            with add_col:
                selected_index = st.selectbox(
                    "Pilih menu",
                    options=range(len(order_options)),
                    format_func=lambda index: (
                        f"{order_options[index][name_col]} · "
                        f"{order_options[index][category_col]} · "
                        f"Rp {int(order_options[index][price_col]):,}"
                    ),
                    key="order_menu_choice",
                )
            with quantity_col:
                quantity_to_add = st.number_input(
                    "Jumlah",
                    min_value=1,
                    step=1,
                    value=1,
                    key="order_menu_quantity",
                )

            if st.button("Tambahkan menu", key="add_order_item", use_container_width=True):
                selected_menu = order_options[selected_index]
                basket = st.session_state.setdefault("order_basket", [])
                existing_item = next(
                    (
                        item for item in basket
                        if item["name"] == str(selected_menu[name_col])
                        and item["category"] == str(selected_menu[category_col])
                        and item["price"] == int(selected_menu[price_col])
                    ),
                    None,
                )
                if existing_item:
                    existing_item["quantity"] += int(quantity_to_add)
                else:
                    basket.append({
                        "name": str(selected_menu[name_col]),
                        "category": str(selected_menu[category_col]),
                        "price": int(selected_menu[price_col]),
                        "quantity": int(quantity_to_add),
                    })
                st.session_state.pop("last_order_confirmation", None)

            basket = st.session_state.setdefault("order_basket", [])
            if basket:
                st.markdown("#### Isi pesanan")
                for item_index, item in enumerate(list(basket)):
                    item_col, quantity_display_col, remove_col = st.columns([3, 1, 1])
                    with item_col:
                        st.write(f"**{item['name']}** · {item['category']}")
                    with quantity_display_col:
                        st.write(f"{item['quantity']} × Rp {item['price']:,}")
                    with remove_col:
                        if st.button(
                            "Hapus",
                            key=f"remove_order_item_{item_index}",
                        ):
                            basket.pop(item_index)
                            st.rerun()

                order_total = sum(
                    item["price"] * item["quantity"] for item in basket
                )
                st.markdown(
                    f'<div class="order-total">Total pesanan: Rp {order_total:,}</div>',
                    unsafe_allow_html=True,
                )
            else:
                order_total = 0
                st.info("Tambahkan satu atau beberapa menu untuk mulai membuat pesanan.")

            confirmation = st.session_state.pop("last_order_confirmation", None)
            if confirmation:
                st.success(
                    f"Pesanan {confirmation['code']} untuk meja "
                    f"{confirmation['table']} berhasil disimpan. "
                    f"Total: Rp {confirmation['total']:,}"
                )
                if confirmation["whatsapp_url"]:
                    st.link_button(
                        "Buka WhatsApp & kirim pesanan",
                        confirmation["whatsapp_url"],
                        type="primary",
                        use_container_width=True,
                    )
                    st.caption("Pesan sudah terisi di WhatsApp. Periksa lalu tekan Kirim.")
                else:
                    st.warning("Nomor WhatsApp tujuan belum valid.")

            if st.button(
                "Simpan semua pesanan",
                key="save_order",
                disabled=not basket,
                use_container_width=True,
            ):
                if not customer_name.strip():
                    st.error("Nama pelanggan wajib diisi.")
                else:
                    order_code = uuid4().hex.upper()
                    whatsapp_url = None
                    if WHATSAPP_PHONE.isdigit() and 8 <= len(WHATSAPP_PHONE) <= 15:
                        item_lines = "\n".join(
                            f"- {item['quantity']} x {item['name']} "
                            f"({item['category']}) — Rp "
                            f"{item['price'] * item['quantity']:,}"
                            for item in basket
                        )
                        message_parts = [
                            "Pesanan baru - Kafe Nusantara",
                            f"Kode: {order_code[:8]}",
                            f"Meja: {int(table_number)}",
                            f"Pelanggan: {customer_name.strip()}",
                            "",
                            "Detail pesanan:",
                            item_lines,
                            "",
                            f"Total: Rp {order_total:,}",
                        ]
                        if order_note.strip():
                            message_parts.extend(["", f"Catatan: {order_note.strip()}"])
                        whatsapp_url = (
                            f"https://wa.me/{WHATSAPP_PHONE}"
                            f"?text={quote(chr(10).join(message_parts), safe='')}"
                        )
                    order_db = None
                    cursor = None
                    try:
                        order_db = connect_db()
                        cursor = order_db.cursor()
                        cursor.executemany(
                            """
                            INSERT INTO pesanan
                                (nama_pelanggan, nama_menu, kategori, jumlah,
                                 harga_satuan, total_harga, kode_pesanan,
                                 nomor_meja, catatan)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            [
                                (
                                    customer_name.strip(),
                                    item["name"],
                                    item["category"],
                                    item["quantity"],
                                    item["price"],
                                    item["price"] * item["quantity"],
                                    order_code,
                                    int(table_number),
                                    order_note.strip() or None,
                                )
                                for item in basket
                            ],
                        )
                        order_db.commit()
                        st.session_state["order_basket"] = []
                        st.session_state["last_order_confirmation"] = {
                            "code": order_code[:8],
                            "table": int(table_number),
                            "total": order_total,
                            "whatsapp_url": whatsapp_url,
                        }
                        st.rerun()
                    except mysql.connector.Error as exc:
                        if order_db is not None:
                            order_db.rollback()
                        st.error(f"Pesanan gagal disimpan: {exc}")
                    finally:
                        if cursor is not None:
                            cursor.close()
                        if order_db is not None:
                            order_db.close()

    try:
        orders_db = connect_db()
        try:
            orders = pd.read_sql(
                """
                SELECT id AS 'No. Pesanan', nama_pelanggan AS 'Pelanggan',
                       nama_menu AS 'Menu', kategori AS 'Kategori',
                       jumlah AS 'Jumlah', harga_satuan AS 'Harga Satuan',
                       total_harga AS 'Total', catatan AS 'Catatan',
                       status AS 'Status', dibuat_pada AS 'Waktu',
                       kode_pesanan AS 'Kode Pesanan',
                       nomor_meja AS 'Nomor Meja'
                FROM pesanan
                ORDER BY dibuat_pada DESC, id DESC
                """,
                orders_db,
            )
        finally:
            orders_db.close()

        with st.container(key="orders-list", border=True):
            st.markdown('<div class="menu-title">Pesanan Terbaru</div><div class="menu-subtitle">20 transaksi terakhir yang tersimpan.</div>', unsafe_allow_html=True)
            if orders.empty:
                st.info("Belum ada pesanan.")
            else:
                grouped_orders = {}
                for row in orders.to_dict("records"):
                    order_code = row["Kode Pesanan"]
                    group_key = (
                        str(order_code)
                        if pd.notna(order_code)
                        else f"legacy-{row['No. Pesanan']}"
                    )
                    if group_key not in grouped_orders:
                        grouped_orders[group_key] = {
                            "id": int(row["No. Pesanan"]),
                            "code": str(order_code) if pd.notna(order_code) else "",
                            "customer": str(row["Pelanggan"]),
                            "table": row["Nomor Meja"],
                            "status": str(row["Status"]),
                            "time": row["Waktu"],
                            "note": row["Catatan"],
                            "items": [],
                            "total": 0,
                            "quantity": 0,
                        }
                    grouped_order = grouped_orders[group_key]
                    grouped_order["items"].append({
                        "name": str(row["Menu"]),
                        "category": str(row["Kategori"]),
                        "quantity": int(row["Jumlah"]),
                        "price": int(row["Harga Satuan"]),
                        "total": int(row["Total"]),
                    })
                    grouped_order["total"] += int(row["Total"])
                    grouped_order["quantity"] += int(row["Jumlah"])

                order_rows = list(grouped_orders.values())[:20]
                for start in range(0, len(order_rows), 2):
                    order_columns = st.columns(2)
                    for column, order in zip(order_columns, order_rows[start:start + 2]):
                        status = order["status"]
                        status_key = status.strip().casefold()
                        status_styles = {
                            "baru": ("new", "●"),
                            "diproses": ("processing", "◷"),
                            "selesai": ("completed", "✓"),
                            "dibatalkan": ("cancelled", "×"),
                        }
                        status_class, status_icon = status_styles.get(
                            status_key,
                            ("new", "●"),
                        )
                        order_time = pd.to_datetime(order["time"], errors="coerce")
                        time_text = (
                            order_time.strftime("%d %b %Y · %H:%M")
                            if pd.notna(order_time)
                            else "Waktu tidak tersedia"
                        )
                        note = str(order["note"]).strip() if pd.notna(order["note"]) else ""
                        note_html = (
                            f'<div class="order-note">Catatan: {escape(note)}</div>'
                            if note
                            else ""
                        )
                        order_label = (
                            f'PESANAN #{escape(order["code"][:8])}'
                            if order["code"]
                            else f'PESANAN #{order["id"]:04d}'
                        )
                        table_text = (
                            f'Meja {int(order["table"])}'
                            if pd.notna(order["table"])
                            else "Meja belum ditentukan"
                        )
                        items_html = "".join(
                            '<div class="order-line">'
                            f'<span class="order-line-name">{item["quantity"]} × '
                            f'{escape(item["name"])} '
                            f'<span class="order-category">{escape(item["category"])}</span></span>'
                            f'<span class="order-line-price">Rp {item["total"]:,}</span>'
                            '</div>'
                            for item in order["items"]
                        )
                        card_html = (
                            '<article class="order-card">'
                            '<div class="order-card-header">'
                            '<div>'
                            f'<div class="order-id">{order_label}</div>'
                            f'<div class="order-time">{escape(time_text)} · {escape(table_text)}</div>'
                            '</div>'
                            f'<span class="order-status order-status-{status_class}">'
                            f'{status_icon} {escape(status)}</span>'
                            '</div>'
                            f'<div class="order-customer">{escape(order["customer"])}</div>'
                            f'<div class="order-lines">{items_html}</div>'
                            f'{note_html}'
                            '<div class="order-card-footer">'
                            f'<span class="order-quantity">{order["quantity"]} item</span>'
                            f'<span class="order-total-value">Rp {order["total"]:,}</span>'
                            '</div>'
                            '</article>'
                        )
                        with column:
                            st.markdown(card_html, unsafe_allow_html=True)
    except mysql.connector.Error as exc:
        st.error(f"Tidak dapat memuat pesanan: {exc}")