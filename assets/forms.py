from django import forms


class DoctorForm(forms.Form):
    jina_la_kwanza = forms.CharField(max_length=100, label = 'Jina la mgonjwa')
    jina_la_pili = forms.CharField(max_length=100, label = 'Jina la ukoo')
    umri = forms.IntegerField(label = 'Miaka ya mgonjwa')
    anwani = forms.CharField(max_length=100, label = 'Anwani ya mgonjwa')
    Uchunguzi = forms.CharField(widget=forms.Textarea, label='All diagnosis with proposed lab tests')