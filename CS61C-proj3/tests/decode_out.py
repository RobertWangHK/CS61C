import csv
import sys

def bin2hex(s):
    b = ''.join(s.split(' '))
    n = int((len(b) - 1) / 4) + 1
    if 'x' in b:
        return 'x' * n
    return "{:x}".format(int(b, 2)).zfill(n)

def print_usage():
    print("Usage: {} <alu|regfile|cpu>".format(sys.argv[0]))
    print()
    print("\tTakes the logisim output on standard input and writes decoded version to standard output.")
    print("\tThe first argument states what circuit produced the input.")
    sys.exit(-1)

def main():
    if len(sys.argv) < 2:
        print_usage()

    typ = sys.argv[1]
    rdr = csv.reader(sys.stdin, delimiter='\t')
    wtr = csv.writer(sys.stdout, delimiter='\t')

    if typ == 'alu':
        wtr.writerow(["Test #", "OF", "Eq", "Result"])
    elif 'regfile':
        wtr.writerow(["Test #", "$s0 Value", "$s1 Value", "$s2 Value", "$ra Value", "$sp Value", "Read Data 1", "Read Data 2"])
    elif typ == 'cpu':
        wtr.writerow(['$s0 Value', '$s1 Value', '$s2 Value', '$ra Value', '$sp Value', 'Time Step', 'Fetch Addr', 'Instruction'])
    else:
        print_usage()

    for row in rdr:
        wtr.writerow([bin2hex(b) for b in row])

main()
