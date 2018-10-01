# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse
from .models import Agent
from django.shortcuts import render

# Create your views here.

def agents(request):
    agents = Agent.objects.all()
    #agent_lits = "- ".join([str(agent) for agent in agents])
    return render(request, 'agents/agent_list.html', {'agents':agents})