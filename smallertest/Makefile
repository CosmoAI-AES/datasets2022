all: train.csv test.csv

PD=$(HOME)/git/cosmoai/CosmoSim/Scripts/
BD=$(HOME)/git/cosmoai/CosmoSim/bin/
ML=$(HOME)/git/cosmoai/CosmoML/src/

export PATH := $(PD):$(BD):$(PATH)

images: .images

.images: train.csv test.csv
	sh $(PD)/datagen.sh -Z 400 < train.csv
	sh $(PD)/datagen.sh -Z 400 < test.csv
	touch $@

train.csv: smaller-sphere-pm.csv
	head -641 $< > $@

test.csv: smaller-sphere-pm.csv
	head -1 $< > $@
	tail -200 $< >> $@

ml: .images
	python3 $(ML)/MLSystem.py

smaller-sphere-pm.csv: smaller-sphere-pm.py
	python3 $<

clean:
	rm -f *.png *.csv
