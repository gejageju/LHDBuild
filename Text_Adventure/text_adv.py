import time
time.sleep(1)
print("Its getting really dark")
time.sleep(2)
print("You came here to this forest with your crew")
time.sleep(1)
print("They are nowhere to be found")
time.sleep(1)
print("It seems like you are stuck here...")
time.sleep(1)
print("All alone ......")
time.sleep(1)

name=input("Enter your name: ")
time.sleep(1)
print("So hello! "+name)
print("Your goal is to find your crewmates before it gets too late!")
time.sleep(1)
print("You  Ready !!??")
input()
print("Make wise choices or else you will die :)")
time.sleep(2)
print("Lets begin !")

time.sleep(3)
print("Its getting dark...\nYou hear the crickets chirp...\nThe leaves rustle due to the slow wind...")
time.sleep(2)
print("You hear the growl of a bear...")
time.sleep(2)
print("From Somewhere Far Away")
time.sleep(2)
print("Its getting really cold")
time.sleep(2)
print("What will you do")
time.sleep(2)
choice=int(input("1. Wait for you crewmates\n2.Try creating a fire\n3.Make noise and cry for help\n"))
if(choice==1):
      time.sleep(2)
      print(name+" keeps waiting in the cold")
      time.sleep(1)
      print(name+" sits there for hours")
      time.sleep(1)
      print(name+" loses stamina slowly and faints")
      time.sleep(1)
      print("Faints in the middle of nowhere in a dangerous forest")
      time.sleep(2)
      print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
if choice==2:
   time.sleep(2)
   print(name+" decides to start a fire\nHow will "+name+" start one")
   x=int(input("1.Make a pit, Gather twigs, slowly build fire with friction\n2.Gather leaves, rub twigs fiercely"))
   if x==2:
       time.sleep(2)
       print(name+" tries creating fire ")
       time.sleep(2)
       print("Yay! "+name+" sees smoke\nThe fire grows")
       time.sleep(3)
       print("Oops !"+name+" starts a forest fire")
       time.sleep(3)
       print(name +" suffocates and dies")
       print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
   if x==1:
       time.sleep(1)
       print(name+ "tries to make fire")
       time.sleep(2)
       print("Yay! "+name+" sees smoke\nThe fire grows")
       time.sleep(2)
       time.sleep(2)
       print("Haaa So warm!")
       time.sleep(2)
       print("This fire saves "+ name+ " from the freezing cold")
       time.sleep(2)
       print(name+"'s tummy starts making noises\nIt seems that "+name+"is hungry!")
       time.sleep(3)
       print("What will "+name+" do now ?")
       time.sleep(2)
       z=int(input("1.Check backpack for food\n2.Pick fruits from a bush nearby\n"))
       if(z==1):
           print(name+" checks backpack for food!")
           time.sleep(2)
           print(name+ " puts their hand inside their backpack")
           time.sleep(2)
           print(name+" : Aaghhhhhhhhhh")
           time.sleep(1)
           print("A scorpion bites "+name+"'s hand")
           time.sleep(3)
           print(name+" dies")
           print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
       if z==2:
           print(name+ " decides to eat wild berries")
           time.sleep(2)
           print(name+" sees  three different fruits ")
           time.sleep(2)
           print("Which fruit will "+name+" eat ?")
           time.sleep(2)
           f=int(input("1.A blueberry\n2.A greenberry\n3.A purpleberry"))
           time.sleep(3)
           if(f==1 or f==3):
               print(name+ " picks the berry and eats it")
               print(name+" : Hmm delicious")
               print(name+ " ...wait.. My eye are getting blurry")
               print(name+ " *faints* ")
               print(name+" picked up a poisonous fruit")
               print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
           if(f==2):
               print(name+ " picks the berry and eats it")
               print(name+" : Hmm delicious")
               time.sleep(3)
               print(name+" : The best fruit I've ever had !")
               time.sleep(2)
               print(" What will "+name+" do now ?")
               x=int(input("1.Try exploring the forest\n2.Get some rest "))
               if x==1:
                  time.sleep(2)
                  print(name+" goes for a walk")
                  print(name+" if it were daytime, this forest would have looked realxing")
                  print(name+" hears a sound")
                  print("Will "+name+" go and check? ")
                  l=int(input("1.Yesss\n2.Ignore"))
                  if(l==1):
                      print(name+" goes and checks")
                      print(name+": hmmm who's there? ")
                      print("Voila!")
                      print(name+" finds her lost teammates!\nCongratulatons!\nThanks for playing with us")
                      exit()
                  if(l==2):
                      print(name+" ignores and walks")
                      print(name+" walks and walks\n"+name+" gets tired")
                      print("What will "+name+ " do?")
                      h=int(input("1.Try to sleep"))
                      print(name+ " decides to sleep")
                      print(name+" has a nice sound sleep, and wakes up fresh")
                      


       
       

if choice==3:
       print(name+" : Help !!!!")
       time.sleep(2)
       print(name+" : Somebody help me!!!")
       time.sleep(3)
       print("You hear the growl of a bear\nFrom somewhere close")
       time.sleep(2)
       print("GRRRRRRRRR")
       time.sleep(2)
       print(name+" sees a wild bear")
       time.sleep(2)
       print("What will "+name+" do ?")
       time.sleep(2)
       x=int(input("1.Try climbing a tree\n2.Run !\n3.Hit the bear with a giant torchlight"))
       if x==1:
           time.sleep(2)
           print(name+ "tries to climb a nearby tree")
           time.sleep(2)
           print(name+" reaches the treetop")
           time.sleep(2)
           print(name+" didnt know that bears are excellent climbers")
           time.sleep(2)
           print("The bear gets "+name)
           time.sleep(2)
           print(name+" becomes bear's meal")
           print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
       if x==2:
           time.sleep(2)
           print(name+" runs really fasts")
           time.sleep(2)
           print("Who knew that "+name+ " is suchan excellent athlete!")
           time.sleep(2)
           print(name+ "outruns the bear \nThe bear is nowhere to be found.")
       if x==3:
           time.sleep(2)
           print(name+" throws the torchlight at the bear")
           time.sleep(3)
           print("Bull's eye !!!")
           time.sleep(2)
           print("Maybe "+name+ " truly is a hero !")
           time.sleep(2)
           print("The bear runs away!")
           print("Victory !")
           time.sleep(3)
           print("What will "+name+" do now?")
           time.sleep(2)
           c=int(input("1. Wait for you crewmates\n2.Try creating a fire\n"))   
           

       