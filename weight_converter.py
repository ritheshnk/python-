weight=int(input("weight: "))
unit=input(" Did you enter your weight in Kg(K) or Pounds(P): ")
if unit.lower()=="K":
    result=weight/0.45
    print(str(result)+" lbs") #need to convert result to str cause python doesnt combine int with str

else:
    result=weight*0.453
    print(str(result)+" Kg") #need to convert result to str cause python doesnt combine int with str
