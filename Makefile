URL = 'http://startup.registroimprese.it/report/startup.zip'
FILES = startup.xls startup.zip

all: startup.py

clean:
	rm -f $(FILES)

startup.py: startup.xls
	python $@

startup.xls: startup.zip
	unzip $<
	touch $@

startup.zip:
	curl -o $@ $(URL)

.PHONY: all clean startup.py

