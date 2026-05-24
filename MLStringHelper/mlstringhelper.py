#Multiline String Helper 1.0 for TI-Nspire Python
#By twisted_nematic57
#Released under AGPLv3 (see ./LICENSE or
# the next tab)

from array import array

class MLStringHelper:
  def __init__(self, istr):
    self.istr=istr
    self.calc_offsets()
  
  def calc_offsets(self):
    length=len(self.istr)
    
    #Optimize memory use of stored indicies.
    # Many multiline strings are < 253 chars
    # long, and very few may be > ~4.3 billion
    # chars long.
    #(For why these numbers are slightly off of
    # the int limits, see below)
    if 0<=length<=253:
      type='B' #8b
    elif 254<=length<=65533:
      type='H' #16b
    else:
      type='I' #32b (overkill for *most* strings)
    
    self.offsets=array(type)
    # First line always starts at index 0
    self.offsets.append(0)
    
    pos=self.istr.find("\n")
    while pos!=-1:
      #pos+1 is saved instead of pos to avoid
      # math wierdness later
      self.offsets.append(pos+1)
      pos=self.istr.find("\n",pos+1)
    #Consider there to be a trailing \n to avoid
    # unnecessapy branches later
    self.offsets.append(length+1)
  
  #Get the total number of lines
  def num_lines(self):
    return len(self.offsets)-1
  
  #Get a char
  def get_char(self, i):
    return self.istr[i]
  
  #Set a char
  def set_char(self, i, c):
    old_c=self.istr[i]
    self.istr=self.istr[:i]+c+self.istr[i+1:]
    if c=='\n' or old_c=='\n':
      self.calc_offsets()
  
  #Add a char
  def add_char(self, i, c):
    self.istr=self.istr[:i]+c+self.istr[i:]
    self.calc_offsets()
  
  #Remove a char
  def remove_char(self, i):
    self.istr=self.istr[:i]+self.istr[i+1:]
    self.calc_offsets()
  
  #Get a line
  def get_line(self, i):
    return self.istr[self.offsets[i]:self.offsets[i+1]-1]
  
  #Set a line
  def set_line(self, i, txt):
    self.istr=self.istr[:self.offsets[i]]+txt+self.istr[self.offsets[i+1]-1:]
    self.calc_offsets()
  
  #Add a line
  def add_line(self, i, txt):
    self.istr=self.istr[:self.offsets[i]]+txt+"\n"+self.istr[self.offsets[i]:]
    self.calc_offsets()
  
  #Remove a line
  def remove_line(self, i):
    self.istr=self.istr[:self.offsets[i]]+self.istr[self.offsets[i+1]:]
    self.calc_offsets()
