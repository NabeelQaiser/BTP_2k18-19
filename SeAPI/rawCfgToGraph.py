

j_counter=1		#jump nodes
dot_str1 = ""	#string for dot file

def connect(x, y, param=""):
	global dot_str1
	if not(x==y):
		dot_str1 = dot_str1 + "\n\t" + x + " -> " + y + " "
		if(param=="if_true" or param=="while_true"):
			dot_str1 = dot_str1 + "[color=green] ;"
		elif param=="if_false" or param=="while_false":
			dot_str1 = dot_str1 + "[color=red] ;"
		else:
			dot_str1 = dot_str1 + ";"

def reshapeNodeStyle(node, shape, color):
	global dot_str1
	dot_str1 = dot_str1 + "\n\t" + node + " [shape=" + shape + ", color=" + color + "] ;"
		

def utilBracketMatcher(tokens, i):
	c = 1
	while True:
		i = i+1
		if(tokens[i]=="]"):
			c= c-1
		if(tokens[i]=="["):
			c= c+1
		if(c==0):
			return i
	

def cfgReader(tokens, s, e):
	global j_counter
	# assumming : we get string of form [---] here, strictly
	s = s+1		#start
	e = e-1		#end
	current = s
	#a = "-1"	#maintain parent
	a = set()
	#re = "-1"	#maintain return_end
	re = set()
	rs = "-1"	#maintain return_start
	while current <= e:
		#case_0
		if tokens[current]=="[":
			curr2 = utilBracketMatcher(tokens, current)
			f,l = cfgReader(tokens, current, curr2)	# returns (first, last)
			current = curr2+1
			#connecting parent
			if(len(a)>0):
				for i in a:
					connect(i, f)
			#a
			a = set(l)
			#rs
			if(rs == "-1"):
				rs = f
			#re
			re = set(l)
		#case_1
		elif tokens[current].isdigit()==True:
			#rs
			if(rs == "-1"):
				rs = tokens[current]
			#connecting parent
			if(len(a)>0):
				for i in a:
					connect(i, tokens[current])
			while current+1 <= e and tokens[current+1].isdigit()==True:
				connect(tokens[current], tokens[current+1])
				current = current+1
			current = current + 1
			#a
			a = set()
			a.add(tokens[current-1])
			#re
			re = set(a)
			#print (" rs = ", rs, " , re = ", re)
		#case_2
		elif tokens[current].split("_")[0]=="if":
			to_merge_set = set()
			# if_handling...
			temp = tokens[current].split("_")[1]        #if_condition
			#reshapeNodeStyle(temp, "diamond", "orange")
			#connecting parent
			if(len(a)>0):
				for i in a:
					connect(i, temp)
			#rs
			if(rs == "-1"):
				rs = temp
			current = current+1
			curr2 = utilBracketMatcher(tokens, current) #if_true
			f1,l1 = cfgReader(tokens, current, curr2)
			connect(temp, f1)   #---connection
			for i in l1:
				to_merge_set.add(i)
			current = curr2+1
			# elsif_handling...
			while tokens[current+1].split("_")[0]=="elsif":
				current = current + 1
				temp_i = tokens[current].split("_")[1]  # elsif_condition
				connect(temp, temp_i)  # connecting parent
				temp = temp_i  # making temp pseudo-parent
				current = current + 1
				curr2_i = utilBracketMatcher(tokens, current)  # -----elsif_true
				f_i, l_i = cfgReader(tokens, current, curr2_i)
				connect(temp_i, f_i)  # ---connection
				for i in l_i:
					to_merge_set.add(i)
				current = curr2_i + 2  # ---[ elsif_x [ y x ] ]
                            
			# else handling...
			curr2 = utilBracketMatcher(tokens, current) #else_part
			f2,l2 = cfgReader(tokens, current, curr2)
			connect(temp, f2)   #---connection
			for i in l2:
				to_merge_set.add(i)
			#print (" rs = ", rs, " , re = ", re, " , a = ", a)
			#print (" f1 = ", f1, " , l1 = ", l1, ", f2 = ", f2, ", l2 = ", l2)
			current = curr2+2	#<<---note : [ if_XX [ ][ ] ]


			# re
			re = set(to_merge_set)
			#a
			a = set(re)

			
	#return
	#print (" rs = ", rs, " , re = ", re)
	return rs,re





### main() ###
#tree = open('cfg_crude.txt').read()
tree = input()
print( "\n# our CFG string...\n\n", tree )

tree = tree.replace("  ", " ")
tree = tree.strip()
tokens = tree.split(" ")

#for i in range(0,len(tokens)):
#	print(tokens[i])

f,l = cfgReader(tokens, 0, len(tokens)-1)
dot_str1 = "\n\tstart -> " + f + ";"+ dot_str1
for i in l:
	dot_str1 = dot_str1 + "\n\t" + i + " -> exit;"
dot_str1 = "# dot file created at runtime\n"+"\ndigraph G {"+dot_str1
dot_str1 = dot_str1+"\n\n\tstart [shape=Msquare, color=green];\n\texit [shape=Msquare, color=red];\n}"
#print("\n\n", dot_str1)

'''
filename = "cprogram.dot"
file = open(filename, 'w')
file.write(dot_str1)
file.close()

call(["dot", "-Tpng", "-o", filename+".png", filename])
call(["eog", filename+".png"])

[ 1 2 3 [ if_4 [ 5 6 ] [ elsif_7 [ 8 9 ] ] [ 10 11 ] ] 12 13 ]

[ 0 1 2 3 4 5 6 7 [ if_8 [ 9 10 11 [ if_12 [ 13  ] [ elsif_14 [ 15  ] ] [ elsif_16 [ 17  ] ] [ 18  ]  ]  ]  [ 19 ]  ] 20  ]


[ 5 6 7 [ if_8 [ 9 10 11 [ if_12 [ 13  ] [ elsif_14 [ 15  ] ] [ elsif_16 [ 17  ] ] [ 18  ]  ]  ]  [ 19 [ if_20 [ 21 22 ] [ elsif_23 [ 24 25 ] ] [ 26 27 ] ] ]  ] 28 29  ]

[ 1 2 3 [ if_4 [ 5 6 ] [ elsif_7 [ 8 9 ] ] [ 10 11 ] ] [ if_12 [ 13 14 ] [ elsif_15 [ 16 17 ] ] [ 18 19 ] ] 20 21 ]

[ [ if_4 [ 5 6 ] [ elsif_7 [ 8 9 ] ] [ 10 11 ] ] 12 13 ]


[ 10 11 12 13 ]

'''
