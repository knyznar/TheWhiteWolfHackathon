from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = ('id_doctor','name','surname','phone','adress','certify','profession','password','email')	
