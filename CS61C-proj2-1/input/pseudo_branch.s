# I am a infinite loop
		addiu $s0, $0, 0
label1:	addiu $s0, $0, 100
		bge $s0, $0, label2

# I am a sad instruction sitting in the middle
		beq $0, $0, label1

label2:	bnez $s0, label1 
