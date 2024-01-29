def main():
    infile = open('clients.txt','r')
    number = 1
    for row in infile:
        number += 1
        print(str(number)+'.', row.rstrip('\n'))
main()