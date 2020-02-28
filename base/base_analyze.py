# 导入模块
import os
import yaml


# 此处是文件路径查找方法，用于数据驱动，调用此方法可查找对应数据文件，并将其中的yaml格式转化成列表
def analyze_file(file_name, data_key):
    with open("." + os.sep + "data" + os.sep + file_name, "r",encoding="UTF-8") as f:
        data = yaml.load(f)
        dict_data = data[data_key]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)

        return list_data