from random import randint
print("1-камінь")
print("2-ножниці")
print("3-папір")
print("якщо бажаєте завершити гру введіть 0")
w1=0
w2=0
n=0
f=1
while(f!=0):
    x=int(input("Ваш хід:"))
    y=randint(1,3)
    if(x==0):
        f=0
        print("Дякую за гру")
    else:
        print("Хід компютера:",y)
    if(x==y):
        print("Нічия")
        n=n+1
    if((x==1) & (y==2)):
       print("Ви перемогли!")
       w1=w1+1
    if((x==2) & (y==1)):
       print("Перемога компьютера")
       w2=w2+1
    if((x==1) & (y==3)):
       print("Перемога компьютера")
       w2=w2+1
    if((x==3) & (y==1)):
       print("Ви перемогли!")
       w1=w1+1
    if((x==2) & (y==3)):
       print("Ви перемогли!")
       w1=w1+1
    if((x==3) & (y==2)):
       print("Перемога компьютера")
       w2=w2+1
    print("Нічиїх:",n)
    print("Ваших перемог:",w1)
    print("Перемог компютера:",w2)
