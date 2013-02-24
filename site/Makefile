SHARED_LAYOUT := /theme/templates/layout.html
GLOBAL_LAYOUT := _global/theme/layout.html

LAYOUT_FILES := $(addsuffix $(SHARED_LAYOUT), cubes brewery blog)

layout: $(LAYOUT_FILES)

$(LAYOUT_FILES): $(GLOBAL_LAYOUT)
	@echo Copying layout file $@
	@cp $< $@



