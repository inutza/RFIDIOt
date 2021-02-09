#!/usr/bin/python3

#
# reblay_send_apdu.py - Merge of send_apdu.py from RFIDIOt repo
# and hf_reblay_emulating.py from
# https://github.com/salmg/proxmark3/blob/master/tools/hf_reblay-emulating.py
# Proxmark must be in standalone, emulation mode
# version 0.1
# Ina Radu <neko3@inaradu.com>

#
# This code is copyright (c) Ina Radu, 2020, All rights reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import py3_rfidiot
import sys
import os

import serial
from smartcard.util import toHexString, toBytes, PACK
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest

PASS = '[+]' 
FAIL = '[-]' 
IN_PROGRESS = '...' 
READER = 'R > C:'
CARD = 'C > R:'

if __name__ == '__main__':

	## connect to ACS
	try:
			card= py3_rfidiot.card
	except:
		print(FAIL, "Couldn't open reader!")
		sys.exit(1)


	card.select()
	print(PASS, "Connected to card; ID: ", card.uid)

	## connect to proxmark
	## hint: bind bt interface with
	## sudo rfcomm bind rfcomm0 [proxmark bt address]
	ser = serial.Serial('/dev/rfcomm0')  # open Proxmark3 Bluetooth port

	print(IN_PROGRESS, "Connecting to proxmark; check blue light is STEADY")
	print(IN_PROGRESS, "Waiting for data from proxmark...")

	try:
		while True:
			initd = ser.read(1)
			data = ser.read(int.from_bytes(initd, "big"))
			capdu = toHexString(list(data), format=PACK) 

			print(READER, capdu)

			r = card.pcsc_send_apdu(capdu)

			## create list from card response
			rapdu = [int(a+b, 16) for a,b in zip(card.data[::2], card.data[1::2])]
			rapdu.extend([int(a+b, 16) for a,b in zip(card.errorcode[::2], card.errorcode[1::2])])
			print(CARD, toHexString(rapdu, PACK))

			ser.write(rapdu)

	except KeyboardInterrupt:
		print(FAIL, "Program interrupted; exit")
		sys.exit(1)