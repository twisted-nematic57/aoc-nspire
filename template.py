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
input=MLStringHelper("""input_goes_here""")

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
  if l: print(":3")


# ---- PART 2 ----------------------
def part2():
  if l: print(":3!!!")


# ---- Launch! -----------------------
main()