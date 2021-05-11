from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import requests, json
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
# import mysql
import MySQLdb

# Create your views here.
def under_maintenance(request):
	if request.method == "POST":
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		row = Login.objects.filter(username = username)
		print(row)
		# cursor = connection.cursor()
		# cursor.execute('SELECT count(*) FROM login where username= %s', [username])
		# row = cursor.fetchone()
		# #print(row)
		if len(row) >= 1:
			return render(request,'dashboard.html')
		else:
			print(row)
	return render(request,'project_index.html')

def master_trs(request):
	return render(request,'project_index_old.html')

def ajaxcall_master_trs(request):
	if request.method == "POST":
		searchStr = request.POST.get("searchStr", "")
		print(searchStr)
		mydb = MySQLdb.connect(
			host="103.145.50.139",
			user="techinsig_midi",
			password="cn3qdUp3Q*P!",
			database="techinsig_midi"
			)
		cursor = mydb.cursor()
		
		#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
		#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
		#qry ='SELECT * FROM trs_master WHERE hsn_code LIKE "'+searchStr+'%" order by chapter_name'
		searc=searchStr
		#print(searc)
		qry ='SELECT * FROM trs_master WHERE hsn_code LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` DESC'
		#print(qry)
		#qry ='SELECT * FROM trs_master WHERE hsn_code="'+searchStr+'" order by chapter_name'
		#cursor.execute('SELECT * FROM `trs_master` WHERE `hsn_code` = %s', [searchStr] )
		cursor.execute(qry)
		row = cursor.fetchall()
		# row = TrsMaster.objects.filter(hsn_code__contains = searc)
		print(row)
		for i in row:
			print(i)

		data = {
			'hsn_code':row,
		}
	return JsonResponse(data)
	#return HttpResponse(json.dumps({'message' : row},ensure_ascii=False), content_type='application/json')

def ajaxcall_append(request):
	searchStr = request.POST.get("autoid", "")
	#print(searchStr)
	mydb = MySQLdb.connect(
		host="103.145.50.139",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	searc=searchStr
	print(searc)
	qry ='SELECT * FROM trs_master WHERE hsn_code LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` DESC'
	print(qry)
	cursor.execute(qry)
	row = cursor.fetchall()
	data = {
		'hsn_code':row,
	}
	return JsonResponse(data)

def ajaxcall_appendprs(request):
	searchStr = request.POST.get("hsncodes", "")
	#print("testttttttttttt")
	#print(searchStr)
	mydb = MySQLdb.connect(
		host="103.145.50.139",
		user="techinsig_midi",
		password="cn3qdUp3Q*P!",
		database="techinsig_midi"
		)
	cursor = mydb.cursor()
	searc=(searchStr)
	#print(searc)
	#qry1 ='SELECT * FROM psr_master WHERE fromval LIKE '+searc
	qry1 ='SELECT * FROM psr_master WHERE '+searc+' > fromval AND '+searc+' <= toval'
	print(qry1)
	cursor.execute(qry1)
	row = cursor.fetchall()
	data = {
		'hsn_codess':row,
	}
	# mydb = mysql.connector.connect(
	# 	host="103.145.50.139",
	# 	user="techinsig_midi",
	# 	password="cn3qdUp3Q*P!",
	# 	database="techinsig_midi"
	# 	)
	#cursor = mydb.cursor()
	#cursor = connection.cursor()
	#select... afield like '%%%s%%' and secondfield = '%s'..." % ( var1, var2 )
	#cursor.execute("SELECT * FROM trs_master where  hsn_code like '%%%s%%'" % ( searchStr ))
	#searc=searchStr
	#print(searc)
	# qry ='SELECT * FROM trs_master WHERE hsn_code LIKE '+searc+'ORDER BY `trs_master`.`hsn_code` DESC'
	# print(qry)
	# cursor.execute(qry)
	# row = cursor.fetchall()
	# data = {
	# 	'hsn_code':row,
	# }
	return JsonResponse(data)
