"""
Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. Proses ini disebut sebagai “web scraping” atau “web crawling”. Anda bisa menggunakan fungsi dan metode pada library ini untuk mengekstraksi informasi dari situs web dan menyimpannya dalam format yang dapat diakses dan digunakan dalam analisis atau aplikasi lainnya. 

Beberapa library untuk melakukan web scraping adalah berikut.

Beautifulsoup
Beautifulsoup adalah library untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan. Untuk menggunakan beautifulsoup, Anda harus menginstalnya terlebih dahulu. Silakan jalankan kode pip berikut untuk menginstalnya.
pip install beautifulsoup4
"""

# Berikut adalah contoh penulisan kode beautifulsoup.
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)