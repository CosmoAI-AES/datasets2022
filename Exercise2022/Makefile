PD=$(HOME)/git/cosmoai/CosmoSim/Scripts/
BD=$(HOME)/git/cosmoai/CosmoSim/bin/

export PATH := $(PD):$(BD):$(PATH)

all: .centred

.images: sphere-pm.csv 
	sh $(PD)/datagen.sh -Z 400 < $<
	touch $@
.centred: .images
	python3 $(PD)/centreimage.py image-*
	touch $@

sphere-pm.csv: sphere-pm.py
	python3 $<

train.csv: sphere-pm.csv
	head -4001 $< > $@

test.csv: sphere-pm.csv
	head -1 $< > $@
	tail -4000 $< >> $@
