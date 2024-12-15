import requests

# Kamus untuk menerjemahkan deskripsi cuaca
kamus_cuaca = {
    'clear sky': 'cerah',
    'few clouds': 'awan sebagian',
    'broken clouds': 'berawan sebagian',
    'overcast clouds': 'mendung',
    'moderate rain': 'hujan sedang',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',
    'rain': 'hujan',
    'thunderstorm': 'badai petir',
    'snow': 'salju',
    'mist': 'kabut',
}

# Fungsi untuk mengambil data cuaca
def ambil_data_cuaca(kota, api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memastikan tidak ada error dari HTTP
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error 401: Unauthorized. Periksa API Key Anda.")
        else:
            print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Kesalahan lain: {err}")
    return None

# Fungsi untuk menganalisis data cuaca
def analisis_cuaca(data):
    if data is None:
        print("Tidak ada data untuk dianalisis.")
        return
    
    forecast_list = data.get('list', [])
    dates = []
    temperatures = []
    humidities = []
    descriptions = []

    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]  # Mengambil tanggal
        dates.append(date)
        temperatures.append(item['main']['temp'])  # Mengambil suhu
        humidities.append(item['main']['humidity'])  # Mengambil kelembaban
        desc = item['weather'][0]['description']  # Mengambil deskripsi cuaca
        descriptions.append(kamus_cuaca.get(desc, desc))  # Menerjemahkan deskripsi cuaca

    # Mencetak data cuaca
    print("Tanggal       | Suhu (C) | Kelembapan (%) | Deskripsi Cuaca")
    print("-" * 55)
    for i in range(len(dates)):
        print(f"{dates[i]:<12} | {temperatures[i]:<8} | {humidities[i]:<13} | {descriptions[i]}")

# Meminta input dari pengguna dan menampilkan analisis cuaca
def main():
    kota = input("Masukkan Nama Kota: ")
    api_key = "aef59a82761d2a87c80f1b3473f55c11"  # Ganti dengan API key Anda
    data_cuaca = ambil_data_cuaca(kota, api_key)
    analisis_cuaca(data_cuaca)

if _name_ == "_main_":
    main()

