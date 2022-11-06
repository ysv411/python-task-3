import sys
import argparse

# Write a utility for generating passwords according to a given template that supports the CLI interface
# and logging (-vvv – show detailed information during processing)

# Rules of template:
# - Each token of template are separate symbol ‘%’.
# - Tokens consist of two part <type_token> and <count>, A10.

# List of type tokens:
# Type of Token			Desctiption
# a						small lateral ASCII
# A						big lateral ASCII
# d						digit
# p						Punctuations
# -						- (same symbol)
# @						@ (same symbol)
# []					set type of token
# count					number of symbols
# Example:
# A4%d3%-%a2% => DHRF345-st
# A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd

# CLI interface can support next commands:
#- l: Set length of password and generate random password from set {small lateral ASCII, big lateral ASCII, digit}
# - t: Set template for generate passwords
# - f: Getting list of patterns from file and generate for each random password
# - c: number of passwords
# -vvv: Verbose mode (-v |-vv |-vvv )
# -h: help

# Output: supports pipe redirect

"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
					help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

print(sys.argv)	# prints list of arguments passed to scripts
				# [0] = name of script, [1] - first argument, etc
				# args = type of Str, numbers must be converted to Int

a=sys.argv[1]
print(a)
b=sys.argv[2]
print(b)
"""

ps = argparse.ArgumentParser()
# ps.add_argument("test")

# Positional argument
ps.add_argument("a", type=int, help='First argument')
ps.add_argument("b", type=int, help='Second argument')

# Optional(named) argument
ps.add_argument("-a", "--action", help='What to do with numbers', required=True, default='summa')
# action='store_const', const='10'
# action='store_true' | 'store_false'
# nargs=2		# = number of args
# choises=['1', '2', '3']

args = ps.parse_args()
print(args)

def summa(a,b):
	print(a+b)

def minus(a,b):
	print(a-b)

if args.action == 'summa':
	summa(args.a, args.b)
elif args.action == 'minus':
	minus(args.a, args.b)
