import streamlit as st
import pandas as pd
from math import radians, sin, cos, sqrt, asin
import geocoder
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static
import time

# Title aplikasi
st.title("Implementasi Algoritma Sorting Jarak Hotel Terdekat di Jawa Timur")

# Pilihan input lokasi
st.header("Pilih Metode Input Lokasi")
input_lokasi = st.radio("Metode Input", ["Lokasi Saat Ini", "Nama Tempat/Alamat"])

# Variabel untuk menyimpan koordinat user
lat1, lon1 = None, None

if input_lokasi == "Lokasi Saat Ini":
    g = geocoder.ip('me')
    if g.latlng:
        lat1, lon1 = g.latlng[0], g.latlng[1]
        st.success(f"Lokasi Anda saat ini: Latitude = {lat1}, Longitude = {lon1}")
    else:
        st.error("Gagal mendapatkan lokasi Anda. Pastikan koneksi internet stabil.")

elif input_lokasi == "Nama Tempat/Alamat":
    lokasi_user = st.text_input("Masukkan Nama Tempat/Alamat:")
    if lokasi_user:
        geolocator = Nominatim(user_agent="maps_project_unesa")
        lokasi = geolocator.geocode(lokasi_user)

        if lokasi:
            lat1, lon1 = lokasi.latitude, lokasi.longitude
            st.success(f"Koordinat: Latitude: {lat1}, Longitude: {lon1}")
        else:
            st.error("Lokasi tidak ditemukan. Coba masukkan alamat yang lebih spesifik.")

