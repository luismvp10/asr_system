# -*- coding: utf-8 -*-
from django import forms
from agents.models import Agent


class AgentForm(forms.ModelForm):


    class Meta:
        model = Agent

        fields = {
            'host_name',
            'community_name',
            'ip_address',
            'snmp_version',
            'snmp_port',
         }
        labels = {
            'host_name': 'Hostname',
            'community_name': 'Comunidad',
            'ip_address': 'IP',
            'snmp_version': 'Versión SNMP',
            'snmp_port': 'Puerto',

        }
        widgets = {
            'host_name' : forms.TextInput(attrs={'class':'form-control'}),
            'community_name':forms.TextInput(attrs={'class':'form-control'}),
            'ip_address': forms.TextInput(attrs={'class':'form-control'}),
            'snmp_version':forms.TextInput(attrs={'class':'form-control'}),
            'snmp_port': forms.TextInput(attrs={'class':'form-control'}),
        }
