#
# This program is find IC in TI web
# when this IC can purchase will pop up 
# purchase web
#
#
# install: pywebview
#
#  $pip3 install pywebview
#


import requests
import webview

#from datetime import date,datetime,time
import time

icNameA = ['TPS7A5301WQRTKRQ1', 'TPS7A5301QRGRRQ1']
DELAY_TIME = 10 # sec


while True:
	now = time.localtime(time.time())
	for i in range(len(icNameA)):
		
		nameIP = icNameA[i]
		web = 'https://www.ti.com/store/ti/en/p/product/?p=' + nameIP
		r = requests.get(web)

		print(time.strftime("============== time : %H:%M:%S =================",now))
		if r.status_code == requests.codes.ok:
			if r.text.find('"ACTIVE">ACTIVE'):  #Add to cart</button>'):
				
				print(" Found: {:}".format(nameIP))
				
				pass_window = webview.create_window('IC Finder', web)
				#master_window = webview.create_window('Window #1', html='<h1>First window</h1>')
				webview.start()
				#print(r.text)
		else:
			
			print(" Not found: {:}".format(nameIP))
			print("===========================\n")
		
	time.sleep(DELAY_TIME)

 
