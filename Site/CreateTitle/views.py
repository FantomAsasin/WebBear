from django.shortcuts import render

def UPload_content(reqest):
	return render(reqest,'CreateTitle/UPload_content.html')

def CreateTitle(reqest):
	return render(reqest,'CreateTitle/CreateTitle.html')

def CreateChapters(reqest):
	return render(reqest,'CreateTitle/CreateChapters.html')
