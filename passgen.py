"""
    Python Password Generator
    Copyright (C) 2021 Mandar Naik

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
from colorama import Fore, Back, Style
import random
import numpy
import sys
import re

my_parser = argparse.ArgumentParser(description='dice ware implementation for generating password using python!.')
my_parser.add_argument("N", type=int, help="length of password")
my_parser.add_argument("-g", default=False, action="store_true", help="generate a N length password")
my_parser.add_argument("-e", default=False, action="store_true", help="entropy of N length password")
my_parser.add_argument("-l", default=False, action="store_true", help="strongness of N length password")
my_parser.add_argument("-c", default=False, action="store_true", help="combination of N length password")
args = my_parser.parse_args()

def generate_password(password_length):
    global list2string
    list = []
    for x in range(password_length):

            roll_one = random.randint(1, 6)
            roll_two = random.randint(0, 5)
            roll_three = random.randint(0, 5)

            if roll_one == 1 or roll_one == 2:
                array = numpy.array([
                    ["a", "b", "c", "d", "e", "f"],
                    ["g", "h", "i", "j", "k", "l"],
                    ["m", "n", "o", "p", "q", "r"],
                    ["s", "t", "u", "v", "w", "x"],
                    ["y", "z", "0", "1", "2", "3"],
                    ["4", "5", "6", "7", "8", "9"],
                ])
                numpy.random.shuffle(array)
                roll_one_block = array[roll_two, roll_three]
                list.append(roll_one_block)

            if roll_one == 3 or roll_one == 4:
                array = numpy.array([
                    ["A", "B", "C", "D", "E", "F"],
                    ["G", "H", "I", "J", "K", "L"],
                    ["M", "N", "O", "P", "Q", "R"],
                    ["S", "T", "U", "V", "W", "X"],
                    ["Y", "Z", "0", "1", "2", "3"],
                    ["4", "5", "6", "7", "8", "9"],
                ])
                numpy.random.shuffle(array)
                roll_two_block = array[roll_two, roll_three]
                list.append(roll_two_block)

            if roll_one == 5 or roll_one == 6:
                array = numpy.array([
                    ["0", "1", "2", "3", "4", "5"],
                    ["6", "7", "8", "9", "!", "#"],
                    ["$", "%", "&", "(", ")", "*"],
                    ["+", ",", "-", ".", "/", ":"],
                    [";", "<", "=", ">", "?", "@"],
                    ["[", "]", "^", "_", "{", "}"],
                ])
                numpy.random.shuffle(array)
                roll_three_block = array[roll_two, roll_three]
                list.append(roll_three_block)

    list2string = "".join(list)
    print("PASSWORD: " + Fore.GREEN + list2string + Style.RESET_ALL)

def entropy_calc(password_length):
	if args.e:
		global entropy
		entropy = password_length * 6.45943161863729725626
		print("ENTROPY: "+ Fore.RED + str(entropy) + Style.RESET_ALL)

def level_password(password_length):
	if args.l:
	    global level
	    entropy = password_length * 6.45943161863729725626
	    if entropy > 256:
	    	level = "MADARA UCHIHA"
	    elif entropy > 128:
	        level = "KAGE"
	    elif entropy > 60:
	        level = "JONIN"
	    elif entropy > 36:
	        level = "CHUNIN"
	    else:
	        level = "GENIN"
	    print("LEVEL: "+ Fore.MAGENTA + level + Style.RESET_ALL)


def password_strength():
	if args.c:
	    if (bool(re.match("((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!#$%&()*+,-.:;<=>?@^_{}]))", list2string))==True):
	        print("COMBINATION: "+ Fore.CYAN + "lowercase, uppercase, numbers and symbols" + Style.RESET_ALL)
	    elif (bool(re.match("(([a-z]*)([A-Z]*)([0-9]*)([!#$%&()*+,-.:;<=>?@^_{}]*))", list2string))==True):
	    	print("COMBINATION: "+ Back.RED +"SOME POOL CHARACTERS ARE MISSING!" + Style.RESET_ALL)

def main(): 
    generate_password(args.N)
    entropy_calc(args.N)
    level_password(args.N)
    password_strength()

if __name__ == '__main__':
    main()