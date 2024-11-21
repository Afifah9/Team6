# Tahap 1: Data Preparation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
file_path = "file_dataset.csv"  # Sesuaikan path jika perlu
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

# Isi nilai hilang (jika ada) dengan median
data.fillna(data.median(), inplace=True)

# Simpan data bersih ke file Excel baru
cleaned_file_path = "data_cleaned_project1.xlsx"
data.to_excel(cleaned_file_path, index=False)
print(f"Data bersih telah disimpan ke file: {cleaned_file_path}")

# Buka file Excel hasil data bersih (hanya untuk OS dengan Excel terinstal)
try:
    os.startfile(cleaned_file_path)
    print(f"File {cleaned_file_path} dibuka di Excel.")
except Exception as e:
    print(f"Tidak dapat membuka file: {e}")

# Tahap 2: Exploratory Data Analysis (EDA)

# Visualisasi distribusi variabel numerik
numerical_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']
for col in numerical_columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(data[col], kde=True, bins=30)
    plt.title(f'Distribusi {col}')
    plt.show()

# Korelasi antar variabel
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Variabel')
plt.show()

# Visualisasi Outcome
sns.countplot(data['Outcome'])
plt.title('Distribusi Outcome')
plt.show()

# Visualisasi hubungan antara Glucose dan Outcome
sns.boxplot(x='Outcome', y='Glucose', data=data)
plt.title('Hubungan antara Glucose dan Outcome')
plt.show()

# Visualisasi BMI terhadap Outcome
sns.boxplot(x='Outcome', y='BMI', data=data)
plt.title('Hubungan antara BMI dan Outcome')
plt.show()
