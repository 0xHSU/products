import os

product = []

if os.path.isfile('product.csv'):
    print('找到')
    with open ('product.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name,price])
    print(product)    
else:
    print('找不到')    


while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入價格:')
    product.append([name, price])
print(product)

for p in product:
    print(p[0], "的價格是", p[1])

with open('product.csv' ,'w', encoding = 'utf-8') as f :
    f.write('商品,價格\n')
    for p in product:
        f.write(p[0] + ',' + p[1] + '\n') 
