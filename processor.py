import json

class Processor:
    def __init__(self, data):
        self.data = data

    def process(self):
        return self._filter_and_transform(self.data)

    def _filter_and_transform(self, data):
        return [self._transform(item) for item in data if self._is_valid(item)]

    def _transform(self, item):
        return {k: v for k, v in item.items() if k != 'unnecessary_field'}

    def _is_valid(self, item):
        return isinstance(item, dict) and 'required_field' in item

    def to_json(self, processed_data):
        return json.dumps(processed_data)

if __name__ == '__main__':
    data = [
        {'required_field': 1, 'unnecessary_field': 2},
        {'required_field': 3},
        {'invalid_field': 4}
    ]
    processor = Processor(data)
    result = processor.process()
    print(processor.to_json(result))