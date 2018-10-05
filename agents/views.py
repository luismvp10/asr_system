# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse
from .models import Agent
from django.shortcuts import render, redirect
from agents.agent_addForm import *
from agents.getSNMP import consultaSNMP
import os
import time
import time
import rrdtool
from pysnmp.hlapi import *

# Create your views here.

def agents(request):
    agents = Agent.objects.all()
    agentAmount= len(Agent.objects.all())
    list_interfaces = []



    #agent_lits = "- ".join([str(agent) for agent in agents])
    return render(request, 'agents/agent_list.html', {'agents':agents, 'agentAmount':agentAmount,})


def agent_add(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent:home')
        else:
            form = AgentForm()
        return render(request, 'agents/agent_add.html',{'form':form})



def get_AgentName(comunidad,ip):
	name = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.5.0')
	return name

def getInterfacesNet(comunidad,ip):
    noInterface = int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.1.0'))
    return  noInterface



""" for agent in agents:
        ip = agent.ip_address
        comunidad = agent.community_name
        numInterfaces = getInterfacesNet(comunidad, ip)
        list_interfaces.append(numInterfaces)
        print(list_interfaces)
    print("********************HOla")
    print(list_interfaces[0])
    print(list_interfaces[1])"""