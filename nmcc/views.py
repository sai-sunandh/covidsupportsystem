from django.shortcuts import render
from django.http import HttpResponse
from .models import reg
# Create your views here.
def hi(request):
	return render(request,'nmcc/home.html',{})


def register(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		mobile=request.POST['mob']
		dist=request.POST['dist']
		data=vaccine(dist)
		ob=reg(NAME=name,EMAIL=email,MOBILE=mobile,DISTRICT=dist)
		ob.save()
		return render(request,'nmcc/vaccine.html',{'data':data,'dist':dist.upper()})
	return render(request,'nmcc/register.html',{})

def owner(request):
	return render(request,'nmcc/owner.html',{})

def home(request):
	return render(request,'nmcc/home.html',{})
	
def hospitals(request):

	return render(request,'nmcc/hospitals.html',{})

def vaccine(dist):
	if dist.upper()=="EAST GODAVARI" or dist.upper()=="EASTGODAVARI":
		data=["Konaseema Institute Of Medical Science AMALAPURAM Andhra Pradesh East Godavari",
				"Raju Neuro And Multispeciality Hospitals P Ltd RAJAHMUNDRY Andhra Pradesh East Godavari",
			"Gsl Trust Cancer Hospital And Research Centre RAJAHMUNDRY Andhra Pradesh East Godavari",
				"Haritha Hospitals KAKINADA Andhra Pradesh East Godavari",
				"Sai Sudha Hospital KAKINADA Andhra Pradesh East Godavari",
				"UNIVERSAL HOSPITALS 29-14-29 Andhra Pradesh East Godavari",
				"HOPE INTERNATIONAL HOSPITAL A UNIT OF PALAPARTHI SUPER SPECIALITY HOSPITALS PRIVATE LIMITED 3-119 Andhra Pradesh East Godavari",
				"LAXMI HOSPITAL 3-16-207 Andhra Pradesh East Godavari",
				"Raghava 24 Hours Hospital D.NO.11-11-3/1 RAMARAOPETA NOOKALAMMA TEMPLE STREET KAKINADA-533004 Andhra Pradesh East Godavari",
				"Aravindam Orthopdeics And Physiotherapy Centre RAJAHMUNDRY Andhra Pradesh East Godavari",
				"Goutami Eye Institute 1 R V Nagar Korukonda Road,Rajahmundry 533105 Andhra Pradesh East Godavari",
				"Sudha Urology And Andrology Hospital KAKINADA Andhra Pradesh East Godavari",
				"Sri Kiran Institute Of Ophthalmology Penumarthi Road, Near Atchampeta JunctionKakinada Andhra Pradesh East Godavari",
				"Sri Bikkina Nursing Home MAIN ROAD MANDAPETA-533308 E.G.Dt  A.P Andhra Pradesh East Godavari",
				"Royal Hospital 20-23-4 Aryapuram Behind Nagadevi Theatre Rajahmundry. 533104 Andhra Pradesh East Godavari",
				"Sri Lalitha Hospitals Insitute Of Laparoscopic Surgery And Training D.NO:13-3-2/3 OPP ANAND BHARATHI,CINEMA ROAD Andhra Pradesh East Godavari",
				"S.A.I. Hospitals D.NO: 2-11-97 ARYAPURAM MIDDLE STREET Andhra Pradesh East Godavari",
				"Safe Emergency Hospital 2-2-7 USHAPRIYA COMPLEX BHANUGUDI JUNCTION KAKINADA Andhra Pradesh East Godavari",
				"KIMS (Krishna Institute of Medical Sciences Ltd) Rajahmundry KATARIGARDENS, SEELAM NUKARAJU COMPLEX ROAD Rajahmundry Andhra Pradesh East Godavari",
				"KAR HOSPITAL ORTHPAEDICS AND MULTI SPECIALITY 1-526 Andhra Pradesh East Godavari",
				"NARAYANA REDDY EYE HOSPITAL 1-426 Andhra Pradesh East Godavari",
				"DR BRM CAREWELL HOSPITAL 2-6-32/3 Andhra Pradesh East Godavari",
				"PANDURANGA PRAJA VYDYASALA 2-17-29 Andhra Pradesh East Godavari",
				"SRI VIJAYA MULTI SPECIALTY HOSPITAL 8-10-30/1 Andhra Pradesh East Godavari",
				"ASCENT HOSPITALS A UNIT OF ASCENT MEDI EXCELLENCE PRIVATE LIMITED 78-16-7 Andhra Pradesh East Godavari",
				"SIDDARATHA NURSING HOME AND POLYCLINIC 29-14-96 Andhra Pradesh East Godavari",
				"SRI AKSHARA HOSPITALS 07-09-2004 Andhra Pradesh East Godavari",
				"NEPHROPLUS (GGH KAKINADA) GOVERNMENT GENRAL HOSPITAL GGH ROAD RR ROAD KAKINADA-01 EAST GODAVARI DISTRICT  AP PIN 533001 Andhra Pradesh East Godavari",
				"Sreelatha Hospital 12-21-4Aryapuram Andhra Pradesh East Godavari",
				"Chakradhar Hospitals D.NO.85-6-24/1 R.T.C.COMPLEX ROAD  V.L.PURAM JN RAJAHMUNDRY Andhra Pradesh East Godavari",
				"Life Line Emergency Neuro and Trauma Hospital 70-1-31/3 RAMANAYYAPETA N.F.C.L.ROAD KAKINADA Andhra Pradesh East Godavari",
				"Siddhartha Hospital 34-1-20 TEMPLE STREET KAKINADA-533001 Andhra Pradesh East Godavari",
				"Dr.KVR HOSPITAL 6-18 MAIN ROAD RAYAVARAM EAST GODAVARI DIST PIN: 533 346. Andhra Pradesh East Godavari",
				"TRUST HOSPITAL A UNIT OF SARVOTTAM HEALTH CARE PVT LTD 3-29 GAIGOLUPADU ROADPAVARAM JUNCTION NEAR NTR STATUE533005 Andhra Pradesh East Godavari",
				"ARUNA HOSPITAL 8-19-4/5 Andhra Pradesh East Godavari",
				"CHANAKYA HOSPITAL 6-256 Andhra Pradesh East Godavari",
				"RAMYA HOSPITALS 9-11-130 Andhra Pradesh East Godavari",
				"INODAYA HOSPITALS A UNIT OF GODAVARTHY NARASIMHA MURTHY HEALTHCARE PVT LTD 70-7-7/11 Andhra Pradesh East Godavari",
				"YASHVEDHHEALTHCARESERVICES 69-18-2/1 Andhra Pradesh East Godavari",
				"SRINIDHI HOSPITALS VN NURSING HOME 3-2-117/E Andhra Pradesh East Godavari",
				"TAPANI HOSPITAL 11-11-2004 Andhra Pradesh East Godavari",
				"7 STAR SUPER SPECIALITY HOSPITAL 20-01-61, Andhra Pradesh East Godavari",
				"Swatantra HospitalsM.S Pvt Ltd RAJAHMUNDRY Andhra Pradesh East Godavari",
				"Gsl Medical College And Gsl General Hospital RAJAHMUNDRY Andhra Pradesh East Godavari",
				"Samudra Healthcare Enterprises Ltd Apollo Hospital Kakinada KAKINADA Andhra Pradesh East Godavari",
				"KAMALAKAR HOSPITAL D.NO.75-7-20 Andhra Pradesh East Godavari",
				"SANJIVI INSTITUTE OF ORTHOPAEDICS and SUPERSPECIALITIES PVT.LTD 11-11-1  RAMARAOPETA  TWOTOWN CENTER, behind nookalamma temple, 533004 Andhra Pradesh East Godavari",
				"RAJAHMUNDRY ORTHOPEDIC HOSPITAL 75-1-18 PRAKASH NAGARRAJAHMUNDRY EastGodavari Andhra Pradesh East Godavari",
				"PULSE EMERGENCY HOSPITAL 1-15-3/1 Andhra Pradesh East Godavari",
				"SRI RAVI HOSPITALS D.NO 86-05-05 TILAK ROAD Andhra Pradesh East Godavari",
				"VIJAY HOSPITAL d.no-46-15-13 DANVAIPETA Andhra Pradesh East Godavari",
				"AKIRA EYE HOSPITAL 12-20-18 Andhra Pradesh East Godavari",
				"SURAREDDY NURSING HOME 1-42-59/4 Andhra Pradesh East Godavari",
				"SARADHI HOSPITALS 74-1318 Andhra Pradesh East Godavari",
				"SUNRISE HOSPITALS A UNIT OF SANKHYA AND SRINIDHI HOSPITALS PVT LTD 2-27-15 Andhra Pradesh East Godavari",
				"GANDHI HOSPITAL 11-02-2012 Andhra Pradesh East Godavari",
				"GANDHI HOSPITALS 76-6-4 Andhra Pradesh East Godavari",
				"RS NEURO AND MULTISPECIALITY HOSPITAL 46-21-10 Andhra Pradesh East Godavari",
				"NARAYANAREDDY HOSPITALS 34-16-51 Andhra Pradesh East Godavari",
				"KUSUMA HOSPITALS 7-7-5/4 Andhra Pradesh East Godavari",
				"DR AGARWALS HEALTH CARE LIMITED 54-9-8 Andhra Pradesh East Godavari",
				"ANNAPURNA HOSPITALS EMERGENCY CARE CENTRE 17-09-2014 Andhra Pradesh East Godavari",
				"REVATHI HOSPITAL 87-1-17 Andhra Pradesh East Godavari",
				"BESTHOSPITAL 10-5-27/1 Andhra Pradesh East Godavari",
				"SRI SANTHI ENT HOSPITAL 75-7-37/1 Andhra Pradesh East Godavari",
				]
		return data
	elif(dist=="WEST GODAVARI" or dist=="WESTGODAVARI"):
		data=[
		"Sudha Hospital Tanuku 21-1-4, OPP COOPERATIVE STORES Andhra Pradesh West Godavari",
"Good Samaritan Cancer and General Hospital VANGAYAGUDEM, ELURU - 534 001 Andhra Pradesh West Godavari",
"Mother Vannini Hospital KADAKATALA,TADEPALLIGUDEM Andhra Pradesh West Godavari"
"Srisaihospital DNO12-69-5SILVERJUBILEEROAD OPP SNVT JR COLLEGETANUKU,WESTGODAVARI-DIST Andhra Pradesh West Godavari",
"Dr G R Reddy Eye Care Center 1-41-1 Andhra Pradesh West Godavari",
"PRABHA HOSPITAL 24B-6-16/1 Andhra Pradesh West Godavari",
"Jnanananda Ophthalmic Institute 03-06-1934 Andhra Pradesh West Godavari",
"CHAITRA HOSPITAL 24A-4-4 Andhra Pradesh West Godavari",
"ANDHRA HOSPITALS ELURU PVT LTD 23A-8-8 Andhra Pradesh West Godavari",
"SAI SPURTHI MULTISPECIALITY HOSPITAL 9-2-30/1 Andhra Pradesh West Godavari",
"SAISWETHA SUPER SPECIALITY HOSPITAL A UNIT OF SAISWETHA HOSPITAL PRIVATE LIMITED 16-18-2 Andhra Pradesh West Godavari",
"Sri Lakshmi Hospitals 3-6-36 TOWNRAILWAY STATION ROADBhimavaram Andhra Pradesh West Godavari", 
"Varma Hospitals Door. No.:1-7-4/2-1 Near AddavanthenaSuryanarayanapuram J.P. RoadBhimavaram. 534 202 Andhra Pradesh West Godavari",
"APPLE HOSPITAL A UNIT OF TANUKU HOSPITAL 21-4-22, NEAR RAILWAY STATION TANUKU WESTGODAVARI Andhra Pradesh West Godavari",
"CHIRANJEEVI HOSPITALS ORTHO AND MULTI SPEICILITY NEAR NEW BUS STAND Andhra Pradesh West Godavari",
"Alluri Sitarama Raju Academy Of Medical Sciences Asram Hospital ELURUWEST GODAVARI DIST Andhra Pradesh West Godavari",
"UVSM Eye Hospital 27-16-5/1 Andhra Pradesh West Godavari",
"BHUVANESWARI HOSPITAL 23B/2/12 Andhra Pradesh West Godavari",
"KASI EYE HOSPITAL 27-8-12/4 Andhra Pradesh West Godavari",
"PRANAVI NURSING HOME 4-17-796 Andhra Pradesh West Godavari",
"AVINASH ORTHO TRAUMA AND CRITICAL CARE HOSPITAL 2-22-20 Andhra Pradesh West Godavari",
"SRI VENKATESWARA INSTITUTE OF RESEARCH AND REHABILITATION FOR THE DISABLED S-41 Andhra Pradesh West Godavari",
"VADLAMUDI HOSPITALS 1-11-146 Andhra Pradesh West Godavari",
"SANKARA NETRA CHIKITSALAYA 23A-6-6 Andhra Pradesh West Godavari",
"SMT RAJESWARI RAMAKRISHNAN LIONS EYE HOSPITAL 12-16-40 Andhra Pradesh West Godavari",
"MURALI KRISHNA MULTI SPECIALITY AND EMERGENCY HOSPITAL 25-10-1934 Andhra Pradesh West Godavari",
"JANAKI HOSPITAL 1-87-58 Andhra Pradesh West Godavari",
"RADHAKRISHNA NETHRYALAYA 27-2-125/A Andhra Pradesh West Godavari",
"SRI SURYA NURSING HOME 12-2-31/2 Andhra Pradesh West Godavari",
"SESHA GIRI HOSPITALS A UNIT OF SRI RATNA NURSING HOME 9-11-19/A Andhra Pradesh West Godavari",
"NEPHROPLUS (DH ELURU) ELURU Andhra Pradesh West Godavari",
"SRI SURYA HOSPITAL 9-1-5/2 Andhra Pradesh West Godavari",
"SRI SAI SPURTHI HOSPITALS 9-190 Andhra Pradesh West Godavari",

		]


		return data
	

