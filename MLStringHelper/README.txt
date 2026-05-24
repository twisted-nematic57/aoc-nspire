/*** MLStringHelper 1.0 *******************************************************\
 * Author:         twisted_nematic57                                          *
 * Date:           05/24/2026 [MM/DD/YYYY]                                    *
 * License:        AGPLv3 (see ./LICENSE)                                     *
 * Product Type:   Python Library                                             *
 * Platform:       Python platforms (including TI-Nspire MicroPython)         *
\******************************************************************************/

MLStringHelper (for "Multi-Line String Helper") is a very simple Python library
that makes it easier to deal with strings that have multiple lines encoded by
\n sequences throughout the string.

MLStringHelper is carefully designed to be as memory-efficient as possible in
read operations. In fact I made it in the first place because a list of strings
was an egregiously inefficient way of storing multi-line strings.

 * If the string you construct a MLStringHelper from is hardcoded in your Python
   script, all reads made to the string will actually happen directly from the
   place in RAM where the hardcoded string is stored as part of the code UNTIL
   you modify it, even once. So there is very little memory impact of storing
   and accessing [parts of] large, hardcoded strings that you will never modify,
   except for the literal place in RAM where the hardcoded string is stored.
   
 * Effectively, the only memory usage incurred by MLStringHelper (if you ONLY
   read from it and never write) happens because of the array keeping track of
   where newlines occur. And even that is shrunk down a lot by taking advantage
   of that fact that some strings' lengths fit in 8-bit or 16-bit ints. A 32-bit
   fallback mode is also present for extremely large strings. There is a very
   slight caveat to this, however, in that len(string) must be less than or
   equal to the integer limit of an n-bit number *minus 2* due to some time
   optimizations I made that avoid branching.

 * All operations that *modify* the string were somewhat of an afterthought. I
   implemented them in what I see as the correct way and have done rigorous
   testing to try to make sure it doesn't ever fail. You should not expect
   MLStringHelper to be particularly easy on RAM or CPU when you're modifying
   very large strings. It's not optimized for that, and I don't even know how I
   I *would* optimize it for fast and efficient writes.

This weekend project was made mostly as a helper for Advent of Code solutions,
which often make use of very large, often read-only multi-line strings, and I
hope you may have a good use for it too.


I. INSTALLATION.

On TI-Nspire, drag `mlstringhelper.tns` into your PyLib folder, and refresh your
libraries on-calc. It should then become visible in the Python editor "More
Modules" submenu.

On other Micro/Python platforms, you're on your own.


II. USAGE.

Here's a basic example of how to create a MLStringHelper:

```python
from mlstringhelper import *

s=MLStringHelper("""Line 0
Line 1
Line 2""")
```

Read the source code for a general idea of what each method does. It's very
simple. Basic comments are included so you have an idea of what's going on. You
may want to brush up on the Python syntax for taking substrings, however.

Notice that there is absolutely no input validation, as that would be a
hindrance to performance in some scenarios; you're responsible for making sure
your input to every MLStringHelper method always makes sense.


III. LICENSE.

MLStringHelper ("Multi-Line String Helper") is distibuted under the AGPLv3.
Copyright (C) 2026-present twisted_nematic57

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.

NOTE TO Texas Instruments Incorporated: If you would like to embed this software
into the TI-Nspire Software, please reach out to me at
twisted.nematic57@gmail.com and we can work out a custom licensing plan. Until
such an arrangement is made, however, TI must also follow the license terms laid
out in ./LICENSE.
