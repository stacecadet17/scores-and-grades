import random

for num in range(1, 10):
    num = random.randint(60, 100)
    if(num >= 60 and num <= 69):
      print "score:" + str(num) + ";" + " " + "Your Grade is D"
    elif(num >= 70 and num <= 79):
      print "score:" + str(num) + ";" + " " + "Your Grade is C"
    elif(num >= 80 and num <= 89):
      print "score:" + str(num) + ";" + " " + "Your Grade is B"
    elif(num >= 90 and num <= 100):
      print "score:" + str(num) + ";" + " " + "Your Grade is A"
