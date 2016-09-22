import random

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
x = random.choice(nums)
x = int(x)


print " Please guess the correct number between 0 and 9, or type '(q)uit' to exit:\n"
    
while True:
      
  try:
   
    line = raw_input(">")
      
    if line == "q" or line == "quit":
        print "Thank you for using this program"
        break   
    elif int(line) > x and int(line) < 10:
        print "You seem to be a little high!"
    elif int(line) < x and int(line) >= 0:
        print "Your number is a little low"
    elif int(line) == x:
        
        print "++++++Thats the number++++++"
        print "~~~~~~Thanks for playing~~~~~~"
        raw_input("***********Press the anykey to exit***********")
        break
    elif int(line) > 9 or int(line) < 0:
        print "please only values from 0-9"
  except:
      print "please no characters"
print "Goodbye!"
    
    

