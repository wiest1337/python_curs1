#urok 7 s utuba
shopping_list=[]
product=(input('Вводи товары по одному: '))
while product != 'stop' :
    shopping_list.append(product)
    if shopping_list[-1]=='hleb':
        shopping_list.remove ('hleb')
    product=(input('Вводи товары по одному: '))

shopping_list.sort()


count = 1
for a in shopping_list:
    print(count,')' , a)
    count+=1
print(shopping_list[0])  
print(shopping_list[-1])  
