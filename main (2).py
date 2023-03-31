a=int (input ("Трехзначное число пробега"))k= int(input ("Двухзначное число даты"))
if a>99 and a<1000:    b=a//1000
    b=a%1000    c=b//100
    d=b%100    f=d//10
    i=f%10    s=b+c+f+1
if k>9 and k<100:    q=k//100
    q=k%100    W=q//10
    m=q%10    n=q+w+m
if s>n:    print ("Сброс")
else:
    print (s, 'Сегодня не сломался')

