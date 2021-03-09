# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

# For Microsoft Edge Users
PATH = "C:/msedgedriver.exe"

# For Chrome Users
# PATH = "C:/chromedriver.exe"

# Data Akun
Email = "smith@doe.com" # Wajib Unik
Phone = "08123456969" # Wajib Unik

KTP = "1234567890123919"
Name = "John Doe"
Password = "wordpass"
TglLahir = "01"
BlnLahir = "01"
ThnLahir = "1991"
Kelurahan = "Kelurahan"
Kota = "Jakarta"
TempatLahir = "Jakarta"
Alamat = "Jl. Jakarta No. 1"
Kecamatan = "Kecamatan"
KodePos = "12345"
NamaAhliWaris = "Jane Doe"
TglLahirAhliWaris = "02"
BlnLahirAhliWaris = "02"
ThnLahirAhliWaris = "1992"
 
class TestCaseSingleProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(PATH)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_NewUser_SingleProduct(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") #Link Website
        time.sleep(1) #In Second

        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[3]/div/div/div[2]/a[2]").click() #Login Button
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/input").click() #Email Column
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/input").send_keys(Email) #Email Column
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[2]/input").click() #Password Column
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[2]/input").send_keys(Password) #Password Column
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[2]/button").click() #Submit Button
        time.sleep(1)

        # Go to Home
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a").click()
        time.sleep(2)

        # Go to Super Safe product page
        driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div/div[1]/div/div[5]/a").click() #Super Safe Product Page Button
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[1]/div/div[3]/div[1]/div/div/div/div[7]/a").click() #Klik Plan Ini (Bronze Plan)
        time.sleep(1)

        # # Pilih Rider
        # driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[5]/div/label").click() #Pilih Rider Super Holiday Protection
        # driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[6]/div/label").click() #Pilih Rider SUper Motor Protection

        time.sleep(1)

        driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[2]/div/div/div[2]/div[1]/div/div[3]/ul/li[3]/div/a").click() #Klik Beli Plan
        time.sleep(1)

        # Klik Tombol Keranjang
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/img").click() #Klik Tombol Keranjang
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[5]/div/div[2]/div").click() #Klik Lanjut Beli

        #Pengisi Form Isi Data
        time.sleep(1)
        driver.find_element_by_xpath("(//div[@id='su-base-select']/div/div)[2]").click() #Click Daftar Pengeluaran
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[2]").click() #Select Daftar Pengeluaran (Rp3jt - 6jt)
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[3]/div/div[15]/button").click() #Click Button SUBMIT
        time.sleep(1)

        # Halaman Rincian Tertanggung
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/div/div").click() #Click Status Tertanggung
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li").click() #Select Tertanggung (Diri Sendiri)
        driver.find_element_by_xpath("(//div[@id='su-base-select']/div/div)[4]").click() #Click Daftar Pekerjaan
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[16]").click() #Select Pekerjaan (Karyawan Swasta)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/div/div[7]/button").click() #Lanjut Button (Halaman Rincian Tertanggung)
        time.sleep(1)

        # Halaman Ahli Waris
        driver.find_element_by_xpath("(//input[@type='search'])[5]").click() #Click Daftar Ahli Waris
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li[4]").click() #Select Daftar Ahli Waris
        driver.find_element_by_xpath("(//input[@name='name'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='name'])[3]").send_keys(NamaAhliWaris) #Input Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").click()
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").send_keys(TglLahirAhliWaris) #Input Tanggal Lahir Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[12]").send_keys(BlnLahirAhliWaris) #Input Bulan Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[13]").send_keys(ThnLahirAhliWaris) #Input Tahun Ahli Waris
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[5]/div/div[5]/button").click() #Submit Button (Halaman Rincian Tertanggung)

        # Halaman pembayaran
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[2]/div/label").click() #Klik S&K 1
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[3]/div/label").click() #Klik S&K 2
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[4]/div/label").click() #Klik S&K 3
        driver.find_element_by_id("next-step").click() #SUBMIT
        time.sleep(1)

        # Halaman Faspay
        driver.find_element_by_name("CARDNAME").click()
        driver.find_element_by_name("CARDNAME").send_keys("FASPAY")
        driver.find_element_by_name("CARDTYPE").click()
        driver.find_element_by_id("CARDNOSHOWFORMAT").click()
        driver.find_element_by_id("CARDNOSHOWFORMAT").send_keys("4111-1111-1111-1111")
        driver.find_element_by_name("CARDCVC").click()
        driver.find_element_by_name("CARDCVC").send_keys("101")
        driver.find_element_by_id("month").click()
        Select(driver.find_element_by_id("month")).select_by_visible_text("May")
        driver.find_element_by_id("month").click()
        driver.find_element_by_id("year").click()
        Select(driver.find_element_by_id("year")).select_by_visible_text("2021")
        driver.find_element_by_id("year").click()
        driver.find_element_by_name("submit").click()
        time.sleep(2)
        driver.find_element_by_link_text("LIHAT AKUN KAMU").click()
        time.sleep(6)

        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()