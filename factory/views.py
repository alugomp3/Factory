from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.http import JsonResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

import time
import datetime
import json

def index(request):
    return render(request, 'index.html', {'texto': 'Smart House '})
