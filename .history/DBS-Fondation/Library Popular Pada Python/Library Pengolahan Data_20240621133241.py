"""
Pandas
Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.
"""


"""
Silakan buka command prompt dan jalankan kode berikut.
pip install pandas
Atau jika Anda ingin menggunakan conda, silakan jalankan kode berikut untuk menginstalnya.

conda install pandas
"""

"""
Seaborn
Terakhir adalah library seaborn yang termasuk jenis library dengan tujuan untuk visualisasi data sama seperti matplotlib. Bahkan library seaborn dibangun berdasarkan pada library matplotlib.

Seaborn termasuk library eksternal sehingga Anda perlu menginstalnya terlebih dahulu. Silakan jalankan kode berikut untuk menginstalnya menggunakan pip.
pip install seaborn
Anda juga bisa menggunakan conda, silakan gunakan kode berikut.

conda install seaborn
"""

# Berikut adalah contoh penerapan seaborn.
import seaborn as sns
import matplotlib.pyplot as plt
 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()