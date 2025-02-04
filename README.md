# 🚀 OOP - Python

## 📄 Laporan OOP - Python
**👨‍💻 Raflee Caesar Dano Malik**

---

## 🔹 1. Konsep Dasar dari "OOP Python"
🔗 [Diagram Konsep OOP Python](https://excalidraw.com/#json=r0VKx_UtNLWSoVpxq-gVS,y5ArYLs3WR5GO1zCOSO-XA)

![Konsep OOP Python](https://github.com/user-attachments/assets/81eddad2-22ab-4cf8-8bf1-844a441722f1)

---

## 🔹 2. Class Diagram dari "OOP Python"
![Class Diagram OOP](https://github.com/user-attachments/assets/326e5491-9bdb-4bad-be47-a9bd13a041d8)

### 📌 **Struktur Kelas Employee**
💠 **Kelas Employee** _(Superclass)_
- **Atribut:**
  - `name` → Nama pegawai
  - `position` → Jabatan pegawai
  - `year_hired` → Tahun pegawai direkrut
  - `salary` → Gaji pegawai
  - `hire_date` → Tanggal mulai bekerja
- **Metode:**
  - `display_info()` → Menampilkan informasi pegawai
  - `get_annual_salary()` → Menghitung gaji tahunan pegawai

### 🔥 **Subclass Employee**
#### 1️⃣ **Kelas Manager**
- **Tambahan Atribut:**
  - `department` → Departemen yang dikelola
  - `team` → Daftar anggota tim
- **Modifikasi:**
  - `display_info()` menampilkan informasi departemen & tim

#### 2️⃣ **Kelas Engineer**
- **Tambahan Atribut:**
  - `expertise` → Keahlian teknis
  - `certifications` → Daftar sertifikasi
- **Modifikasi:**
  - `display_info()` menampilkan keahlian & sertifikasi

#### 3️⃣ **Kelas Intern**
- **Tambahan Atribut:**
  - `duration` → Durasi magang (bulan)
  - `mentor` → Mentor selama magang
- **Modifikasi:**
  - `display_info()` menampilkan informasi magang & mentor

---

## 🔹 3. Use Case Diagram dari "OOP Python"
![Use Case Diagram OOP](https://github.com/user-attachments/assets/444e5303-a0ae-40e8-8998-768d664bc2cf)

### 📌 **Use Cases dalam Sistem**

✅ **1️⃣ Create Employee (Membuat Pegawai Baru)**
- Admin/HR Manager dapat menambahkan data pegawai baru
- Data yang dimasukkan meliputi **nama, posisi, tahun bergabung, gaji, dan tanggal perekrutan**
- Sistem akan menyimpan informasi pegawai

✅ **2️⃣ View Employee Info (Melihat Informasi Pegawai)**
- Admin/HR Manager dapat mencari & melihat informasi pegawai
- Informasi mencakup **nama, posisi, gaji, dan tanggal perekrutan**
- Membantu HR dalam pengelolaan pegawai

✅ **3️⃣ Calculate Annual Salary (Menghitung Gaji Tahunan)**
- Admin/HR Manager dapat menghitung gaji tahunan pegawai
- Sistem mengalikan **gaji bulanan × 12 bulan**
- Berguna untuk evaluasi keuangan & pengelolaan anggaran perusahaan

---

## 🔹 4. Sequence Diagram dari "OOP Python"
![Sequence Diagram OOP](https://github.com/user-attachments/assets/daaddbce-93b7-4434-8088-25aac18e07c4)

### 🎯 **Alur Interaksi dalam Sistem**
🔹 **1️⃣ Inisialisasi Objek Pegawai**
   - Main Program menciptakan objek **Manager, Engineer, dan Intern** dengan informasi lengkap.

🔹 **2️⃣ Menampilkan Informasi Pegawai**
   - Sistem memanggil `display_info()` untuk **menampilkan detail pegawai**.

🔹 **3️⃣ Menghitung Gaji Tahunan**
   - Sistem memanggil `get_annual_salary()` untuk **menghitung total gaji tahunan**.

---


