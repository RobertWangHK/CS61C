p1:
	cp alu.circ regfile.circ tests
	cd tests && python ./sanity_test.py p1 | tee ../TEST_LOG

p2:
	cp alu.circ regfile.circ mem.circ cpu.circ tests
	cd tests && python ./sanity_test.py p2 | tee ../TEST_LOG
