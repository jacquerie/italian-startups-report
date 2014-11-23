URL = 'http://startup.registroimprese.it/report/startup.zip'
FILES = startup.xls startup.zip

all: report

clean:
	rm -f $(FILES)

report: report.py

report.py: startup.xls
	@python $@

startup.xls: startup.zip
	unzip $<
	touch $@

startup.zip:
	curl -o $@ $(URL)

.PHONY: all clean report report.py

