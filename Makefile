.PHONY: all clean update update-methods check-method-doc check-photos-search-doc format typecheck test dev-init

FLICKCURL_UTILS ?= $(HOME)/dev/redland/flickcurl/utils
LIST_METHODS ?= $(FLICKCURL_UTILS)/list-methods
METHODS_NEW ?= methods.lst.new
UV ?= uv
UV_CACHE_DIR ?= /tmp/flickr-api-history-uv-cache
UV_CMD ?= UV_CACHE_DIR=$(UV_CACHE_DIR) $(UV)
PYTHON ?= $(UV_CMD) run python
CHECK_METHOD_DOC_MODULE ?= flickr_api_history.check_method_doc
METHOD_DOC ?= flickr.photos.search
METHOD_DOC_URL ?= https://www.flickr.com/services/api/$(METHOD_DOC).html
METHOD_DOC_ARCHIVE ?= archive/$(METHOD_DOC).html
METHOD_DOC_FETCHED ?= $(METHOD_DOC_ARCHIVE).new

all: methods.lst

clean:
	rm -f methods.lst $(METHODS_NEW) $(METHOD_DOC_FETCHED)

methods.lst: $(LIST_METHODS)
	$(LIST_METHODS) > $@

$(LIST_METHODS):
	cd $(FLICKCURL_UTILS) && $(MAKE) list-methods

update: update-methods

update-methods: $(LIST_METHODS)
	$(LIST_METHODS) > $(METHODS_NEW)
	diff -u methods.lst $(METHODS_NEW) || test $$? -eq 1
	mv $(METHODS_NEW) methods.lst

check-method-doc:
	@test -f $(METHOD_DOC_ARCHIVE) || { echo "Missing archived method doc: $(METHOD_DOC_ARCHIVE)" >&2; exit 2; }
	$(PYTHON) -m $(CHECK_METHOD_DOC_MODULE) --method $(METHOD_DOC) --archive $(METHOD_DOC_ARCHIVE) --url $(METHOD_DOC_URL) --fetched-output $(METHOD_DOC_FETCHED)

check-photos-search-doc:
	$(MAKE) check-method-doc METHOD_DOC=flickr.photos.search

format:
	$(PYTHON) -m black .

typecheck:
	$(PYTHON) -m mypy flickr_api_history tests

test:
	$(PYTHON) -m pytest

dev-init:
	$(UV_CMD) sync
	$(MAKE) format
	$(MAKE) typecheck
	$(MAKE) test
