from pathlib import Path
ROOT = Path(__file__).parent
input_file_path = ROOT / 'git.txt'

try:
    with open(input_file_path,'r') as fin:
        content = fin.read(10) #aici poate fi read / readline = citeste primul rand sau readlines = cieste toate randurile
        print (content)
        print(len(content))

        content2 = fin.read(4)
        print (content2)
except OSError as err:
    print(err)
#else:
#    #print(type(content))
#    #print(content)
#    for i in content:
#        if i.startswith('#'):
#            print(i.strip("\n\r\t "))