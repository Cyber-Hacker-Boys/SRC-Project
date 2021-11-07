from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


class IPCreatorForm(forms.Form):
    srcIP = forms.GenericIPAddressField(label='Source IP')
    srcPort = forms.IntegerField(label='Source Port')
    destIP = forms.GenericIPAddressField(label='Destination IP')
    destPort = forms.IntegerField(label='Destination Port')
    seqN = forms.IntegerField(label='Sequence Number')
    ackN = forms.IntegerField(label='Acknowledgement Number')
    ip_id = forms.IntegerField(label='IP ID')
    ip_flags = forms.IntegerField(label='IP Flags')
    content = forms.CharField(label='Content', widget=forms.Textarea)
