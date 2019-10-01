import re
from numpy.random import choice
from time import sleep

def gather_dict(vstup=None):
	text = input() if not vstup else vstup
	slovniko=re.compile(r'\s+').split(text)
	slovnik=list(filter(lambda x:x!='',slovniko))
	mega={}
	for i in range(0, len(slovnik),2):
		cz=slovnik[i+1]
		viet=slovnik[i]
		mega[cz]=viet
		mega[viet]=cz
		#print(f'{slovnik[i]} znamena {slovnik[i+1]}')
	return mega
preklad = gather_dict(''' Chanh citron Nho hrozen Bê tele
Lê hruška
Cô teta
   Mèo kočka Hè léto
Bò kráva Cò čáp
Mờ matný
   Hổ tygr Khỉ opice Bẻ zlomit Cỏ tráva Vỏ obal Vẽ malovat Gỗ dřevo
Lễ svátek
Mỡ mastný Ngã spadnout
    Cá ryba Lá list Chó pes Bé malá Bế nést
   Vợ manželka Cụ stařec Ngựa kůň Cọ palma Mẹ matka''')

print(preklad.keys())
body = {}
for k in preklad.keys():
	body[k]=10

def dej_body():
	for k in body.keys():
		body[k]+=1
#print(body.values())
print(body.keys())
def vyber():
	#return choice(['a','b'],1,p= [float(i)/sum([2,3]) for i in[2,3]])[0]
	prst=body.values()
	return choice(list(body.keys()),1 ,p= [float(i)/sum(prst) for i in prst], replace = False)[0]

def hadej(slovo):
	print(f'Preloz {slovo}:', end=' ')
	prelozene=input()
	return prelozene == preklad[slovo]

while 1:
	slovicko = vyber()
	dej_body()
	#print(body)
	body[slovicko]*=2
	if hadej(slovicko):
		body[slovicko]//=3
		print('PARADKA')
	else:
		print(f'NE, "{slovicko}" je "{preklad[slovicko]}"')
	sleep(0.3)
	print('press enter to continue')
	input()
	print(body)
	print('\n\n\n\n\n')
	
	
