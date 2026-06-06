# ---- Solution Running Options ----------
l=const(1) #If false, suppress console output
#(Prepend "if l: " to every print statement in your
# code for the above to take effect.)
_part=const(1) #Which part to run, 1 or 2?


# ---- Start of internal runner code --------
import gc
from time import *
from mlstringhelper import *

#BE CAREFUL! Very long lines lag the editor.
input=MLStringHelper("""[input]""")

def mround(val,p):
  return "{:.{}f}".format(val,p)

def printmeminfo():
  print("Heap used/free (KB): "+mround(gc.mem_alloc()/1024,3)+"/"+mround(gc.mem_free()/1024,3))

def main():
  tstart=ticks_ms()
  if _part==1:
    part1()
  else:
    part2()
  tend=ticks_ms()
  
  print("-----------------------------------")
  print("Total time (s): "+mround(ticks_diff(tend,tstart)/1000,2))
  printmeminfo()

# ---- End of internal runner code ---------

from array import array

# ---- PART 1 ----------------------
def part1():
  pos=array('h')
  pos.append(0) #Start at 0,0
  pos.append(0) # [x,y]; len(pos)==2 always
  known=array('h') #Flattened tuple list
  known.append(0) #First house also gets a
  known.append(0) # present!
  
  for c in input.get_line(0):
    if c==">":
      pos[0]+=1
    elif c=="<":
      pos[0]-=1
    elif c=="^":
      pos[1]+=1
    elif c=="v":
      pos[1]-=1
    
    visited=0 #bool
    for i in range(0,len(known),2):
      if known[i]==pos[0] and known[i+1]==pos[1]:
        visited=1
    if not visited: #Record new house!
      known.append(pos[0])
      known.append(pos[1])
    
  if l: print("Present-receiving houses: "+str(int(len(known)/2)))


# ---- PART 2 ----------------------
def part2():
  pos=array('h')
  pos.append(0) #Start at 0,0
  pos.append(0) # [x,y]; len(pos)==2 always
  robo_pos=array('h') #Same as above, but for
  robo_pos.append(0) # robo-santa
  robo_pos.append(0)
  known=array('h') #Flattened tuple list
  known.append(0) #First house also gets a
  known.append(0) # present!
  
  for i,c in enumerate(input.get_line(0)):
    curr_pos=pos if i%2==0 else robo_pos
    
    if c==">":
      curr_pos[0]+=1
    elif c=="<":
      curr_pos[0]-=1
    elif c=="^":
      curr_pos[1]+=1
    elif c=="v":
      curr_pos[1]-=1
    
    visited=0 #bool
    for i in range(0,len(known),2):
      if known[i]==curr_pos[0] and known[i+1]==curr_pos[1]:
        visited=1
    if not visited: #Record new house!
      known.append(curr_pos[0])
      known.append(curr_pos[1])
    
  if l: print("Present-receiving houses: "+str(int(len(known)/2)))


# ---- Launch! -----------------------
main()
