default: check

check:
	python -m tests.test_list_compare -vv

.PHONY: default check
