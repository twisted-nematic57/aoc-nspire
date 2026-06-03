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

#import ...

# ---- PART 1 ----------------------
def part1():
  total=0
  for i in range(0,input.num_lines()):
    d=list(map(int,input.get_line(i).split("x")))
    #0=length,1=width,2=height (index=value)
    ln=d[0]
    w=d[1]
    h=d[2]
    total+=2*ln*w+2*w*h+2*h*ln
    
    d.sort()    
    ln=d[0]
    w=d[1]
    
    total+=ln*w
  if l: print("_ft**2 of wrapping paper needed: "+str(total))


# ---- PART 2 ----------------------
def part2():
  total=0
  for i in range(0,input.num_lines()):
    d=list(map(int,input.get_line(i).split("x")))
    d.sort()
    ln=d[0] #smallest
    w=d[1] #2nd smallest
    h=d[2]
    total+=ln*w*h+2*(ln+w)
  if l: print("_ft of ribbon needed: "+str(total))


# ---- Launch! -----------------------
main()

