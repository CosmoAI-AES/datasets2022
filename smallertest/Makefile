all: train.csv test.csv

PD=$(HOME)/git/cosmoai/CosmoSim/Scripts/
BD=$(HOME)/git/cosmoai/CosmoSim/bin/

export PATH := $(PD):$(BD):$(PATH)

images: train.csv test.csv
	sh $(PD)/datagen.sh < train.csv
	sh $(PD)/datagen.sh < test.csv

train.csv: smaller-sphere-pm.csv
	head -701 $< > $@

test.csv: smaller-sphere-pm.csv
	head -1 $< > $@
	tail -300 $< >> $@
