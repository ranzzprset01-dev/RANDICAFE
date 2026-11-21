-- ========================================================
-- RANDI CAFE - SUPABASE / POSTGRESQL DATABASE SCHEMA
-- ========================================================

-- 1. Tabel users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'admin'
);

-- 2. Tabel menu
CREATE TABLE IF NOT EXISTS menu (
    id SERIAL PRIMARY KEY,
    nama_menu VARCHAR(100) NOT NULL,
    kategori VARCHAR(50) NOT NULL,
    harga INTEGER NOT NULL,
    deskripsi TEXT,
    gambar_url TEXT,
    badge VARCHAR(50),
    tersedia BOOLEAN DEFAULT TRUE
);

-- 3. Tabel pesanan
CREATE TABLE IF NOT EXISTS pesanan (
    id BIGSERIAL PRIMARY KEY,
    kode_pesanan VARCHAR(36) NOT NULL,
    nama_pelanggan VARCHAR(100) NOT NULL,
    nomor_meja VARCHAR(50) NOT NULL,
    nama_menu TEXT NOT NULL,
    kategori VARCHAR(50) DEFAULT 'General',
    jumlah INTEGER NOT NULL DEFAULT 1,
    harga_satuan INTEGER NOT NULL DEFAULT 0,
    total_harga BIGINT NOT NULL,
    catatan VARCHAR(500),
    status VARCHAR(30) NOT NULL DEFAULT 'Baru',
    dibuat_pada TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_pesanan_kode_pesanan ON pesanan(kode_pesanan);

-- Aktifkan Realtime di Supabase untuk tabel pesanan
ALTER PUBLICATION supabase_realtime ADD TABLE pesanan;

-- ========================================================
-- DATA AWAL (SEED DATA)
-- ========================================================

-- Akun Login: RANDI / RANDI17112005
INSERT INTO users (username, password, role) VALUES
('RANDI', 'RANDI17112005', 'admin')
ON CONFLICT (username) DO NOTHING;
