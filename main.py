J="_O@" # version 2
HEIGHT=6 #max 6
WIDTH=7 #max 11/21

x=[[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
tour,joue,coup=0,1,0

def pr(x):
  for row in x:
    for n in row:
      print(J[n]+" ",end="")
    print()

def jouer_coup(coup):
  try: #Coup valide ?
    coup=int(coup)
  except:
    return -69

  if coup==0:
    return -2
  if coup==-1:
    return -1
  if coup>WIDTH or coup<0:
    return -69
  
  i=1
  while i<=HEIGHT:
    if x[HEIGHT-i][coup-1]!=0:
      i+=1
    else:
      x[HEIGHT-i][coup-1]=joue
      break

  if i==HEIGHT+1: #Colonne pleine ?
    return -69

  return 0 #Tout est good :)
while tour<HEIGHT*WIDTH:
  pr(x)

  coup=input(str(joue)+">")

  coco = jouer_coup(coup)
  if coco==0:
    tour+=1
    joue=(tour%2)+1
  elif coco==-2:
    break
  
pr(x)  
print("fini")
