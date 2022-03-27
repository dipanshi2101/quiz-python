
def answer(ans,ans1):
    global score
    score=0
    if(ans==ans1):
        print("\n \t YOUR ANSWER IS CORRECT ")
        score=score+1
    elif(ans==ans1.strip()):
        print("\n \t YOUR ANSWER IS CORRECT ")
        score=score+1
    elif(ans is False or ans1 is False):
        print("\n\t YOUR ANSWER IS WRONG ")
    elif(len(ans)!=len(ans1)):
        print("\n \t YOUR ANSWER IS WRONG ")
    else :
        print("\n\t YOUR ANSWER IS WRONG ")
    
    
print("\n\tHELLO MYSELF PIE , AND I'M GOING TO CONDUCT THIS QUIZ WHICH WILL CONSIST 5 ROUNDS , TELL ME SOMETHING ABOUT YOURSELF")
print("\n WHAT IS YOUR NAME : ")
name=input()

if(name == "dipanshi") :
    print("\n HEY I KNOW SOMEONE OF THIS NAME ,ANYWAYS NICE TO MEET YOU : "+name)
else :
    print("\n NICE TO MEET YOU : "+name)

print("\n DO YOU WANT TO PLAY THE QUIZ : (for yes enter 'y' else 'n')")
want=input()
if(want=='y' or want=='Y'):
    print("\n\t WE ARE GOOD TO GO THEN :) ")
else :
    print("\n\t OKAY THEN , NICE TO TALK TO YOU :) ")
    exit()

print('''\n\tIMPORTANT INSTRUCTIONS : 1) PLEASE MAKE SURE THAT YOU TYPE THE CORRECT\n
                                2) THE ANSWER ARE NOT THOUGH "CASE-SENSITIVE" BUT STILL PLEASE USE CASE THAT IS MENTIONED''')

print("\n SO THE, FIRST ROUND IS THE COMPULSARY ROUND AND THIS ROUND IS BASED ON YOUR GENERAL KNOWLEDGE, SO LET'S START \n")

print("\n\n************ ROUND-1 *************\n\n")
#round 1


f1=open('sample.txt','r')


result=0

#1
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR OPTION : ")
ans="B"
ans1=input()
ans1=ans1.upper()

answer(ans,ans1)
if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#2
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="B"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#3
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#4
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

f1.close()

#ROUND-2

print("\n\n\n*********** ROUND-2 ************\n\n")

f1=open('bio.txt','r')

#1
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="B"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#2
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")


#3
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#4
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="B"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")
f1.close()

#ROUND-3

print("\n\n\n*********** ROUND-3 *************\n\n")
f1=open('history.txt','r')

#1
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="B"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#2
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#3

data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#4
data=f1.readline()
print(data)
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="A"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

f1.close()

#ROUND-4

print("\n\n\n************** ROUND-4 **************\n\n")
print("\n ENTER YOUR CHOICE OF SUBJECT : 1 (BOLLYWOOD) 0r 2(IPL) (BY DEFAULT 2) \n")

cho=input()
print("\n ENTERED CHOICE : "+str(cho))
cho=int(cho)
print("\n")

if(cho == 1):
    f1=open('sample2.txt','r')

    #1
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="B"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    
    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
   
    #2
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="A"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    
    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
    
    #3
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="A"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    
    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")

    #4
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="B"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    
    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
    
    f1.close()

else:
    
    f1=open('ipl.txt','r')

    #1
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="A"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    

    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
   
    #2
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="B"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    

    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
    
    #3
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="B"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    

    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")

    #4
    data=f1.readline()
    print(data)
    data=f1.readline()
    print(data)
    print("\n ENTER YOUR ANSWER : ")
    ans="A"
    ans1=input()
    ans1=ans1.upper()
    answer(ans,ans1)
    

    if(score==1):
        result=result+2

    print("\n YOUR SCORE IS - "+str(result)+"\n\n")
    
    f1.close()



#ROUND-5
print("\n\n************ ROUND-5 *************\n")

print("\n\n TRUE/FALSE  ROUND : ENTER T FOR TRUE AND F FOR FALSE \n")

f1=open('true.txt','r')

#1
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="T"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)


if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#2
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="T"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)


if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#3

data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="T"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)


if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

#4
data=f1.readline()
print(data)
print("\n ENTER YOUR ANSWER : ")
ans="F"
ans1=input()
ans1=ans1.upper()
answer(ans,ans1)

if(score==1):
    result=result+2

print("\n YOUR SCORE IS - "+str(result)+"\n\n")

f1.close()


#result
print("\n\n \t YOUR FINAL SCORE (out of 40) is : ",end="")
print(result)

if(result==40):
    print("\n\n\t\t YOU PLAYED VERY WELL"+name)
    print("\n\t\t CONGRATULATIONS")

elif(result<40 and result>=30):
    print("\n\n\t\t YOUR SCORE IS QUITE GOOD , KEEP IT UP "+name)

elif(result<30 and result>=23):
    print("\n\n\t\t YOU NEED TO WORK ON SOME TOPICS "+name)

else:
    print("\n\n\t\t YOU REALLY NEED TO WORK HARD , GOOD LUCK "+name)

