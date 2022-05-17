BUILD := dist/
TARGET := ../docs

build: $(BUILD)

$(BUILD):
	npm run-script build
	rsync -a $(BUILD) $(TARGET)

.PHONY: clean
clean:
	rm -r $(BUILD)