import json

from PythonCode.api17.test_api6_3_generate_testcase import json_travel


def test_json_travel():
    with open("demo.json") as f:
        data = json.load(f)
        print(json.dumps(json_travel(data, array=3), indent=2, ensure_ascii=False))
        print(json.dumps(json_travel(data, text=4), indent=2, ensure_ascii=False))
        print(json.dumps(json_travel(data, num=6), indent=2, ensure_ascii=False))