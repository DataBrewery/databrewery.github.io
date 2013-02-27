PROJECTS := cubes brewery blog

.PHONY: all $(PROJECTS)

all: $(PROJECTS)

$(PROJECTS):
	@echo Creating content for $@... ; \
	cd $@ ; \
	pelican content -s pelicanconf.py

