import array
import os
import sys,getopt
print(os.getcwd())
def test(inputfile,outputfile):
    a =""
    with open(os.path.join(os.getcwd(),inputfile)) as f:
        newcells = array.array('i', []) 
        for line in f:
            cells = line.split(',')
            for word in cells:
                if word != "\n" and word != "":
                    newcells.append(int(word.lower(),16))
        #print(len(newcells))
        for i in range(0,len(newcells)):
            #print(newcells[i])
            if i % 3 == 0:
                a += hex(newcells[i])
            elif (i+1) % 3 == 0:
                a += hex(newcells[i]).replace("0x","")+",\n"
            else:
                a += hex(newcells[i]).replace("0x","")
        print(a)
        f.close()
    with open(os.path.join(os.getcwd(),outputfile), "w") as f: 
        f.write(a)
        f.close()

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   test(inputfile,outputfile)
   print('Input file is :'+inputfile)
   print('Output file is :'+outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
