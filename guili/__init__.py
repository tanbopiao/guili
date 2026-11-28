"""圭例库（GUILI）· 勘判先例库：例以辅圭，判有所依。

命名即种子：圭例库＝以圭（标准）为纲、以例（先例）为目的勘判依据库。
逻辑本体：凡裁决必先援引先例，先例之间相抵须勘验，援引必留台账可查。

三算子：
- 引（yin.Yin）    援引官：给定争点匹配最适先例，给出裁决建议与依据链。
- 鉴（jian.Jian）  勘验官：先例冲突与过时检测，标记相抵先例对。
- 册（ce.Ce）      援引台账官：只增不覆盖的援引流水，何例多用、何例闲置可统计。

三算子合枢于 Guili 门面（cite / audit / ledger）。
原单文件骨架 API（describe / add_precedent / lookup）收编保留，行为不变。
"""

from .legacy import Guili as _LegacyGuili
from .yin import Yin
from .jian import Jian
from .ce import Ce

__all__ = ["Guili", "Yin", "Jian", "Ce"]


class Guili(_LegacyGuili):
    """圭例库门面：原 v1 API 之上长出引/鉴/册三算子。"""

    def __init__(self, config=None):
        super().__init__(config)
        self._ce = Ce(lambda: [p["case_id"] for p in self.precedents])
        self._yin = Yin(self, ledger=self._ce)
        self._jian = Jian(self)

    def cite(self, issue):
        """引：给定争点，援引最适先例并给裁决建议与依据链；援引留册。"""
        return self._yin.cite(issue)

    def audit(self):
        """鉴：勘验全库，标记相抵先例对与疑似过时先例。"""
        return self._jian.audit()

    def ledger(self):
        """册：援引台账汇总——何例多用、何例闲置。"""
        return self._ce.summary()

    def ledger_digest(self):
        """台账快照哈希：先例内容被篡改即对不上，留痕防篡改。"""
        import hashlib, json
        raw = json.dumps(self.precedents, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:16]
