weight=int(input("weight: "))
unit=input(" Did you enter your weight in Kg(K) or Pounds(P): ")
if unit.lower()=="K":
    result=weight/0.45
    print(str(result)+" lbs")
else:
    result=weight*0.453
    print(str(result)+" Kg")
