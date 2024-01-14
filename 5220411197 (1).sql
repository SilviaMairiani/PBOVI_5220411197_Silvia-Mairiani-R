-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Jan 2024 pada 17.27
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411197`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `loket`
--

CREATE TABLE `loket` (
  `id` int(15) NOT NULL,
  `nama_loket` varchar(30) NOT NULL,
  `lokasi` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `loket`
--

INSERT INTO `loket` (`id`, `nama_loket`, `lokasi`) VALUES
(1, 'maju jaya', 'godean'),
(3, 'jaya 3', 'bantul'),
(4, 'cahaya bersama', 'bantul'),
(5, 'maju 2', 'sleman'),
(6, 'cahaya 4', 'malang'),
(7, 'bersama 1', 'malang');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penjualan`
--

CREATE TABLE `penjualan` (
  `no_ktp` int(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nama_loket` varchar(30) NOT NULL,
  `keberangkatan` varchar(30) NOT NULL,
  `tujuan` varchar(30) NOT NULL,
  `kelas` varchar(15) NOT NULL,
  `harga` int(15) NOT NULL,
  `banyak` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penjualan`
--

INSERT INTO `penjualan` (`no_ktp`, `nama`, `nama_loket`, `keberangkatan`, `tujuan`, `kelas`, `harga`, `banyak`) VALUES
(123678, 'vivi', 'maju jaya', 'godean', 'malang', 'ekonomi', 600000, 1),
(342567, 'nayla', 'jaya 3', 'yogyakarta', 'sulawesi', 'ekonomi', 2300000, 1),
(678543, 'vava', 'bersama 1', 'malang', 'malaysia', 'bisnis', 3000000, 1),
(987654, 'nini', 'cahaya 4', 'malang', 'lombok', 'ekonomi', 800000, 1),
(1234567, 'silvia', 'maju jaya', 'yogyakarta', 'bali', 'ekonomi', 1000000, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tiket_pesawat`
--

CREATE TABLE `tiket_pesawat` (
  `id` int(15) NOT NULL,
  `nama_loket` varchar(30) NOT NULL,
  `lokasi` varchar(30) NOT NULL,
  `keberangkatan` varchar(15) DEFAULT NULL,
  `tujuan` varchar(50) DEFAULT NULL,
  `kelas` varchar(50) DEFAULT NULL,
  `harga` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tiket_pesawat`
--

INSERT INTO `tiket_pesawat` (`id`, `nama_loket`, `lokasi`, `keberangkatan`, `tujuan`, `kelas`, `harga`) VALUES
(3, 'maju jaya', 'godean', 'yogyakarta', 'bali', 'ekonomi', '1000000'),
(4, 'maju jaya', 'godean', 'yogyakarta', 'surabaya', 'ekonomi', '700000'),
(5, 'jaya 3', 'bantul', 'yogyakarta', 'sulawesi', 'ekonomi', '2300000'),
(6, 'cahaya 4', 'malang', 'malang', 'lombok', 'ekonomi', '800000'),
(7, 'bersama 1', 'malang', 'malang', 'malaysia', 'bisnis', '3000000');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `loket`
--
ALTER TABLE `loket`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `penjualan`
--
ALTER TABLE `penjualan`
  ADD PRIMARY KEY (`no_ktp`);

--
-- Indeks untuk tabel `tiket_pesawat`
--
ALTER TABLE `tiket_pesawat`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `loket`
--
ALTER TABLE `loket`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `tiket_pesawat`
--
ALTER TABLE `tiket_pesawat`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
