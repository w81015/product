import os #operating system

#讀取檔案
def read_file():
    products = []
    if os.path.isfile('products.csv'):
        print('Yeah! File found.')
        with open('products.csv', 'r', encoding = 'utf-8-sig') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
        print(products)
    else:
        print('No file.')

#讓使用者輸入
def input():
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        products.append([name, price])
    print(products)

#印出所有紀錄
def print():
    for p in products:
        print(p[0],'的價格是',p[1])

#寫入檔案
def write():
    with open('products.csv', 'w', encoding = 'utf-8-sig') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

read_file()