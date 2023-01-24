print('''
*******************************************************************************
                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
''')
print("Survival!!  Gator Attack!!")
print("Your mission is to find safety.") 

#Write your code below this line 👇
Choice1 = input(''' Oh No!! On your first Everglades tour, the air boat had hit an unknown 
object has begun to sink.  You can Wait for the captain to give instructions or you can start swimming towards a small inlet 20 feet away.

Wait
or
Swim ? \n

''')

if Choice1.lower() == 'swim':
  print('''
*******************************************************************************
                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
GameOver!!!

Halfway towards the inlet you are grabbed by a Gator and pulled under.  You are never seen again.
  
  ''')

elif Choice1.lower() == 'wait':
  Choice2 = input('''\n The captian fires a couple shots in the water to scare off near-by gators, then guides the group through the water towards shallow wetland.  Darkness is slowing creeping over the swamp.
A couple feet ahead of the group is an aggitated gator protecting its nest.  It charges towards the group!!!! 

  Do run to the Right
  or
  Left ?\n
  
  ''')
  if Choice2.lower() == "right":
    print('''
*******************************************************************************
                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
GameOver!!!

You trip over a tree root and get mauled by the gator.
  
  ''') 
  elif Choice2.lower() == "left":
    choice3 = input('''\n You run to left while some of your group runs to the right.  You glance back to see the gator had grabbed one of the group members who had fell !!  Through the clearing ahead, you notice a light glowing in the distance.  Meanwhile you notice the captain running in another direction.  

  Do you:
  turn back to help,
  follow the captain
  or
  go towards the light?
  
  answer by typing (help, follow or light)\n
  
  ''')
    if choice3.lower() == 'follow':
      print('''
*******************************************************************************
                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
GameOver!!!

You lose sight of the captain and end up lost.  As you try to gain a sense of direction you hear a menacing bellow move towards you.  You are never found!!!
  
  ''') 
    elif choice3.lower() == 'light':
      print('''
*******************************************************************************
                   _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
*******************************************************************************
GameOver!!!

As you move closer to the light you see more small lights starting to pop up in the dark.  By the time you realize the glows are eyes, You are dragged into the shadows !!!
  
  ''') 

    elif choice3.lower() == 'help':
      print('''
*******************************************************************************
  
                                          |   ____     _____
     ___                                  |  |____|   |_____|
    |\_ --------__,+-_____________________|____________________-------
    \  `===#==__|__/\____|_____|_______|_______|_______|_____-------
     \
      |   Everglades Park Ranger
       \
    ~~~~-\_ /~~=._         ~~~~~~~~~~~             ~~~~~~~~~~~~~
~~~~      =/       ~~~~~~~~ ~~~~~~    ~~~~~~~~~~~~~             ~~~~~           
*******************************************************************************


You grab the gator's tail and it snaps towards to you!!! It is sizing you up but is hesitant to attack.
It gives the other tourist time to get up and move a safe distance away.  It hissing before backing away towards its nest.
As you regroup with the others, a boat is seen coming towards the area with a bright light.
It is a park ranger!! The crew is saved !!!!! 
  
  ''') 

  else:
      print('''
*******************************************************************************
  
 .d888                     888 
d88P"                      888 
888                        888 
888888 .d88b.  .d88b.  .d88888 
888   d88""88bd88""88bd88" 888 
888   888  888888  888888  888 
888   Y88..88PY88..88PY88b 888 
888    "Y88P"  "Y88P"  "Y88888          
*******************************************************************************
Game Over!!!

In your shcock and panic, you failed to make a decision.  In a matter of moments another nearby gator seizes the opportunity.!!!!
You become gator food!!!! 
  
  ''') 