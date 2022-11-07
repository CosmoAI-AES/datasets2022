PD=$(HOME)/git/cosmoai/CosmoSim/Scripts/
BD=$(HOME)/git/cosmoai/CosmoSim/bin/

export PATH := $PD:$BD:$PATH

all: sphere-pm.csv 
	python3 $PD/datasetgen.py < $<

train.csv: sphere-pm.csv
	head -4001 $< > $@

test.csv: sphere-pm.csv
	head -1 $< > $@
	tail -4000 $< >> $@
