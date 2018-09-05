TAG = 0.1.0
NAME = $(shell basename `pwd`)

REPO = krausm/$(shell basename `pwd`)
IMAGE=$(REPO):$(TAG)

.PHONY: echo build run run_shell

echo:
	echo $(IMAGE)

build:
	docker build -t $(IMAGE) .
	docker images | grep '$(REPO)'

push:
	docker push $(IMAGE)

run:
	-docker run -it --rm -p 9104:9104 --name $(NAME) $(IMAGE)

run_shell:
	-docker run -it --rm -p 9104:9104 --name $(NAME) --entrypoint /bin/sh $(IMAGE)
