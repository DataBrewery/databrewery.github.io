SHARED_LAYOUT := /theme/templates/layout.html
GLOBAL_LAYOUT := _global/theme/layout.html
PROJECTS := cubes brewery blog

.PHONY: all $(PROJECTS)

LAYOUT_FILES := $(addsuffix $(SHARED_LAYOUT), $(PROJECTS))

all: layout $(PROJECTS)

layout: $(LAYOUT_FILES)

$(LAYOUT_FILES): $(GLOBAL_LAYOUT)
	@echo Copying layout file $@
	@cp $< $@

content:
	for project in $(PROJECTS); do \
		pushd . ; \
		cd $(project) ; \
		echo making $(project) ; \
		pwd ; \
		popd ; \
	done

$(PROJECTS):
	@echo Creating content for $@... ; \
	cd $@ ; \
	pelican content -s pelicanconf.py

