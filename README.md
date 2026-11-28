# guili · 圭例库

**GUILI-01 勘判先例库：例以辅圭，判有所依。**

> 命名即种子：圭例库＝以圭（标准）为纲、以例（先例）为目的勘判依据库。名字所对应的逻辑与架构，是从种子长出来的。

## 命名映射（道统 → 架构）

| 道 | 义 | 算子 |
|----|----|------|
| 引 | 援引最适先例，给裁决建议与依据链 | `Yin` 援引官 |
| 鉴 | 先例冲突与过时检测，标记相抵先例对 | `Jian` 勘验官 |
| 册 | 援引流水只增不覆盖，多用闲置可统计 | `Ce` 援引台账官 |

逻辑本体：**凡裁决必先援引先例，先例相抵须勘验，援引必留台账可查。**
无例可援时明示「此判无据」，不硬裁——援引官先说清手里有什么，才谈得上依循。

## 安装

零第三方依赖，仅 Python 3.10+ 标准库。

```bash
git clone https://github.com/tanbopiao/guili.git
cd guili
python -m unittest discover -s tests -v   # 自测
python examples/demo_precedent.py         # 端到端演示
```

## 用法

```python
from guili import Guili

g = Guili()

# 立例：先例入库，只增不覆盖
g.add_precedent({"tags": ["幂等"], "ruling": "重试须带幂等键"})

# 引：援引最适先例
r = g.cite("支付重试引发幂等问题")
print(r["verdict"])   # 重试须带幂等键
print(r["basis"])     # ['GL-0001']

# 鉴：勘验全库，标记相抵先例对
print(g.audit()["conflicts"])

# 册：援引台账——何例多用、何例闲置
print(g.ledger())
```

原单文件骨架 API（`describe()` / `add_precedent()` / `lookup()`）收编保留，行为不变。

## 自测

```bash
python -m unittest discover -s tests -v
```

## 许可

MIT
