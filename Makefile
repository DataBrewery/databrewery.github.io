PROJECTS := cubes brewery blog
HOME := home
BUILD_PATH := _build

CONF_LOCAL := pelicanconf.py
CONF_PUBLISH := publishconf.py

#########################################################

-include Makefile.local

ALL_TARGETS := $(PROJECTS) $(HOME)
PUBLISH_TARGETS := $(addprefix publish_, $(PROJECTS))
CONFIG := $(CONF_LOCAL)

.PHONY: all $(PROJECTS) $(HOME)

all: $(PROJECTS) home
build: CONFIG := $(CONF_PUBLISH)
build: MSG := "final "
build: $(PROJECTS) home

publish: build rsync

$(PROJECTS):
	@echo Creating $(MSG)content for $@... ; \
	cd $@ ; \
	pelican content -s $(CONFIG)

rsync: check-publish-target
	@echo Publishing... ; \
	for target in $(PROJECTS) ; do \
		echo Syncing $$target ; \
		rsync -r $(BUILD_PATH)/$$target/ $(PUBLISH_TARGET)/$$target ; \
	done ; \
	echo Syncing home... ; \
	rsync -r $(BUILD_PATH)/$(HOME)/ $(PUBLISH_TARGET)

check-publish-target:
ifndef PUBLISH_TARGET
	$(error PUBLISH_TARGET is undefined. You can add it to Makefile.local)
endif

