from django import forms
from .models import Mobile

class MobileForm(forms.ModelForm):
	class Meta:
		model =Mobile
		fields =['Model_Name','Image','Brand','Price','Descrption']