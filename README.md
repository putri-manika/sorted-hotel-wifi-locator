# Pencarian Jaringan Wifi Hotel Terdekat di Jawa Timur dengan Algoritma Sorting

## Deskripsi Proyek
Proyek ini mengembangkan aplikasi untuk mencari **hotel dengan jaringan Wifi terdekat** di Jawa Timur berdasarkan lokasi pengguna, menggunakan tiga algoritma pengurutan:

- **Brute Force**
- **Merge Sort** (Divide and Conquer)
- **Insertion Sort** (Decrease and Conquer)

Pengguna dapat memasukkan lokasi secara manual atau otomatis berdasarkan alamat IP. Sistem akan mengembalikan 5 hotel terdekat dan memvisualisasikannya dalam peta interaktif.

---

## Tujuan
- Mengembangkan sistem pencarian hotel terdekat berdasarkan lokasi geografis di Jawa Timur.
- Menerapkan dan membandingkan tiga algoritma sorting berdasarkan performa dan waktu eksekusi.
- Menampilkan hasil pencarian secara visual dengan peta interaktif.

---

## Dataset
- **Sumber**: [Kaggle - Hotel Jawa Timur](https://www.kaggle.com/datasets/thedevastator/tourists-attractions-in-indonesia?select=hotel-jatim.csv)
- **Fitur**: Nama hotel, alamat, rating, harga, fasilitas, dan koordinat (latitude, longitude).
- **Tujuan**: Menghitung jarak dari lokasi pengguna ke hotel dan mengurutkannya berdasarkan kedekatan.

---

## Metodologi

### 1. Praproses Data
- Pembersihan kolom latitude dan longitude.
- Validasi nilai koordinat agar berada dalam rentang yang sesuai.
- Simpan hasil ke file `cleaned_hotel_data.csv`.

### 2. Fungsi Haversine
- Menghitung jarak lintas bumi dari lokasi pengguna ke tiap hotel.

### 3. Lokasi Pengguna
- Input dari alamat IP (otomatis) atau nama tempat (manual).
- Konversi alamat ke koordinat menggunakan **Geocoder** dan **Nominatim**.

### 4. Algoritma Pengurutan

#### a. Brute Force
- Menghitung jarak semua hotel dan membandingkannya secara manual.
- Kompleksitas: O(n²)

#### b. Merge Sort
- Pembagian array secara rekursif dan penggabungan hasil urutan.
- Kompleksitas: O(n log n)

#### c. Insertion Sort
- Menyisipkan elemen satu per satu ke posisi terurut.
- Efektif untuk dataset kecil.

### 5. Visualisasi
- Menggunakan **Folium** untuk menampilkan lokasi pengguna dan hotel.
- Menampilkan 5 hotel terdekat dengan garis dan radius.

---

## Hasil Evaluasi

| Algoritma        | Rata-rata Waktu Eksekusi | Catatan                          |
|------------------|---------------------------|----------------------------------|
| Brute Force      | 0.02878 detik             | Paling lambat, tidak efisien     |
| Merge Sort       | 0.000004 detik            | Sangat efisien dan stabil        |
| Insertion Sort   | 0.000003 detik            | Paling cepat untuk dataset kecil |

> Insertion Sort lebih unggul dalam kasus dataset kecil (105 baris).

---

## 🌍 Fitur Aplikasi
- Input lokasi pengguna via IP atau manual.
- Menghitung jarak ke hotel dengan Haversine.
- Pengurutan menggunakan 3 algoritma berbeda.
- Peta interaktif dengan hotel terdekat.
- Output disimpan sebagai `peta_hotel_terdekat.html`.

---

## 👥 Anggota Kelompok
| Nama                        | NIM           | 
|-----------------------------|---------------|
| Putri Manika Rukmamaya      | 23031554091   | 
| Dimas Fatkhul Rahman        | 23031554211   | 
| Mixal Zamzami Ahmad         | 23031554169   | 

---

## Kesimpulan
- **Brute Force** memiliki performa paling lambat dan tidak efisien.
- **Merge Sort** efisien untuk dataset besar.
- **Insertion Sort** terbukti paling optimal untuk dataset kecil karena overhead yang rendah.
- Pemilihan algoritma harus disesuaikan dengan karakteristik dan ukuran data.
- Sistem ini mampu memberikan hasil pencarian hotel terdekat secara cepat dan akurat, serta dapat dikembangkan lebih lanjut untuk sektor pariwisata berbasis lokasi.
