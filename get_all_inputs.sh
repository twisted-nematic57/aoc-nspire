#!/bin/bash

# Paste your session cookie here (only needed if any inputs aren't cached locally)
SESSION="theTOWWWWWWWNNNinsideMEEEEE"

# AoC guidelines require a descriptive User-Agent
USER_AGENT="github.com/twisted-nematic57/aoc-nspire by twisted.nematic57@gmail.com"

# Create a workspace directory
mkdir -p temp_workspace
cd temp_workspace
cp ../template.py .

# Fetch input and build python scripts for each day
generate_day() {
    local year=$1
    local day=$2
    local input_file="input_${year}_${day}.txt"
    local script_file="day_${year}_${day}.py"

    echo "Processing Year $year Day $day..."

    # Download the input ONLY if we haven't already (use caching)
    if [ ! -f "$input_file" ]; then
        curl -s -b "session=$SESSION" -A "$USER_AGENT" \
            "https://adventofcode.com/$year/day/$day/input" -o "$input_file"

        # This script tries to respect AoC server rate limits to some degree.
        # As per https://www.reddit.com/r/adventofcode/wiki/faqs/automation/ ,
        # it is unclear if rate limits are "every 900s only for leaderboards" or
        # "every 900s for ALL AUTOMATED REQUESTS". A 900s delay is used anyway.
        sleep 900
    fi

    # Check if the session cookie was valid
    if grep -q "Please don't repeatedly request this endpoint before it unlocks" "$input_file" || \
       grep -q "Puzzle inputs differ by user" "$input_file"; then
        echo "Error: Invalid session cookie."
        cat "$input_file"
        rm "$input_file"
        exit 1
    fi

    # Safely inject the input into the Python template
    # Use a quick python one-liner so special characters/newlines don't break bash injection
    python3 -c "
with open('template.py', 'r') as f:
    template = f.read()
with open('$input_file', 'r') as f:
    data = f.read()

# Strip the trailing newline from the data to prevent empty lines at the end of the input
data = data.rstrip('\n')

with open('$script_file', 'w') as f:
    f.write(template.replace('input_goes_here', data))
"
}

echo "Beginning to create template Python files with inputs..."

# Years 2015 to 2024: 25 days
for year in {2015..2024}; do
    for day in {1..25}; do
        generate_day $year $day
    done
done

# Year 2025: 12 days
for day in {1..12}; do
    generate_day 2025 $day
done

# Hacky setup for organizing and renaming the generated Python scripts to the format
# Sorry for the jank. I'm lazy when it comes to scripting. It Works On My Machine™
for f in day_*_*.py; do [[ "$f" =~ day_([0-9]{4})_([0-9]+)\.py ]] && mv -n "$f" $(printf "y%sd%02d.py" "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"); done
mkdir -p py
mv *.py py
mv py/template.py .

echo ""
echo "All inputs have been cached to temp_workspace/. They should not need to be downloaded ever again. Do not delete any .txt files inside temp_workspace."
echo "Done! All scripts generated successfully. See temp_workspace/py for the generated Python files."
echo ""
echo "Note: You may need to manually escape triple-quotes that may appear in the input of 2017 Day 9."
