"""圭例库（GUILI）· 勘判先例库

道统出处：元极恒一·道统构件定名册 V1.0 全量编译补录 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：勘判先例库。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Guili:
    """圭例库（GUILI）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "GUILI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "guili",
            "cn": "圭例库",
            "code": self.CODE,
            "duty": "勘判先例库",
            "mingwen": "例以辅圭，判有所依",
            "anchor": self.ANCHOR,
        }

    def add_precedent(self, case):
        """先例入库，只增不覆盖（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("GUILI.add_precedent 骨架桩，候进化轮补齐")

    def lookup(self, issue):
        """例以辅圭：按争点查先例（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("GUILI.lookup 骨架桩，候进化轮补齐")
