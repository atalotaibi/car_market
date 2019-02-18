from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully created')
			return redirect('car-list')
	context = {
		"car": form,
		}
	return render(request, 'car_create.html', context)


def car_update(request, car_id):
	car_obj = Car.objects.get(id=car_id)
	car = CarForm(instance=car_obj)
	if request.method == "POST":
		car = CarForm(request.POST, instance=car_obj)
		if car.is_valid():
			car.save()
			messages.success(request, 'Successfully updated.')
			return redirect('car-list')
	context = {
        "car_obj": car_obj,
        "car": car,
    }
	#Complete Me
	return render(request, 'car_update.html', context)


def car_delete(request, car_id):
	car_obj = Car.objects.get(id=car_id)
	car_obj.delete()
	#Complete Me
	return redirect('car-list')