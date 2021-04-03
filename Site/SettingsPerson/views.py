from django.shortcuts import render

def Auto(reqest):
	return render(reqest,'SettingsPerson/Auto.html')

def Registr(reqest):
	return render(reqest,'SettingsPerson/Registr.html')

def Settings(reqest):
	return render(reqest,'SettingsPerson/Settings.html')