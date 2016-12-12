default: demo

demo:
	@python ./main.py

check:
	@python -m tests.test_list_compare -vv
	@python -m tests.test_social_analysis -vv

.PHONY: default demo check
