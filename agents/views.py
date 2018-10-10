# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse
from .models import Agent
from django.shortcuts import render, redirect
from agents.agent_addForm import  AgentForm
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


def agentActions(request):
    agents = Agent.objects.all()
    return render(request, 'agents/agent_actions.html', {'agents': agents,})



def agentAdd(request):
    if request.method=='POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()

        return  redirect('agents/')
    else:
        form = AgentForm()
    return render(request, 'agents/agent_addForm.html', {'form':form})


def agentDetails(request, id):
    agents = Agent.objects.filter(id=id)
    print(agents)
    return  render(request,'agents/agent_details.html', {'agents':agents,})


def agentDelete(request, id):
    agent = Agent.objects.filter(id=id)
    agent.delete()
    return HttpResponse(1)


def agentEdit(request, id):
    agent = Agent.objects.filter(id=id)
    return HttpResponse(agent)

def getAgentName(request, comunidad, ip):
    name = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.5.0'))
    return HttpResponse(name)



def getStateAgent(request,ip):
    response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
    return  HttpResponse(response)


def getOperativeSystem(request,comunidad,ip):
    so = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.1.0')
    return HttpResponse(so)


def getInterfacesNet(request, comunidad,ip):
    noInterface = int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.2.1.0'))
    return  HttpResponse(noInterface)


def getTimeActivity(request, comunidad, ip):
    time = int(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.3.0'))
    res = getCompleteTime(time)
    return HttpResponse(res)


def getCompleteTime(nums):
    num = int(nums)/100
    hor = (int(num / 3600))
    minu = int((num - (hor * 3600)) / 60)
    seg = num - ((hor * 3600) + (minu * 60))
    res= str(hor) + "h " + str(minu) + "m " + str(seg) + "s"
    return res

def getAgentLocation(request, comunidad, ip):
    location = str(consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.6.0'))
    return HttpResponse(location)

def getAgentContact(request, comunidad, ip):
    contact = consultaSNMP(comunidad, ip, '1.3.6.1.2.1.1.4.0')
    return HttpResponse(contact)


""" for agent in agents:
        ip = agent.ip_address
        comunidad = agent.community_name
        numInterfaces = getInterfacesNet(comunidad, ip)
        list_interfaces.append(numInterfaces)
        print(list_interfaces)
    print("********************HOla")
    print(list_interfaces[0])
    print(list_interfaces[1])
    
    
          if request.method == 'POST':
              form = AgentForm(request.POST)
              if form.is_valid():
                 form.save()
              return render(request, 'agents/agent_addForm.html', {'form': form})
        else:
         form = AgentForm()
         return render(request, 'agents/agent_addForm.html', {'form':form})
    
    
    
    """