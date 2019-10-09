"""
    1，首先运行这个文件（图片名称转换）
    2，totorial.py（生成配置文件，开始训练时 Ctrl-C 停止）
        可能需要修改的配置：
            EndAcc: 0.95        要求达到的准确率，达到会自动停止，否则一直训练
            test_num: 50        划分测试集数量
            TestBatchSize: 10   测试集批处理数量，必须小于test_num，默认10，一般无需调整
    3，检查配置文件model.yaml，运行trains.py开始训练
    （每次训练前清空 model/, log/, out/，不清空/model默认断点续练，没有测试，还是清空吧）
    完成后会在out/中生成一个.pb，一个.yaml
"""

import re
import os
import hashlib

# 训练集路径
root = r"./images/"
all_files = os.listdir(root)

for file in all_files:
    old_path = os.path.join(root, file)

    # 已被修改过忽略
    if len(file.split(".")[0]) > 32:
        continue

    # 采用标注_文件md5码.图片后缀 进行命名
    with open(old_path, "rb") as f:
        _id = hashlib.md5(f.read()).hexdigest()
    new_path = os.path.join(root, file.replace(".", "_{}.".format(_id)))

    # 重复标签的时候会出现形如：abcd (1).jpg 这种形式的文件名
    new_path = re.sub(" \(\d+\)", "", new_path)
    print(new_path)
    os.rename(old_path, new_path)

