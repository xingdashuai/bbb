import yaml

with open("./value2.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("data:{}".format(data))
    # print("类型:{}".format(type(data.get("value13"))))
    # print("类型:{}".format(type(data.get("value24"))))
