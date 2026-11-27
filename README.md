# 质押退出队列与迟到罚没归属

保存质押池的合成验证者状态、入份额与退出申请及实际赎回到账。时间由纪元和观测顺序共同标识。

在仓库根目录使用 Python 3.11 的标准库。资料用 UTF-8 CSV 保存，空字段的含义见数据说明。

```sh
python3 inspect_inputs.py
python3 -m unittest discover -s tests -v
```

查看入口按表列出记录数及原始字段。资料测试核对文件接口和关键跨表引用。业务时点、计量单位及来源字段见[数据说明](data/README.md)。
