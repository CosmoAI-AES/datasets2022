all: train.csv test.csv

PD=$(HOME)/git/cosmoai/CosmoSim/Scripts/
BD=$(HOME)/git/cosmoai/CosmoSim/bin/

export PATH := $PD:$BD:$PATH

images: train.csv test.csv
	python3 $PD/datasetgen.py < train.csv
	python3 $PD/datasetgen.py < test.csv

train.csv: sphere-pm.csv
	head -4001 $< > $@

test.csv: sphere-pm.csv
	head -1 $< > $@
	tail -4000 $< >> $@
