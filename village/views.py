from django.shortcuts import render, redirect, get_object_or_404
from .models import BloodDonor, MedicalService, TransportTrip, CraftService

# الصفحة الرئيسية - بتجيب داتا كل الأقسام وتعرضها
def index(request):
    donors = BloodDonor.objects.all()
    medical_services = MedicalService.objects.all()
    trips = TransportTrip.objects.all()
    crafts = CraftService.objects.all()
    
    context = {
        'donors': donors,
        'medical_services': medical_services,
        'trips': trips,
        'crafts': crafts,
    }
    return render(request, 'index.html', context)

# دالة الاستقبال العامة للإضافات من برة
def add_service_from_outside(request):
    if request.method == 'POST':
        section_type = request.POST.get('section_type')
        
        if section_type == 'blood':
            BloodDonor.objects.create(
                name=request.POST.get('name'),
                blood_group=request.POST.get('blood_group'),
                phone=request.POST.get('phone'),
                area=request.POST.get('area')
            )
        elif section_type == 'medical':
            MedicalService.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                phone=request.POST.get('phone')
            )
        elif section_type == 'transport':
            TransportTrip.objects.create(
                driver_name=request.POST.get('driver_name'),
                destination=request.POST.get('destination'),
                time=request.POST.get('time'),
                phone=request.POST.get('phone')
            )
        elif section_type == 'craft':
            CraftService.objects.create(
                worker_name=request.POST.get('worker_name'),
                craft_type=request.POST.get('craft_type'),
                phone=request.POST.get('phone'),
                area=request.POST.get('area')
            )
            
    return redirect('index')

# دالات الحذف أو الإخفاء بعد إتمام الخدمة
def complete_blood(request, pk):
    get_object_or_404(BloodDonor, pk=pk).delete()
    return redirect('index')

def complete_medical(request, pk):
    get_object_or_404(MedicalService, pk=pk).delete()
    return redirect('index')

def complete_transport(request, pk):
    get_object_or_404(TransportTrip, pk=pk).delete()
    return redirect('index')

def complete_craft(request, pk):
    get_object_or_404(CraftService, pk=pk).delete()
    return redirect('index')