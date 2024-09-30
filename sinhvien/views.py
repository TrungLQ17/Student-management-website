from django.shortcuts import render
from .models import HeDaiHoc, VB2, SinhVien

def home(request):
    context = {
        'he_daihocs': HeDaiHoc.objects.all(),
        'vb2s': VB2.objects.all()
    }
    return render(request, 'sinhvien/home.html', context)

def sinhvien_list(request):
    he_daihocs = HeDaiHoc.objects.all()
    vb2s = VB2.objects.all()
    return render(request, 'sinhvien/sinhvien_list.html', {'he_daihocs': he_daihocs, 'vb2s': vb2s})

def sinhvien_totnghiep(request):
    he_daihocs = [sv for sv in HeDaiHoc.objects.all() if sv.check_dk()]
    vb2s = [sv for sv in VB2.objects.all() if sv.check_dk()]
    return render(request, 'sinhvien/sinhvien_totnghiep.html', {'he_daihocs': he_daihocs, 'vb2s': vb2s})

def sinhvien_khong_totnghiep(request):
    he_daihocs = [sv for sv in HeDaiHoc.objects.all() if not sv.check_dk()]
    vb2s = [sv for sv in VB2.objects.all() if not sv.check_dk()]
    return render(request, 'sinhvien/sinhvien_khong_totnghiep.html', {'he_daihocs': he_daihocs, 'vb2s': vb2s})

def sinhvien_max_dtb(request):
    sinhvien1 = max(HeDaiHoc.objects.all(), key=lambda sv: sv.diem_tb, default=None)
    sinhvien2 = max(VB2.objects.all(), key=lambda sv: sv.diem_tb, default=None)
    if sinhvien1 is None and sinhvien2 is None:
        sinhvien = None
    elif sinhvien1 is None:
        sinhvien = sinhvien2
    elif sinhvien2 is None:
        sinhvien = sinhvien1
    else:
        sinhvien = sinhvien1 if sinhvien1.diem_tb > sinhvien2.diem_tb else sinhvien2
    return render(request, 'sinhvien/sinhvien_max_dtb.html', {'sinhvien': sinhvien})

def sinhvien_min_dtb(request):
    sinhvien1 = min(HeDaiHoc.objects.all(), key=lambda sv: sv.diem_tb, default=None)
    sinhvien2 = min(VB2.objects.all(), key=lambda sv: sv.diem_tb, default=None)
    if sinhvien1 is None and sinhvien2 is None:
        sinhvien = None
    elif sinhvien1 is None:
        sinhvien = sinhvien2
    elif sinhvien2 is None:
        sinhvien = sinhvien1
    else:
        sinhvien = sinhvien1 if sinhvien1.diem_tb < sinhvien2.diem_tb else sinhvien2
    return render(request, 'sinhvien/sinhvien_min_dtb.html', {'sinhvien': sinhvien})

def tim_kiem_sv(request):
    ma_sv = request.GET.get('ma_sv')
    sinh_viens = []
    
    if ma_sv:
        sinh_viens += HeDaiHoc.objects.filter(ma_sv=ma_sv)
        sinh_viens += VB2.objects.filter(ma_sv=ma_sv)

    return render(request, 'sinhvien/tim_kiem_sv.html', {'sinh_viens': sinh_viens, 'ma_sv': ma_sv})