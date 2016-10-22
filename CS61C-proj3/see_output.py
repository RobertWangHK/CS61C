# Credit: This script was developed by a student in CS61C Fall 2015 and adapted for use in this project

import subprocess, sys
def do():
    print subprocess.check_output('python2.7 assembler.py %s' % sys.argv[1], shell=True)
    hex_data = [instr[:-1] for instr in open(sys.argv[1][:-2]+".hex").readlines()[1:]]
    temp_circuit = open('temp.circ', 'w')
    temp_circuit.write(circuit0)
    temp_circuit.write(" ".join(hex_data) + "\n")
    temp_circuit.write(circuit1)
    temp_circuit.close()
    output = subprocess.check_output("java -jar tests/logisim.jar temp.circ -tty table", shell=True)[-360:]
    output = output.replace(" ", "")
    output = output.replace("\t", "")
    output = output.replace("\n", "")
    regs = ['s0', 's1', 's2', 'ra', 'sp']
    vals = {}
    output = output[32:]
    for reg in regs:
        temp, output = output[:32], output[32:]
        vals[reg] = temp

    for reg in regs:
        printVal = None
        if vals[reg]=='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx':
            printVal = 'x'
        else:
            printVal = int(vals[reg], 2)
        print("%s: %s %s" % (reg, vals[reg], printVal))
    #print output
    #print int(s0, 2)
