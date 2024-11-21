# Tahap 1: Data Preparation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "data.csv"  # Sesuaikan path jika perlu
data = pd.read_csv(file_path)

# Informasi dataset
print("Informasi dataset:")
print(data.info())

# Statistik deskriptif
print("\nStatistik deskriptif:")
print(data.describe())

# Cek nilai yang hilang
print("\nJumlah nilai yang hilang per kolom:")
print(data.isnull().sum())

# Isi nilai hilang pada kolom non-numerik dengan string 'Missing'
data.fillna(value={'badan_usaha': 'Missing', 'penanggung_jawab': 'Missing',
                   'no_telepon': 'Missing', 'no_fax': 'Missing'}, inplace=True)

# Ekstraksi angka dari kolom kapasitas
if 'kapasitas' in data.columns:
    data['kapasitas_numeric'] = pd.to_numeric(
        data['kapasitas'].str.extract(r'(\d+)', expand=False), errors='coerce'
    )

# Tambahkan kolom numerik jika ada
numerical_columns = data.select_dtypes(include=[np.number]).columns

# Simpan data bersih ke file Excel baru
cleaned_file_path = "data_cleaned.xlsx"
data.to_excel(cleaned_file_path, index=False)
print(f"Data bersih telah disimpan ke file: {cleaned_file_path}")

# Tahap 2: Exploratory Data Analysis (EDA)
# Visualisasi distribusi variabel numerik
if len(numerical_columns) > 0:
    for col in numerical_columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data[col].dropna(), kde=True, bins=30)
        plt.title(f'Distribusi {col}')
        plt.show()
else:
    print("Tidak ada kolom numerik untuk divisualisasikan.")

# Korelasi antar variabel numerik
if len(numerical_columns) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[numerical_columns].corr(), annot=True, cmap='coolwarm')
    plt.title('Korelasi Antar Variabel')
    plt.show()
else:
    print("Tidak ada cukup kolom numerik untuk membuat heatmap.")

# Visualisasi Outcome (jika kolom Outcome ada)
if 'Outcome' in data.columns:
    sns.countplot(data['Outcome'])
    plt.title('Distribusi Outcome')
    plt.show()

    # Visualisasi hubungan variabel numerik dengan Outcome
    for col in numerical_columns:
        if col != 'Outcome':
            sns.boxplot(x='Outcome', y=col, data=data)
            plt.title(f'Hubungan antara {col} dan Outcome')
            plt.show()
