import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSlider,
    QDoubleSpinBox, QPushButton, QMessageBox, QRadioButton
)
from PyQt5.QtCore import Qt


class KalkulatorBMI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator BMI & Berat Ideal")
        self.setGeometry(600, 300, 650, 550)
        self.bikin_ui()

    def bikin_ui(self):
        self.setStyleSheet("background-color: #fefefe;")
        layout = QVBoxLayout()

        judul = QLabel("Kalkulator BMI & Berat Ideal")
        judul.setAlignment(Qt.AlignCenter)
        judul.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(judul)

        teks_gender = QLabel("Jenis Kelamin:")
        teks_gender.setStyleSheet("margin-top: 10px; font-weight: bold;")
        layout.addWidget(teks_gender)

        baris_gender = QHBoxLayout()
        self.pil_pria = QRadioButton("Pria")
        self.pil_cewe = QRadioButton("Wanita")
        self.pil_pria.setChecked(True)
        baris_gender.addWidget(self.pil_pria)
        baris_gender.addWidget(self.pil_cewe)
        layout.addLayout(baris_gender)

        layout.addWidget(QLabel("Tinggi Badan (cm):"))
        self.sld_tinggi = QSlider(Qt.Horizontal)
        self.sld_tinggi.setRange(100, 220)
        self.sld_tinggi.setValue(170)

        self.spin_tinggi = QDoubleSpinBox()
        self.spin_tinggi.setRange(100, 220)
        self.spin_tinggi.setValue(170)
        self.spin_tinggi.setSuffix(" cm")

        self.sld_tinggi.valueChanged.connect(self.spin_tinggi.setValue)
        self.spin_tinggi.valueChanged.connect(lambda val: self.sld_tinggi.setValue(int(val)))

        baris_tinggi = QHBoxLayout()
        baris_tinggi.addWidget(self.sld_tinggi)
        baris_tinggi.addWidget(self.spin_tinggi)
        layout.addLayout(baris_tinggi)

        layout.addWidget(QLabel("Berat Badan (kg):"))
        self.sld_berat = QSlider(Qt.Horizontal)
        self.sld_berat.setRange(30, 200)
        self.sld_berat.setValue(60)

        self.spin_berat = QDoubleSpinBox()
        self.spin_berat.setRange(30, 200)
        self.spin_berat.setValue(60)
        self.spin_berat.setSuffix(" kg")

        self.sld_berat.valueChanged.connect(self.spin_berat.setValue)
        self.spin_berat.valueChanged.connect(lambda val: self.sld_berat.setValue(int(val)))

        baris_berat = QHBoxLayout()
        baris_berat.addWidget(self.sld_berat)
        baris_berat.addWidget(self.spin_berat)
        layout.addLayout(baris_berat)

        self.btn_hitung = QPushButton("Hitung Sekarang")
        self.btn_hitung.clicked.connect(self.hitung_bmi)
        self.btn_hitung.setStyleSheet(
            "background-color: #3498db; color: white; font-weight: bold; padding: 10px; border-radius: 5px;"
        )
        layout.addWidget(self.btn_hitung)

        self.lbl_hasil = QLabel("Isi data dulu, baru klik 'Hitung Sekarang' ya 😄")
        self.lbl_hasil.setStyleSheet("font-size: 14px; margin-top: 10px; color: #2d3436;")
        self.lbl_hasil.setWordWrap(True)
        layout.addWidget(self.lbl_hasil)

        self.lbl_nama = QLabel("Muh. Ressa Arsy Ma'rif - F1D022137")
        self.lbl_nama.setAlignment(Qt.AlignCenter)
        self.lbl_nama.setStyleSheet("color: gray; font-size: 11px; margin-top: 15px;")
        layout.addWidget(self.lbl_nama)

        self.setLayout(layout)

    def hitung_bmi(self):
        tinggi = self.spin_tinggi.value()
        berat = self.spin_berat.value()
        tinggi_m = tinggi / 100
        bmi = berat / (tinggi_m ** 2)

        if bmi < 18.5:
            ket = "Kurus"
            saran = "Tipis banget nih... mungkin kurang makan atau kebanyakan scroll TikTok malem-malem? 😅"
        elif 18.5 <= bmi <= 24.9:
            ket = "Normal"
            saran = "Berat badan lo udah oke banget. Pertahankan aja gaya hidup sehat, jangan males gerak! 💪"
        elif 25 <= bmi <= 29.9:
            ket = "Gemuk (Overweight)"
            saran = "Mulai berat dikit nih. Coba atur pola makan & tambahin jalan-jalan sore, biar gak makin rebahan doang 🏃‍♂️"
        elif 30 <= bmi <= 34.9:
            ket = "Obesitas I"
            saran = "Mulai serius nih. Gak apa-apa, pelan-pelan aja ubah gaya hidup. Bisa mulai dari kurangi fast food 🍟"
        elif 35 <= bmi <= 39.9:
            ket = "Obesitas II"
            saran = "Cukup berat, tapi masih bisa dibalikin. Semangat, jangan nyerah. Cari support system juga oke kok 🙌"
        else:
            ket = "Obesitas III"
            saran = "Udah darurat, bro/sis. Sayangi diri sendiri, coba konsul sama dokter. Kamu berhak sehat ❤️"

        if self.pil_pria.isChecked():
            ideal = tinggi - 100
            gender = "Pria"
        else:
            ideal = tinggi - 105
            gender = "Wanita"

        teks = (
            f"Jenis Kelamin: {gender}\n"
            f"Tinggi: {tinggi:.1f} cm\n"
            f"Berat: {berat:.1f} kg\n"
            f"BMI: {bmi:.2f}\n"
            f"Kategori: {ket}\n"
            f"BB Ideal (Broca): {ideal:.1f} kg\n\n"
            f"💡 Saran:\n{saran}"
        )

        self.lbl_hasil.setText(teks)
        QMessageBox.information(self, "Hasil Cek BMI", teks)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jendela = KalkulatorBMI()
    jendela.show()
    sys.exit(app.exec_())