# Proses jika koordinat tersedia
if lat1 and lon1:
    # Membaca dataset hotel
    baca = pd.read_csv('cleaned_hotel_data.csv')

    # Fungsi Haversine untuk menghitung jarak antara dua koordinat
    def haversine(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = [radians(titik) for titik in [lon1, lat1, lon2, lat2]]
        selisih_lon = lon2 - lon1
        selisih_lat = lat2 - lat1
        a = sin(selisih_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(selisih_lon / 2)**2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius Bumi dalam kilometer
        return c * r

    durasi_merge_sort = []

    B = 0
    while B < 5 :

        start_time = time.perf_counter()

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left = merge_sort(left)
            right = merge_sort(right)

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][1] < right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        end_time = time.perf_counter()

        durasi_merge_sort.append(end_time - start_time)

        B += 1

    jarak_ke_setiap_hotel = []

    for i in range(len(baca)):
        lat2 = baca.iloc[i, 1]
        lon2 = baca.iloc[i, 2]

        b = haversine(lon1, lat1, lon2, lat2)
        jarak_ke_setiap_hotel.append((i, b))

    sorted_hotels_merge = merge_sort(jarak_ke_setiap_hotel)

    total_durasi_merge_sort = sum(durasi_merge_sort)
    ratarata_durasi_merge_sort = total_durasi_merge_sort/len(durasi_merge_sort)

    # Dropdown untuk memilih jumlah hotel yang akan ditampilkan
    jumlah_hotel = st.number_input("Jumlah Hotel yang Ingin Ditampilkan (MAX 5)", min_value=1, max_value=5, step=1, value=1)

    # Menghitung jarak ke setiap hotel dengan Brute Force
    jarak_ke_setiap_hotel = []
    hotel_terdekat_brute = []
    durasi_brute_force = []

    A = 0
    while A < 5 :

        start_time = time.perf_counter()

        for i in range(len(baca)):
            lat2 = baca.iloc[i, 1]
            lon2 = baca.iloc[i, 2]

            a = haversine(lon1, lat1, lon2, lat2)
            jarak_ke_setiap_hotel.append((i,a))

        while True:
            terdekat = jarak_ke_setiap_hotel[0]

            for j in jarak_ke_setiap_hotel:
                if j[1] < terdekat[1]:
                    terdekat = j

            hotel_terdekat_brute.append(terdekat)
            jarak_ke_setiap_hotel.remove(terdekat)

            if jarak_ke_setiap_hotel == []:
                break

        end_time = time.perf_counter()

        durasi_brute_force.append(end_time - start_time)

        A += 1

    total_durasi_brute_force = sum(durasi_brute_force)
    ratarata_durasi_brute_force = sum(durasi_brute_force)/len(durasi_brute_force)

    durasi_insertion_sort = []

    C = 0
    while C < 5 :

        start_time = time.perf_counter()

        def insertion_sort(arr):
                for i in range(1, len(arr)):
                    key = arr[i]
                    j = i - 1
                    
                    while j >= 0 and arr[j][1] > key[1]:
                        arr[j + 1] = arr[j]
                        j -= 1
                    
                    arr[j + 1] = key
                
                return arr
        
        end_time = time.perf_counter()

        durasi_insertion_sort.append(end_time - start_time)
        
        C += 1

    jarak_ke_setiap_hotel = []

    for i in range(len(baca)):
        lat2 = baca.iloc[i, 1]
        lon2 = baca.iloc[i, 2]

        c = haversine(lon1, lat1, lon2, lat2)
        jarak_ke_setiap_hotel.append((i, c))

    hotel_terurut = insertion_sort(jarak_ke_setiap_hotel)

    total_durasi_insertion_sort = sum(durasi_insertion_sort)
    ratarata_durasi_insertion_sort = sum(durasi_insertion_sort)/len(durasi_insertion_sort)

    # Menampilkan hotel terdekat (Brute Force)
    st.header("Hotel-Hotel Terdekat (Brute Force)")
    for j in range(jumlah_hotel):
        hotel_index = hotel_terdekat_brute[j][0]
        jarak = hotel_terdekat_brute[j][1]
        hotel_name = baca.iloc[hotel_index, 0]
        st.write(f"{j+1}. {hotel_name} - Jarak: {jarak:.2f} km")

    st.write(f"Total durasi Brute Force: {total_durasi_brute_force:.6f} detik")

    # Menampilkan hotel terdekat (Merge Sort)
    st.header("Hotel-Hotel Terdekat (Merge Sort)")
    for j in range(jumlah_hotel):
        hotel_index = sorted_hotels_merge[j][0]
        jarak = sorted_hotels_merge[j][1]
        hotel_name = baca.iloc[hotel_index, 0]
        st.write(f"{j+1}. {hotel_name} - Jarak: {jarak:.2f} km")

    st.write(f"Total durasi Merge Sort: {total_durasi_merge_sort:.6f} detik")

    st.header("Hotel-Hotel Terdekat (Insertion Sort)")
    for j in range(jumlah_hotel):
        hotel_index = hotel_terurut[j][0]
        jarak = hotel_terurut[j][1]
        hotel_name = baca.iloc[hotel_index, 0]
        st.write(f"{j+1}. {hotel_name} - Jarak: {jarak:.2f} km")

    st.write(f"Total durasi Insertion Sort: {total_durasi_insertion_sort:.6f} detik")

    # Membuat DataFrame untuk menampilkan hasil
    data = {
    'algoritma': ['Brute Force', 'Merge Sort', 'Insertion Sort'],
    'durasi rata-rata': [ratarata_durasi_brute_force, ratarata_durasi_merge_sort, ratarata_durasi_insertion_sort]
    }

    # Membuat DataFrame dan mengurutkannya berdasarkan durasi rata-rata
    df = pd.DataFrame(data)
    df_sorted = df.sort_values(by='durasi rata-rata')
    df_sorted['rata-rata durasi'] = df_sorted['durasi rata-rata'].apply(lambda x: f"{x:.6f}")

    # Menampilkan header
    st.header("Perbandingan Algoritma")
    st.table(df_sorted[['algoritma', 'rata-rata durasi']])

    # Menampilkan hasil algoritma tercepat
    tercepat_pertama = df_sorted.iloc[0, 1]
    tercepat_kedua = df_sorted.iloc[1, 1]
    tercepat_ketiga = df_sorted.iloc[2, 1]

    persentase2 = (tercepat_ketiga - tercepat_pertama) / tercepat_ketiga * 100
    persentase1 = (tercepat_kedua - tercepat_pertama) / tercepat_kedua * 100

    st.subheader("Analisis")
    st.write(f'{df_sorted.iloc[0, 0]} menjadi algoritma tercepat, yakni {persentase1:.2f}% lebih cepat dari {df_sorted.iloc[1, 0]} dan {persentase2:.2f}% lebih cepat dari {df_sorted.iloc[2, 0]}')

    # Menampilkan algoritma yang sudah diurutkan
    # for index, row in df_sorted.iterrows():
    #     st.write(f"Rata-rata durasi {row['algoritma']}: {row['durasi rata-rata']:.6f} detik")
    # Membuat peta dengan Folium
    peta = folium.Map(location=[lat1, lon1], zoom_start=10)

    # Marker lokasi user
    folium.Marker(
    location=[lat1, lon1],
        popup="Lokasi Anda",
        icon=folium.Icon(color="blue", icon="user"),).add_to(peta)

    warna_garis = ["red", "green", "blue", "purple", "orange"]
    ikon_hotel = ["home", "home", "home", "home", "home"]

        # Menambahkan marker hotel dan garis penghubung (Menggunakan Merge Sort sebagai referensi)
    for idx, (hotel_index, jarak) in enumerate(sorted_hotels_merge[:jumlah_hotel]):
        hotel_data = baca.iloc[hotel_index]
        hotel_lat = hotel_data['Lattitute_cleaned']
        hotel_lon = hotel_data['Longitude_cleaned']
        hotel_name = hotel_data['Hotel Name']

        # marker hotel
        folium.Marker(
            location=[hotel_lat, hotel_lon],
            popup=f"Hotel: {hotel_name}\nJarak: {jarak:.2f} km",
            icon=folium.Icon(color=warna_garis[idx % len(warna_garis)], icon=ikon_hotel[idx % len(ikon_hotel)]),).add_to(peta)

        folium.PolyLine(
            locations=[[lat1, lon1], [hotel_lat, hotel_lon]],
            color=warna_garis[idx % len(warna_garis)],
            weight=2.5,
            opacity=0.8,).add_to(peta)

        folium.Circle(
            location=[hotel_lat, hotel_lon],
            radius=500,  # Radius dalam meter
            color=warna_garis[idx % len(warna_garis)],
            fill=True,
            fill_opacity=0.04,).add_to(peta)

        # Tampilkan peta di Streamlit
    st.header("Visualisasi Peta Hotel Terdekat")
    folium_static(peta)
