def gVal(i, height):
    i+=1
    if(i==1):
        if(height>11000):
            height=11000
        else:
            height=height
    elif(i==2):
        if(height>20000):
            height=20000
        else:
            height=height
    elif(i==3):
        if(height>32000):
            height=32000
        else:
            height=height
    elif(i==4):
        if(height>47000):
            height=47000
        else:
            height=height
    elif(i==5):
        height=height
    first=float(6371*6371)
    second=float((6371+height/1000)*(6371+height/1000))
    g=9.8065*first/second
    return g

##def hVal(height):
##    height=float(6371/(6371+(height/1000))*height)
##    return height

def aVal(stage):
    stage+=1
    if(stage==1):
        a=(-0.0065)
    elif(stage==2):
        a=0
    elif(stage==3):
        a=0.001
    elif(stage==4):
        a=0.0028
    elif(stage==5):
        a=0
    return a
    
def stageHeight(stage, height):
    stage+=1
    if(stage==1):
        if(height>11000):
            height=11000
        else:
            height=height
    elif(stage==2):
        if(height>20000):
            height=9000
        else:
            height-=11000
    elif(stage==3):
        if(height>32000):
            height=12000
        else:
            height-=20000
    elif(stage==4):
        if(height>47000):
            height=15000
        else:
            height-=32000
    elif(stage==5):
        height-=47000
    return height

def formula1(stage, height):
    initHeight=height
    temp=288.15
    density=1.22522
    pressure=101325
    for i in range(0,stage):
        height=stageHeight(i, initHeight)
        g=gVal(i, initHeight)
        a=aVal(i)
        if ((i!=1)&(i!=4)):
            tempNew=temp+a*height
            pressure=pressure*(pow((tempNew/temp),(-g/(a*287))))
            density=density*(pow((tempNew/temp),((-g/(a*287))-1)))
            temp=tempNew
        else:
            temp=temp
            pressure=pressure*(pow(2.7182,(-g/(287*temp)*(height))))
            density=density*(pow(2.7182,(-g/(287*temp)*(height))))
    print "Temperature at height",initHeight,"=",temp
    print "Pressure at height",initHeight,"=",pressure
    print "Density at height",initHeight,"=",density

    
height=input("Enter the height at which values are required: ")
if(height<=11000):
    formula1(1, height)
elif((height>11000)&(height<=20000)):
    formula1(2, height)
elif((height>20000)&(height<=32000)):
    formula1(3, height)
elif((height>32000)&(height<=47000)):
    formula1(4, height)
elif((height>47000)&(height<=100000)):
    formula1(5,height)
else:
    print "Out of Bounds!"
