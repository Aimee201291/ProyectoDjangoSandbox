#Esta es la clase del formulario que vamos a usar en nuestra vista
from django import forms  

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota  #Indicamos de qué modelo vamos a crear este formulario

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]
		labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
		widgets = { #Son los que se van a pintar en forma de etiquetas html
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
}