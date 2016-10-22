  addiu $s0 $0 1
  addiu $s1 $0 2
  jal change_ra
  j dummy
  
change_ra:
  add $s2 $s0 $s1
  jr $ra

dummy: add $t0 $t0 $0