circuit0 = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="2.7.1" version="1.0">
This file is intended to be loaded by Logisim (http://www.cburch.com/logisim/).
<lib desc="#Wiring" name="0">
    <tool name="Splitter">
      <a name="fanout" val="1"/>
      <a name="incoming" val="32"/>
      <a name="appear" val="center"/>
      <a name="bit0" val="none"/>
      <a name="bit1" val="none"/>
      <a name="bit2" val="0"/>
      <a name="bit3" val="0"/>
      <a name="bit4" val="0"/>
      <a name="bit5" val="0"/>
      <a name="bit6" val="0"/>
      <a name="bit7" val="0"/>
      <a name="bit8" val="0"/>
      <a name="bit9" val="0"/>
      <a name="bit10" val="0"/>
      <a name="bit11" val="0"/>
      <a name="bit12" val="0"/>
      <a name="bit13" val="0"/>
      <a name="bit14" val="0"/>
      <a name="bit15" val="0"/>
      <a name="bit16" val="0"/>
      <a name="bit17" val="0"/>
      <a name="bit18" val="0"/>
      <a name="bit19" val="0"/>
      <a name="bit20" val="0"/>
      <a name="bit21" val="0"/>
      <a name="bit22" val="0"/>
      <a name="bit23" val="0"/>
      <a name="bit24" val="0"/>
      <a name="bit25" val="0"/>
      <a name="bit26" val="none"/>
      <a name="bit27" val="none"/>
      <a name="bit28" val="none"/>
      <a name="bit29" val="none"/>
      <a name="bit30" val="none"/>
      <a name="bit31" val="none"/>
    </tool>
    <tool name="Pin">
      <a name="facing" val="north"/>
    </tool>
    <tool name="Probe">
      <a name="radix" val="16"/>
    </tool>
    <tool name="Tunnel">
      <a name="facing" val="north"/>
      <a name="label" val="clk"/>
    </tool>
    <tool name="Pull Resistor">
      <a name="facing" val="north"/>
    </tool>
    <tool name="Clock">
      <a name="facing" val="north"/>
    </tool>
    <tool name="Constant">
      <a name="facing" val="north"/>
    </tool>
    <tool name="Bit Extender">
      <a name="in_width" val="32"/>
      <a name="out_width" val="8"/>
    </tool>
  </lib>
  <lib desc="#Gates" name="1">
    <tool name="NOT Gate">
      <a name="facing" val="south"/>
    </tool>
    <tool name="Buffer">
      <a name="width" val="3"/>
    </tool>
    <tool name="AND Gate">
      <a name="width" val="16"/>
      <a name="inputs" val="2"/>
    </tool>
    <tool name="OR Gate">
      <a name="inputs" val="2"/>
    </tool>
    <tool name="NAND Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </tool>
    <tool name="NOR Gate">
      <a name="inputs" val="2"/>
    </tool>
    <tool name="XOR Gate">
      <a name="inputs" val="2"/>
    </tool>
    <tool name="XNOR Gate">
      <a name="size" val="30"/>
      <a name="inputs" val="2"/>
    </tool>
    <tool name="Odd Parity">
      <a name="facing" val="south"/>
      <a name="inputs" val="3"/>
    </tool>
    <tool name="Controlled Inverter">
      <a name="size" val="20"/>
    </tool>
  </lib>
  <lib desc="#Plexers" name="2">
    <tool name="Multiplexer">
      <a name="width" val="32"/>
    </tool>
    <tool name="Demultiplexer">
      <a name="select" val="5"/>
    </tool>
    <tool name="Decoder">
      <a name="enable" val="false"/>
    </tool>
    <tool name="BitSelector">
      <a name="width" val="32"/>
      <a name="group" val="8"/>
    </tool>
  </lib>
  <lib desc="#Arithmetic" name="3">
    <tool name="Adder">
      <a name="width" val="16"/>
    </tool>
    <tool name="Subtractor">
      <a name="width" val="16"/>
    </tool>
    <tool name="Multiplier">
      <a name="width" val="1"/>
    </tool>
    <tool name="Divider">
      <a name="width" val="16"/>
    </tool>
    <tool name="Negator">
      <a name="width" val="1"/>
    </tool>
    <tool name="Comparator">
      <a name="width" val="16"/>
    </tool>
    <tool name="Shifter">
      <a name="width" val="32"/>
    </tool>
  </lib>
  <lib desc="#Memory" name="4">
    <tool name="Register">
      <a name="width" val="32"/>
    </tool>
    <tool name="Counter">
      <a name="width" val="32"/>
      <a name="max" val="0xffffffff"/>
    </tool>
    <tool name="RAM">
      <a name="addrWidth" val="24"/>
      <a name="dataWidth" val="32"/>
    </tool>
    <tool name="ROM">
      <a name="contents">addr/data: 8 8
0
</a>
    </tool>
  </lib>
  <lib desc="#I/O" name="5"/>
  <lib desc="#Base" name="6">
    <tool name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
  </lib>
  <lib desc="file#cpu.circ" name="7"/>
  <main name="main"/>
  <options>
    <a name="gateUndefined" val="ignore"/>
    <a name="simlimit" val="1000"/>
    <a name="simrand" val="0"/>
  </options>
  <mappings>
    <tool lib="6" map="Button2" name="Menu Tool"/>
    <tool lib="6" map="Ctrl Button1" name="Menu Tool"/>
    <tool lib="6" map="Button3" name="Menu Tool"/>
  </mappings>
  <toolbar>
    <tool lib="6" name="Poke Tool"/>
    <tool lib="6" name="Edit Tool"/>
    <tool lib="6" name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
    <sep/>
    <tool lib="0" name="Pin">
      <a name="tristate" val="false"/>
    </tool>
    <tool lib="0" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="labelloc" val="east"/>
    </tool>
    <tool lib="1" name="NOT Gate"/>
    <tool lib="1" name="AND Gate"/>
    <tool lib="1" name="OR Gate"/>
  </toolbar>
  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>
    <wire from="(160,380)" to="(260,380)"/>
    <wire from="(250,140)" to="(340,140)"/>
    <wire from="(570,350)" to="(600,350)"/>
    <wire from="(860,250)" to="(890,250)"/>
    <wire from="(240,130)" to="(240,180)"/>
    <wire from="(160,250)" to="(230,250)"/>
    <wire from="(230,230)" to="(230,250)"/>
    <wire from="(250,100)" to="(250,130)"/>
    <wire from="(240,130)" to="(250,130)"/>
    <wire from="(570,250)" to="(580,250)"/>
    <wire from="(820,350)" to="(820,430)"/>
    <wire from="(160,380)" to="(160,390)"/>
    <wire from="(340,100)" to="(340,140)"/>
    <wire from="(820,450)" to="(850,450)"/>
    <wire from="(260,150)" to="(260,180)"/>
    <wire from="(860,350)" to="(880,350)"/>
    <wire from="(890,440)" to="(910,440)"/>
    <wire from="(160,250)" to="(160,380)"/>
    <wire from="(250,140)" to="(250,180)"/>
    <wire from="(280,210)" to="(300,210)"/>
    <wire from="(70,160)" to="(220,160)"/>
    <wire from="(820,350)" to="(860,350)"/>
    <wire from="(820,430)" to="(850,430)"/>
    <wire from="(800,350)" to="(820,350)"/>
    <wire from="(260,150)" to="(430,150)"/>
    <wire from="(230,150)" to="(230,180)"/>
    <wire from="(280,350)" to="(320,350)"/>
    <wire from="(780,250)" to="(860,250)"/>
    <wire from="(600,250)" to="(640,250)"/>
    <wire from="(70,100)" to="(70,160)"/>
    <wire from="(560,250)" to="(570,250)"/>
    <wire from="(570,250)" to="(570,350)"/>
    <wire from="(260,370)" to="(260,380)"/>
    <wire from="(160,100)" to="(160,150)"/>
    <wire from="(160,150)" to="(230,150)"/>
    <wire from="(430,100)" to="(430,150)"/>
    <wire from="(860,250)" to="(860,350)"/>
    <wire from="(190,210)" to="(210,210)"/>
    <wire from="(220,160)" to="(220,180)"/>
    <wire from="(550,350)" to="(570,350)"/>
    <comp lib="0" loc="(430,100)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="$sp Value"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(280,350)" name="Counter">
      <a name="width" val="32"/>
      <a name="max" val="0xffffffff"/>
    </comp>
    <comp lib="6" loc="(268,272)" name="Text">
      <a name="text" val="YOUR CPU SHOULD FIT IN HERE!"/>
    </comp>
    <comp lib="0" loc="(160,390)" name="Clock">
      <a name="facing" val="north"/>
    </comp>
    <comp lib="0" loc="(560,250)" name="Tunnel">
      <a name="facing" val="east"/>
      <a name="width" val="32"/>
      <a name="label" val="fetch_addr"/>
    </comp>
    <comp lib="0" loc="(70,100)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="$sp Value"/>
      <a name="labelloc" val="north"/>
    </comp>

    <comp lib="0" loc="(600,350)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="Requested Address"/>
      <a name="labelloc" val="south"/>
    </comp>
    <comp lib="0" loc="(890,250)" name="Tunnel">
      <a name="width" val="32"/>
      <a name="label" val="Instruction"/>
    </comp>
    <comp lib="0" loc="(160,100)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="$s1 Value"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(190,210)" name="Tunnel">
      <a name="facing" val="east"/>
      <a name="width" val="32"/>
      <a name="label" val="Instruction"/>
    </comp>

    <comp lib="0" loc="(820,450)" name="Constant">
      <a name="width" val="32"/>
      <a name="value" val="0x0"/>
    </comp>
    <comp lib="0" loc="(880,350)" name="Probe">
      <a name="facing" val="west"/>
      <a name="radix" val="16"/>
    </comp>
    <comp lib="0" loc="(910,440)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="label" val="halt"/>
      <a name="labelloc" val="east"/>
    </comp>
    <comp lib="7" loc="(280,210)" name="main"/>
    <comp lib="6" loc="(466,459)" name="Text">
      <a name="text" val="There should be no blue/red wires here, and the outputs shouldn't be x's."/>
    </comp>
    <comp lib="6" loc="(710,202)" name="Text">
      <a name="text" val="Instruction Memory"/>
      <a name="font" val="SansSerif bold 12"/>
    </comp>

    <comp lib="3" loc="(890,440)" name="Comparator">
      <a name="width" val="32"/>
      <a name="mode" val="unsigned"/>
    </comp>
    <comp lib="0" loc="(250,100)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="$s2 Value"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="0" loc="(800,350)" name="Pin">
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="Requested Instruction"/>
      <a name="labelloc" val="south"/>
    </comp>
    <comp lib="0" loc="(320,350)" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="Time Step"/>
      <a name="labelloc" val="south"/>
    </comp>
    <comp lib="0" loc="(340,100)" name="Pin">
      <a name="facing" val="south"/>
      <a name="output" val="true"/>
      <a name="width" val="32"/>
      <a name="label" val="$ra Value"/>
      <a name="labelloc" val="north"/>
    </comp>
    <comp lib="4" loc="(780,250)" name="ROM">
      <a name="addrWidth" val="24"/>
      <a name="dataWidth" val="32"/>
      <a name="contents">addr/data: 24 32
"""
circuit1 = """</a>
    </comp>
    <comp lib="0" loc="(550,350)" name="Probe">
      <a name="radix" val="16"/>
    </comp>
    <comp lib="0" loc="(580,250)" name="Splitter">
      <a name="fanout" val="1"/>
      <a name="incoming" val="32"/>
      <a name="appear" val="center"/>
      <a name="bit0" val="none"/>
      <a name="bit1" val="none"/>
      <a name="bit2" val="0"/>
      <a name="bit3" val="0"/>
      <a name="bit4" val="0"/>
      <a name="bit5" val="0"/>
      <a name="bit6" val="0"/>
      <a name="bit7" val="0"/>
      <a name="bit8" val="0"/>
      <a name="bit9" val="0"/>
      <a name="bit10" val="0"/>
      <a name="bit11" val="0"/>
      <a name="bit12" val="0"/>
      <a name="bit13" val="0"/>
      <a name="bit14" val="0"/>
      <a name="bit15" val="0"/>
      <a name="bit16" val="0"/>
      <a name="bit17" val="0"/>
      <a name="bit18" val="0"/>
      <a name="bit19" val="0"/>
      <a name="bit20" val="0"/>
      <a name="bit21" val="0"/>
      <a name="bit22" val="0"/>
      <a name="bit23" val="0"/>
      <a name="bit24" val="0"/>
      <a name="bit25" val="0"/>
      <a name="bit26" val="none"/>
      <a name="bit27" val="none"/>
      <a name="bit28" val="none"/>
      <a name="bit29" val="none"/>
      <a name="bit30" val="none"/>
      <a name="bit31" val="none"/>
    </comp>
    <comp lib="0" loc="(300,210)" name="Tunnel">
      <a name="width" val="32"/>
      <a name="label" val="fetch_addr"/>
    </comp>
  </circuit>
</project>


"""
do()
