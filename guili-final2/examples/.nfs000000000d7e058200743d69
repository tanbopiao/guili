"""圭例库端到端演示：立例 → 援引 → 勘验 → 台账。"""
from guili import Guili

g = Guili()

# 立例：先例入库，只增不覆盖
g.add_precedent({"tags": ["原子性"], "ruling": "跨库写须同务，两步不如一步"})
g.add_precedent({"tags": ["幂等"], "ruling": "重试须带幂等键"})
g.add_precedent({"tags": ["锁"], "ruling": "先到先得"})
g.add_precedent({"tags": ["锁"], "ruling": "后到让先"})  # 与上例相抵

# 引：援引最适先例
r = g.cite("支付重试引发幂等问题")
print("援引裁决：", r["verdict"])
print("依据链：", r["basis"])

# 鉴：勘验全库
a = g.audit()
print("相抵先例对：", [(c["a"], c["b"]) for c in a["conflicts"]])

# 册：援引台账
s = g.ledger()
print("多用例：", s["cited"])
print("闲置例：", s["idle"])
