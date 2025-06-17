# Finale Project Cloud Computing
<div align="center">
    <a href="https://docs.google.com/document/d/1-E_JjysibYCLHvg31IF_ZUP5xFzLmM0nlyJYOrQ7xWY/edit?tab=t.0">Laporan</a>
</div>

## File Utama
- Folder frontend: berisikan script pembuatan website
- Folder pyscript: berisikan script python untuk melakukan running 

## Kontributor
- Amellia Harmaimun Hidayah (23083010034)
- Diana Novitasari (23083010014)
- Muhammad Erlangga Kurniawan (23083010045)
- M.C. Raka Anugerah (23083010070)
- M. Nurhadyatullah Kusharyadi (23083010049)


# Fase Pengerjaan
## Fase 1: Pembuatan Frontend dan Backend Aplikasi
pembuatan Frontend dan juga Backend dari aplikasi dapat dilihat di folder frontend dimana kita membuat index.html sebagai html utama kita dan juga style.css sebagai tempat script css kita dan kita juga akan menggunakan script.js untuk membangun backend kita
disini kita juga menggunakan icon secara global dengan menggunakan google api material symbol dan juga font dari google fonts
![code-html](out/piccod1.png)

## Fase 2 Pembangunan RDS dan server EC2:
setelah kita membuat akun AWS Educate, langkah berikutnya adalah untuk membuat server di EC2, hal tersebut dapat dilihat dari gambar di bawah berikut
![EC2-AWS](out/picfas1.jpeg)
<br />
setelah kita membangun server di EC2, kemudian kita akan melakukan setup untuk membuat databases di Amazon RDS, hal tersebut dapat dilihat di gambar di bawah
![RDS-AWS](out/picfas2.jpeg)

## Fase 3 Koneksi pada Databases:
kemudian setelah databases dan server telah berjalan, kita dapat melanjutkan pada pengetesan koneksi pada python disini kita menggunakan library flask sebagai library utama untuk melakukan koneksi pada databases tersebut. uji script tersebut dapat dilihat dari python script di bawah berikut
![pyscript](out/piccod2.png)

<br />
output dari kodingan tersebut adalah kita tersambung dengan server tersebut
![Out3](out/pic3.jpeg)
<br />
dan ketika kita menyambungkan pada server local tersebut, maka kita akan mendapatkan hasil web yang sebelumnya telah kita bangun
![Out1](out/pic1.png)

## Fase 4 Cloudwatch Monitoring:
setelah aplikasi kita telah berjalan dengan sukses tentu kita dapat melakukan monitoring dengan menggunakan Amazon CloudWatch. hasil monitoring dari Cloudwatch dapat dilihat sebagai berikut

#### untuk penggunaan secara keseluruhan
![Out1](out/cwatch1.png)
#### untuk penggunaan Cpu
![Out1](out/cwatch1.png)

## Fase 5 Presentasi
setelah itu kita melakukan presentasi secara daring dan juga melakukan dokumentasi
<div align="center">
    <a href="https://youtu.be/Vhb71u5W2qw?si=n_8cLdYeijtEh1lb">Link Presentasi</a>
</div>


## Hasil utama
hasil dari running Aplikasi berikut adalah sebagai berikut:
### Laman Utama
![Out1](out/pic1.png)
### Hasil ketika melakukan Searching pada kota Surabaya:
![Out2](out/pic2.png)
### Hasil running script python:
![Out3](out/pic3.jpeg)
