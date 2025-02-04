# OOP - Python

Laporan OOP - Python

Raflee Caesar Dano Malik

1. Konsep dasar dari "OOP Python"
   https://excalidraw.com/#json=r0VKx_UtNLWSoVpxq-gVS,y5ArYLs3WR5GO1zCOSO-XA
   
<img width="1542" alt="Screen Shot 2025-02-04 at 23 54 45" src="https://github.com/user-attachments/assets/81eddad2-22ab-4cf8-8bf1-844a441722f1" />

2. Class diagram dari "OOP Python"
   <img width="895" alt="Screen Shot 2025-02-04 at 23 56 43" src="https://github.com/user-attachments/assets/326e5491-9bdb-4bad-be47-a9bd13a041d8" />
   
    📌 Di dalam sistem ini, kita memiliki satu kelas utama, yaitu Employee, yang menjadi dasar dari semua tipe pegawai dalam sistem. Kelas Employee memiliki beberapa atribut utama, seperti:
  	•	name: Menyimpan nama pegawai.
	  •	position: Menyimpan jabatan pegawai.
	  •	year_hired: Tahun pegawai direkrut.
	  •	salary: Gaji pegawai.
	  •	hire_date: Tanggal pegawai mulai bekerja.
   
    📌 Selain atribut, Employee juga memiliki dua metode utama: 
	  •	display_info() → Menampilkan informasi pegawai.
	  •	get_annual_salary() → Menghitung dan mengembalikan total gaji tahunan pegawai.
   
    📌 Karena dalam perusahaan ada beberapa jenis pegawai dengan peran yang berbeda, kita membuat tiga subclass yang masing-masing mewarisi atribut dan metode dari Employee, namun memiliki atribut tambahan yang         spesifik untuk peran mereka.
   
    1️⃣ Kelas Manager
	    •	Mewarisi semua atribut dan metode dari Employee.
	    •	Tambahan atribut:
	    ◦	department: Menunjukkan departemen yang dikelola oleh Manager.
	    ◦	team: Berisi daftar anggota tim yang berada di bawah Manager.
	    •	Metode display_info() dimodifikasi untuk menampilkan informasi departemen dan tim.
   
    2️⃣ Kelas Engineer
    	•	Mewarisi semua atribut dan metode dari Employee.
	    •	Tambahan atribut:
	    ◦	expertise: Menunjukkan bidang keahlian Engineer.
	    ◦	certifications: Menyimpan daftar sertifikasi yang dimiliki oleh Engineer.
	    •	Metode display_info() ditambahkan untuk menampilkan informasi keahlian dan sertifikasi.
   
    3️⃣ Kelas Intern
	    •	Mewarisi semua atribut dan metode dari Employee.
	    •	Tambahan atribut:
	    ◦	duration: Menyimpan durasi magang dalam bulan.
	    ◦	mentor: Menunjukkan siapa mentor dari Intern.
	    •	Metode display_info() diperbarui untuk menampilkan informasi durasi magang dan mentor.

3. Use Case diagram dari "OOP Python"
   <img width="842" alt="Screen Shot 2025-02-04 at 23 59 04" src="https://github.com/user-attachments/assets/444e5303-a0ae-40e8-8998-768d664bc2cf" />
   
   📌 Terdapat tiga use case utama dalam sistem ini:
  1️⃣ Create Employee (Membuat Pegawai Baru)
	  •	Admin/HR Manager dapat menambahkan data pegawai baru ke dalam sistem.
	  •	Data yang dimasukkan meliputi nama, posisi, tahun bergabung, gaji, dan tanggal perekrutan.
	  •	Setelah data dimasukkan, sistem akan menyimpan informasi pegawai tersebut.
   
  2️⃣ View Employee Info (Melihat Informasi Pegawai)
  	•	Admin/HR Manager dapat mencari dan melihat informasi detail dari seorang pegawai.
	  •	Informasi yang ditampilkan termasuk nama, posisi, gaji, dan tanggal perekrutan.
	  •	Fitur ini membantu HR dalam pengelolaan pegawai.
   
  3️⃣ Calculate Annual Salary (Menghitung Gaji Tahunan)
  	•	Admin/HR Manager dapat menghitung gaji tahunan seorang pegawai berdasarkan gaji bulanan yang tersimpan dalam sistem.
	  •	Sistem akan secara otomatis mengalikan gaji bulanan dengan 12 bulan untuk memberikan total gaji tahunan.
	  •	Fitur ini penting untuk evaluasi keuangan dan pengelolaan anggaran perusahaan.

4. Sequence diagram dari "OOP Python"
   <img width="876" alt="Screen Shot 2025-02-05 at 00 00 05" src="https://github.com/user-attachments/assets/daaddbce-93b7-4434-8088-25aac18e07c4" />

   📌 1. Gambaran Umum "Sequence Diagram ini menggambarkan bagaimana sistem kita bekerja dalam skenario utama, yaitu proses pembuatan dan pengelolaan data karyawan dalam aplikasi.
   
   📌 2. Aktor dan Objek Utama "Di dalam diagram ini, ada beberapa komponen utama yang perlu kita perhatikan:
	    •	Main Program (Sebagai inisiasi utama sistem)
	    •	Manager (Karyawan yang memiliki tim dan departemen)
	    •	Engineer (Karyawan dengan keahlian teknis tertentu)
	    •	Intern (Pegawai magang dengan durasi tertentu)

  📌 3. Alur Interaksi "Proses utama dalam diagram ini adalah sebagai berikut: 
      1️⃣ Main Program pertama-tama akan menciptakan objek Manager, Engineer, dan Intern dengan informasi detail seperti nama, posisi, tahun   perekrutan, gaji, dan atribut tambahan masing-masing. 
      2️⃣ Setelah objek dibuat, sistem memanggil fungsi display_info() untuk menampilkan informasi lengkap dari setiap karyawan. 
      3️⃣ Setelah itu, sistem juga memanggil fungsi get_annual_salary() untuk menghitung dan mengembalikan gaji tahunan dari setiap karyawan.
      Jadi, Sequence Diagram ini membantu kita untuk melihat alur komunikasi antar objek secara sistematis dan memastikan bahwa semua proses berjalan dengan baik sesuai desain.




   
