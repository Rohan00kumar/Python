l = [];
while True :
    c=int(input('''
          1 Push operation
          2 pop operation
          3 peek elemrnt
          4 diplay stack
          5 break
          '''
          ))
    if c ==1 :
        n= input("Enter any number : ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Stack is Empty")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Stack is empty")
        else:
            print("Last value of stack",l[-1])
    elif c==4:
        print("Display stack is full")       
    elif c==5:
        break;
            