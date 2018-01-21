from pass_one import optab,LOCCTR,start,sym
length = hex(int(LOCCTR,16)-int(start,16))

objpgm = open("ObjectProgram.txt","w")	
inter = open("Intermediatefile.txt","r")
symtab = open("SymbolTab.txt","r")
l = []

addrlist = []
for i in inter.readlines():
	ls= i.strip().split()
	add = ls[0][2:]
	if add!="-":
		addrlist.append(add)
	label = ls[1]
	opcode = ls[2]
	if len(ls)==4:
		operand = ls[3]
	if ls[2]=="START":
		objpgm.write("H^"+label+"^00"+start+"^00"+length[2:]+"\n")
	elif ls[2]=="END":
		tempstr = "\nE^00"+start
	else:
		if ls[2] in optab.keys():
			
				
			#op = str(bin(int(optab[ls[2]],16)))
			op = optab[ls[2]]
			if ls[2]=="RSUB":
				op +="0000"
			elif operand in sym.keys():
				op += sym[operand][2:]
			l.append(op)
		elif ls[2]=="WORD":
			op = hex(int(operand))
			op1 = str(op)
			op1 = op1[2:]
			if len(op1)<6:
				for i in range(6-len(op1)):
					op1 = "0"+op1
			
			l.append(op1)
		elif ls[2]=="BYTE":
			temp = operand[2:len(operand)-1]
			if operand.find("X"):
				l.append(temp)
			elif operand.find("X"):
				str = null
				for i in temp:
					hexcode = hex(ord(i))
					tmp = str(hexcode)
					str +=tmp[2:]
				l.append(str)
		else:
			l.append("-")
			
i = 0

while i<len(l):
	if i==0:
		STRT = addrlist[1]
	else:
		STRT = addrlist[i]
	cnt = 0
	if i<len(l) and l[i]!="-":
		objpgm.write("\nT^00"+STRT+"^")
		last_pas = objpgm.tell()
		objpgm.write("  ^")
	while i<len(l) and l[i]!="-" and cnt<10 :
		objpgm.write(l[i])
		cnt +=1
		i+=1
	objpgm.seek(last_pas)
	tempaddr = str(hex(int(addrlist[i],16)-int(STRT,16)))
	straddr = tempaddr[2:4]
	objpgm.write(straddr)
	objpgm.seek(0,2)
	
	i+=1
objpgm.write(tempstr)
objpgm.close()
inter.close()
symtab.close()
		
					
					
					
	

			
	
	



		
		
			
			
			
			
