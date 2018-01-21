#Opening SIC program
inp = open("SIC_input.asm","r")
#For output of PASS ONE
out = open("Intermediatefile.txt","w")
#SYMBOLTAB
symtab = open("SymbolTab.txt","w");
sym = {}
optab = {
	"ADD":"18",
	"AND":"40",
	"COMP":"28",
	"DIV":"24",
	"J":"3C",
	"JEQ":"30",
	"JGT":"34",
	"JLT":"38",
	"JSUB":"48",
	"LDA":"00",
	"LDCH":"50",
	"LDL":"08",
	"LDX":"04",
	"MUL":"20",
	"OR":"44",
	"RD":"D8",
	"RSUB":"4C",
	"STA":"0C",
	"STCH":"54",
	"STL":"14",
	"STSW":"E8",
	"STX":"10",
	"SUB":"1C",
	"TD":"E0",
	"TIX":"2C",
	"WD":"DC"}

#READING FIRST LINE
first = inp.readline()
out.write("-")
out.write("".join(first))
newl = first.strip().split()
#OUTPUT into Intermediate file
LOCCTR = newl[2]
start = LOCCTR


for i in inp.readlines():
	n = i.strip().split()
	
	if n[0]!='.':
		out.write(hex(int(LOCCTR,16)))
		out.write("".join(i))
		if n[0]!="-":
			symtab.write(n[0]+" "+hex(int(LOCCTR,16))+"\n")
			sym[n[0]] = str(hex(int(LOCCTR,16)))
		if n[1] in optab.keys() or n[1]=="WORD":
			LOCCTR = str(hex(int(LOCCTR,16)+(3)))
		elif n[1]=="RESW":
			temp = int(n[2],16)
			LOCCTR = str(hex(int(LOCCTR,16)+(temp)*3))
		elif n[1]=="RESB":
			LOCCTR = str(hex(int(LOCCTR,16)+int(n[2])))
		elif n[1]=="BYTE":
			if n[2][0]=="X":
				LOCCTR = str(hex(int(LOCCTR,16)+(len(n[2])-3)/2))
			elif n[2][0]=="C":
				LOCCTR = str(hex(int(LOCCTR,16)+(len(n[2])-3)))

				
inp.close()
out.close()
symtab.close()
			
		
	
	
