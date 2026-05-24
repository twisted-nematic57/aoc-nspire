# aoc-nspire

### Latest completed problem: TBD **(0/262)**

The goal is simple: **Solve every single Advent of Code problem in TI-Nspire MicroPython using just over 2MB of heap space per problem.** In a world full of bloated, vibecoded slop, it's important to remember what computer programming is *actually about:* tricking rocks into doing funny math just for the fun of it. Sometimes those [rocks](http://www.datamath.org/Graphing/NSpire_CXII_CAS.htm#:~:text=The%20ARM9%20CPU%20is%20integrated%20into%20an%20ASIC%20with%20the%20markings%20ET%2DNS2018%2D001%20%28S6M98%29) will come in proprietary, bespoke, absurdly overpriced [packages](https://education.ti.com/en/products/calculators/graphing-calculators/ti-nspire-cx-ii-cx-ii-cas), but the fun and novelty just gets stronger the weirder the platform is.

Here are the details of my platform on a blank shell:

![A screenshot of the TI-Nspire MicroPython Shell showing all essential information about its implementation. Python version 3.4.0, MicroPython version 1.11.0, and 2036192 bytes of RAM are free.](assets/nspirepython.png)

I never even use [`@micropython.native`](https://docs.micropython.org/en/v1.9.3/pyboard/reference/speed_python.html#the-native-code-emitter) or [`@micropython.viper`](https://docs.micropython.org/en/v1.9.3/pyboard/reference/speed_python.html#the-viper-code-emitter) due to it being unavailable as an anti-exploit measure by TI. I consider this to be just another challenge to time-optimize my code as much as possible.
## Code & Measurements

The source code of my solutions is accessible to those without access to the TI-Nspire computer software. Plaintext Python files are provided as solution source code; in fact the corresponding native TI-Nspire files are not provided at all, given that they can just be copy-pasted into the Nspire Computer Software as needed. A comprehensive [table of runtimes](./RUNTIMES.md) is also maintained.

You may also notice that a library called [MLStringHelper](./MLStringHelper/) is bundled in this repository. It is primarily there just to make it easier to deal with multi-line strings in Python without having to resort to egregiously inefficient lists of strings. Take a look at its [README](./MLStringHelper/README.txt) for more info.

## How I set this up

You'll notice I have a few funny looking scripts, [`get_all_inputs.sh`](./get_all_inputs.sh) and [`nspire_setup_macro.ahk`](./nspire_setup_macro.ahk).

First of all, I apologize for the very hacky nature of these. It Works On My Machine™ which is composed of a Fedora host and a Windows VM in VirtualBox which I use to run the proprietary TI-Nspire Software. If you want to reproduce this process yourself and you get stuck, feel free to [open an issue](https://github.com/twisted-nematic57/aoc-nspire/issues/new) to ask for help.

`get_all_inputs.sh` gets all inputs from the Advent of Code server, caches them in plaintext files, and creates a series of Python files that I'll use as starting points for solutions to each day of each year. Then, `nspire_setup_macro.ahk` will copy-paste them into the proprietary TI-Nspire Software so that I can edit my Python files on the physical calculator itself. The pasting process, however, happens on a year-by-year basis, meaning that as of mid-2026, I have to run the AutoHotKey script 10 times just to paste all my files. There is a good justification for this: it's not good to keep *that much data* in one TI-Nspire document. So I manually split up on-calculator documents (which you can basically think of as "project files") year-by-year.

## AoC Policies

In compliance with [Advent of Code's policies](https://adventofcode.com/2025/about#:~:text=please%20don%27t%20include%20parts%20of%20Advent%20of%20Code%20like%20the%20puzzle%20text%20or%20your%20inputs) regarding copying and sharing, my inputs are not included in this repository. Please [open an issue](https://github.com/twisted-nematic57/aoc-nspire/issues/new) if you discover I accidentally left one my inputs visible publicly.

