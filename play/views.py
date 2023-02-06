from django.shortcuts import render,redirect,get_object_or_404
from .models import PlayMenu
from django.core import serializers
import random
import json
from django.http import JsonResponse


def explore_menu(request):
    
    menu_list = PlayMenu.objects.all()
    
    total_menu_num = len(PlayMenu.objects.all())
    random_menu_pk = random.randint(1,total_menu_num)
    random_menu_queryset = PlayMenu.objects.filter(id=random_menu_pk).values()
    random_menu = random_menu_queryset[0]
    
    top4_menu = PlayMenu.objects.order_by('-click_count')[0:4]
    
    return render(request, "play/explore_menu.html",{'menu_list':menu_list,'random_menu':random_menu,'top4_menu':top4_menu})


def click_count(request,pk):
    menu = get_object_or_404(PlayMenu,pk=pk)
    menu.click_count = menu.click_count + 1
    
    menu.save()
    
    return redirect("play:explore_menu")