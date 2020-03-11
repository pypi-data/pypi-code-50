import argparse, random, textwrap
import sys
import rstr

upperalpha    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
loweralpha    = 'abcdefghijklmnopqrstuvwxyz'
digit         = '0123456789'
keyboard_punc = '~`!@#$%^&*()_+-={}|[]\\:";\'<>?,./'

parser = argparse.ArgumentParser(
  description = 'shell wrapper for rstr (https://pypi.org/project/rstr/)', 
  prog = 'python -m crstr'
  )

parser.add_argument(
  '--version', 
  action = 'version', 
  version = '%(prog)s 1.0'
  )

parser.add_argument(
  '-l', '--length', 
  dest = 'strlength', 
  default = random.randint(1, 255), 
  metavar = 'strlength', 
  type = int, 
  help = 'The length of the output string', 
  action = 'store'
  )

charset_parser = parser.add_mutually_exclusive_group()

charset_parser.add_argument(
  '-B', '--64', '--base64', 
  dest = 'charset', 
  help = 'use base64 charset', 
  action = 'store_const', 
  const = upperalpha + loweralpha + digit + '+/', 
  )
charset_parser.add_argument(
  '-x', '--16', '--hexadecimal', 
  dest = 'charset', 
  help = 'use lower-case hexadecimal charset', 
  action = 'store_const', 
  const = digit + loweralpha[0 : 6], 
  )
charset_parser.add_argument(
  '-X', '--16U', '--HEXADECIMAL', 
  dest = 'charset', 
  help = 'use upper-case hexadecimal charset', 
  action = 'store_const', 
  const = digit + upperalpha[0 : 6], 
  )
charset_parser.add_argument(
  '-o', '--8', '--octal', 
  dest = 'charset', 
  help = 'use octal charset', 
  action = 'store_const', 
  const = digit[0 : 8], 
  )
charset_parser.add_argument(
  '-b', '--2', '--binary', 
  dest = 'charset', 
  help = 'use binary charset',
  action = 'store_const', 
  const = '01', 
  )
charset_parser.add_argument(
  '-d', '--10', '--decimal', 
  dest = 'charset', 
  help = 'use decimal charset', 
  action = 'store_const', 
  const = digit, 
  )
charset_parser.add_argument(
  '-a', '--alpha', 
  dest = 'charset', 
  help = 'use alphabet (both upper-case & lower-case) charset', 
  action = 'store_const', 
  const = upperalpha + loweralpha, 
  )
charset_parser.add_argument(
  '-A', '--ALPHA', 
  dest = 'charset', 
  help = 'use upper-case alphabet charset', 
  action = 'store_const', 
  const = upperalpha, 
  )
charset_parser.add_argument(
  '--lower-case', 
  dest = 'charset', 
  help = 'use lower-case alphabet charset', 
  action = 'store_const', 
  const = loweralpha, 
  )
charset_parser.add_argument(
  '-w', '--word', 
  dest = 'charset', 
  help = 'use word charset (alphabet & number)', 
  action = 'store_const', 
  const = digit + upperalpha + loweralpha, 
  )
charset_parser.add_argument(
  '--lower-word', 
  dest = 'charset', 
  help = 'use lower-case word charset', 
  action = 'store_const', 
  const = digit + loweralpha, 
  )
charset_parser.add_argument(
  '--upper-word', 
  dest = 'charset', 
  help = 'use upper-case word charset', 
  action = 'store_const', 
  const = digit + upperalpha, 
  )
charset_parser.add_argument(
  '-c', '--charset',
  dest = 'charset', 
  metavar = 'charset', 
  help = 'use customized charset', 
  action = 'store' 
  )

regex_parser = parser.add_mutually_exclusive_group()
# BUG: rstr will encounter an error when attempting to generate a random string
# longer than 101 characters using regex

regex_parser.add_argument(
  '-v', '--variable', 
  dest = 'regex', 
  help = 'generate python variable-name-allowed string', 
  action = 'store_const', 
  const = r'[a-zA-Z](\w|_){$-1len$}', 
  )
regex_parser.add_argument(
  '-p', '--package', 
  dest = 'regex', 
  help = 'generate common package-name-styled string', 
  action = 'store_const', 
  const = r'[a-zA-Z]([a-zA-Z]|\d|-){$-1len$}', 
  )
regex_parser.add_argument(
  '-r', '--regex',
  dest = 'regex', 
  metavar = 'regex', 
  help = 'use customized regex', 
  action = 'store' 
  )

args = parser.parse_args()

if hasattr(args, 'charset') and args.charset != None:
  if hasattr(args, 'regex') and args.regex != None:
    print(textwrap.dedent('''\
      Illegal syntax: duplicate rule
      '''), file = sys.stderr)
    parser.print_usage()
    exit(2)
  print(rstr.rstr(args.charset, int(args.strlength)))

elif hasattr(args, 'regex') and args.regex != None:
  if hasattr(args, 'charset') and args.charset != None:
    print(textwrap.dedent('''\
      Illegal syntax: duplicate rule
      '''), file = sys.stderr)
    parser.print_usage()
    exit(2)
  print('charset: {}'.format(args.charset))
  print('regex: {}'.format(args.regex))
  print(
    rstr.xeger(
      args.regex.replace(r'$-1len$', str(args.strlength - 1))
      )
    )

else:
  print(textwrap.dedent('''\
    Illegal syntax: a rule is required
    '''), file = sys.stderr)
  parser.print_usage()
  exit(2)
