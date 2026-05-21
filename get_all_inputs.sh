#!/bin/bash

# Paste your session cookie here
SESSION="labubucakepartysoda_0xdeadbeef"

# AoC guidelines require a descriptive User-Agent
USER_AGENT="github.com/twisted-nematic57/aoc-nspire by twisted.nematic57@gmail.com"
# ==========================================

# Create a workspace directory
mkdir -p aoc_workspace
cd aoc_workspace

cat << 'EOF' > template.py
from time import *
from mlstringhelper import *

#"print" string if not in quiet mode
def prt(string):
  if(not quiet):
    print(string)

#Input. BE CAREFUL!
input=MLStringHelper("""stuff1234""")
#
#
#
#
#
#
#
#
#
#
# ---- Start of internal handler code --------
part=1 #Which part to run, 1 or 2?
quiet=0 #Minimize printing? ([True/1]/[False/0])

def main():
  if part==1:
    ___tstart=clock()
    p1()
  else:
    ___tstart=clock()
    p2()

  ___tend=clock()
  print("-----------------------------------")
  print("Total time: "+str(___tend-___tstart)+"_s")
# ---- End of internal handler code --------

#import ...

# ---- PART 1 ----------------------
def p1():
  prt(":3")

# ---- PART 2 ----------------------
def p2():
  prt(":3 again!!!")

# ---- Some more internal stuff -----------
main()
EOF

# Fetch input and build each python script
generate_day() {
    local year=$1
    local day=$2
    local input_file="input_${year}_${day}.txt"
    local script_file="day_${year}_${day}.py"

    echo "Processing Year $year Day $day..."

    # Download the input ONLY if we haven't already (caching)
    if [ ! -f "$input_file" ]; then
        curl -s -b "session=$SESSION" -A "$USER_AGENT" \
            "https://adventofcode.com/$year/day/$day/input" -o "$input_file"

        # Be a *little* respectable
        sleep 2
    fi

    # Check if the session cookie was valid
    if grep -q "Please don't repeatedly request this endpoint before it unlocks" "$input_file" || \
       grep -q "Puzzle inputs differ by user" "$input_file"; then
        echo "Error: Invalid session cookie or puzzle not unlocked yet."
        cat "$input_file"
        rm "$input_file"
        exit 1
    fi

    # Inject into the template python file
    python3 -c "
with open('template.py', 'r') as f:
    template = f.read()
with open('$input_file', 'r') as f:
    data = f.read()

# Strip the trailing newline from the data to prevent empty lines at the end of the input
data = data.rstrip('\n')

with open('$script_file', 'w') as f:
    f.write(template.replace('stuff1234', data))
"
}

echo "Starting Advent of Code Setup..."

# Years 2015 to 2024: Full 25 days
for year in {2015..2024}; do
    for day in {1..25}; do
        generate_day $year $day
    done
done

# Year 2025: Days 1 to 12
for day in {1..12}; do
    generate_day 2025 $day
done

echo "Done! All scripts generated successfully."
