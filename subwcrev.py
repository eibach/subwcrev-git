import argparse
import subprocess
import sys
import re

parser = argparse.ArgumentParser(description='Analyze batch files.')
parser.add_argument('workdir',
				   help='the workdir to analye')
parser.add_argument('src',
				   help='the source file')
parser.add_argument('dest',
				   help='the destination file')

args = parser.parse_args()

try:
#	label = subprocess.check_output("git -C " + args.workdir + " describe --always", shell=True).decode().strip()
	label = subprocess.check_output("git -C " + args.workdir + " rev-parse --short HEAD", shell=True).decode().strip()
	revision = subprocess.check_output("git -C " + args.workdir + " svn find-rev " + label, shell=True).decode().strip()
	print("Hash: " + label + " Revision: " + revision)
	with open(args.src, "r") as src, open(args.dest, "w") as dest:
		for line in src:
			dest.write(re.sub("\$WCREV\$", label, line))

except Exception as e:
	print(e)
	print("Falling back to original subwcrev")
	cmdline = ["C:\\Program Files\\TortoiseSVN\\bin\\subwcrev_orig.exe"]
	cmdline.extend(sys.argv[1:])
	subprocess.call(cmdline, shell=True)
