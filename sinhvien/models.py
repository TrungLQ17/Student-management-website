from django.db import models

class SinhVien(models.Model):
    ma_sv = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=100)
    dia_chi = models.CharField(max_length=100, null=True, blank=True)
    tong_tc = models.IntegerField(default=0)
    diem_tb = models.FloatField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return f'MSSV: {self.ma_sv} - Họ và tên: {self.ho_ten}'
    
    
class HeDaiHoc(SinhVien):
    ten_lv = models.CharField(max_length=100, blank=True)
    diem_lv = models.FloatField(default=0)

    def check_dk(self):
        return self.diem_tb >= 5.0 and self.diem_lv >= 5.0 and self.tong_tc >= 120

class VB2(SinhVien):
    diem_tot_nghiep = models.FloatField(default=0)

    def check_dk(self):
        return self.diem_tb >= 5.0 and self.diem_tot_nghiep >= 5.0 and self.tong_tc >= 84

class TotNghiep(models.Model):
    nam_totnghiep = models.IntegerField()
    dot_totnghiep = models.IntegerField()
    he_daihoc = models.ManyToManyField(HeDaiHoc, blank=True)
    vb2 = models.ManyToManyField(VB2, blank=True)
