from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsPost
from django.db import models
from django.core.paginator import Paginator

def news_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    search_query = request.GET.get('q', '').strip()
    all_news = NewsPost.objects.all().order_by('-created_at')
    paginator = Paginator(all_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if search_query:
        latest_news = NewsPost.objects.filter(
            models.Q(title__icontains=search_query) | models.Q(content__icontains=search_query)
        ).order_by('-created_at')[:3]
    else:
        latest_news = NewsPost.objects.all().order_by('-created_at')[:3]
    return render(request, 'news/news_list.html', {
        'news': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'latest_news': latest_news,
        'search_query': search_query,
    })

def news_detail(request, pk):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    post = get_object_or_404(NewsPost, pk=pk)
    search_query = request.GET.get('q', '').strip()
    if search_query:
        latest_news = NewsPost.objects.filter(
            models.Q(title__icontains=search_query) | models.Q(content__icontains=search_query)
        ).order_by('-created_at')[:3]
    else:
        latest_news = NewsPost.objects.all().order_by('-created_at')[:3]
    return render(request, 'news/news_detail.html', {'post': post, 'latest_news': latest_news, 'search_query': search_query})

