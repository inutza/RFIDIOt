# RFIDIOt.py - RFID IO tools for python

This is a port of the RFIDIOt core to python 3. **It has not been thoroughly
tested!** The ported core can be found in the `py3_rfidiot` folder. So use

```python
import py3_rfidiot
```

Basically applied `2to3` to the `rfidiot/` files and fixed a few issues that
popped up:

* moved to format strings for prints -- v likely some were missed
* removed the use of `string` module
* adjusted reader names to remove `PICC` as it wasn't matching (at least for ACR122U)

Example files ported and tested are added with the `py3_` prefix.

E.g: `py3_send_apdu.py` works. None of the other example files from the
original repo have been tested, hence why there aren't any `py3_` variants. 
Port them if you need them.

PRs welcome.

/* 
 * Adam Laurie <adam@algroup.co.uk>
 * http://rfidiot.org/
 *
 * This code is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This code is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 */

Copyright (c) 2006-2011 Adam Laurie <adam@algroup.co.uk>

q: What is RFIDIOt?
a: A collection of tools and libraries for exploring RFID technology, written 
in python.

q: Why RFIDIOt?
a: I like silly puns. Also, I'm coming at this from an idiot's point of view: 
I know nothing about RFID tags, and even less about python. As such, I felt a 
complete idiot when I started. :)

q: How can I contribute?
a: Send me patches, info, new tools, coffee, money, drugs and/or a Miles Davis song :) 

q: What hardware is supported?
a: So far this works with the ACG serial readers. I use the CF Card model, 
but it should also work with the USB version by changing the serial port to 
/dev/ttyUSB0. You can find more details here:

  http://www.acg.de

q: So what exactly is here?
a: Please see http://www.rfidiot.org/documentation.html
