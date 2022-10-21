all: train.csv test.csv
train.csv: sphere-pm.csv
	head -4001 $< > $@
test.csv: sphere-pm.csv
	head -1 $< > $@
	tail -4000 $< >> $@
