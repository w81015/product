#第一 Ch.61
#建立一個記帳程式
#可以輸入商品名稱
#按q離開程式
#印出商品
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':  #記得加上''
		break
	products.append(name)
print(products)


#第二 Ch.61
#也讓使用者輸入價格
#印出每個商品的價格
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': #記得加上''
		break
	price = input('請輸入商品價格：') 
		#要問完商品後，再問價格，但有可能沒有商品，所以價格要放在輸入q的後面
	p = []	#建立一個小清單，存放商品名稱和價格
	p.append(name)	#在小清單上加上商品名稱
	p.append(price)	#在小清單上加上商品價格
	products.append(p)	#將小清單放進大清單products
print(products) 	#所有商品和價格

for p in products:
	print(p[0],'的價格是',p[1])

#25-27行：p = [name, price]
#25-28行：products.append([name,price])




#第三 Ch.62 + Ch.63
#價格轉換成整數
#接下來要把輸入的內容存到電腦中
#將輸入的內容存到products.csv中
#在csv中商品名稱和價格分別在第一、二行
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price) #轉換成整數。後面就不能合併。要再轉換成字串。
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('products.csv', 'w', ) as f:
	for p in products: #是products清單中的小清單p
		f.write(p[0] + ',' + str(p[1]) + '\n') #記得要放上+



#第四 Ch.64
#加上標題
#調整編碼
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name,price])
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('products.csv', 'w', encoding = 'utf-8-sig') as f: 
#教學影片上是utf-8，但沒辦法成功；上網搜尋要改成utf-8-sig就成功了（？）
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')


#第五 Ch.65 Ch.66
#讀取檔案
#把檔案中項目分別印出來
#去掉標頭

#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳過第一行
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name,price])
print(products)

#印出所有紀錄
for p in products:
	print(p[0],'的價格是',p[1]) #不是name或price

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8-sig') as f: #記得encoding
	f.write('商品,價格\n')
	for p in products: #記得要products
		f.write(p[0] + ',' + p[1] + '\n')



#第六 Ch.67
#在開始前，檢查檔案在不在

import os #operating system
products = []
if os.path.isfile('products.csv'):
	print('Yeah! File found.')
	with open('products.csv', 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過第一行
			name, price = line.strip().split(',')
			products.append([name, price])
print(products)
else:
	print('No file.')

while True
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

with open('products.csv', 'w', encoding = 'utf-8-sig') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

