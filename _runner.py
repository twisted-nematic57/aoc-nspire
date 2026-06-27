#SolveKit-nspire
#AoC Solution Runner & Benchmarker
#Released under the AGPLv3
#See ./LICENSE and ./README.md in the Git
# repo for license plaintext and documentation

def main():
  #Note that all config vars are booleans except
  # the solution reference and benchmarking
  # iteration count.
  
  import y2015d01 as _s #Solution selector
  _part=const(0) #Part to run minus 1 (0 or 1)
  _loud=const(1) #(dis/en)able console output
  
  _mode=const(0) #0=one run; 1=benchmark
  _iters=const(1024) #Benchmarking iterations
  _m=const(1) #Print benchmarking progress?
  
  # ---- Start of internal runner logic -------
  import gc
  from time import *
  import ti_system
  
  #Returns a string containing val rounded to p
  # decimal places
  def mround(val,p):
    return "{:.{}f}".format(val,p)
  
  #Prints used/free RAM numbers in kilobytes
  def printmeminfo():
    print("Heap used/free (kB): "+mround(gc.mem_alloc()/1000,3)+"/"+mround(gc.mem_free()/1000,3))
  
  # ---- RUNNER CORE --------------
  _tstart=0 #Preinit these to save some μs(?)
  _tend=0
  target=_s.part2 if _part else _s.part1
  
  if _mode: #Benchmark
    runtimes=[0.0]*_iters
    tstr=""
    for i in range(_iters):
      gc.collect()
      #-BEGIN PERF. CRIT. SEGMENT-
      _tstart=ticks_ms()
      target(_loud)
      _tend=ticks_ms()
      #-END PERF. CRIT. SEGMENT-
      #runtimes.append(mround(ticks_diff(_tend,_tstart)/1000,2))
      tstr=mround(ticks_diff(_tend,_tstart)/1000,2)
      if _m: print("Run "+str(i+1)+" (s): "+tstr)
      runtimes[i]=float(tstr)
    print("-----------------------------------")
    print("Saving & computing statistics…")
    ti_system.store_list("runtimes",runtimes)
    
    print("Done. See statistics in the spreadsheet tab.")
  else: #Single run
    gc.collect()
    #-BEGIN PERF. CRIT. SEGMENT-
    _tstart=ticks_ms()
    target(_loud)
    _tend=ticks_ms()
    #-END PERF. CRIT. SEGMENT-
    
    print("-----------------------------------")
    print("Total time (s): "+mround(ticks_diff(_tend,_tstart)/1000,2))
    printmeminfo()

main()
