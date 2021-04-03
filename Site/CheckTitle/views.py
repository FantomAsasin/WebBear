from django.shortcuts import render


def Home(reqest):
	return render(reqest,'CheckTitle/Content.html')

def Chapters(reqest):
	return render(reqest,'CheckTitle/Chapters.html')

def Check_Content(reqest):
	return render(reqest,'CheckTitle/Check_Content.html')

def Page_Title(reqest):
	return render(reqest,'CheckTitle/Page_Title.html')