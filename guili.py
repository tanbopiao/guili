"""圭例库（GUILI）· 勘判先例库

道统出处：元极恒一·道统构件定名册 V1.0 全量编译补录 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：勘判先例库。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Guili:
    """圭例库（GUILI）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "GUILI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.precedents = []
        self._seq = 0

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
        """先例入库，只增不覆盖。"""
        self._seq += 1
        cid = "GL-%04d" % self._seq
        self.precedents.append({"case_id": cid, "case": case})
        self.events.append({"event": "add_precedent", "case_id": cid})
        return cid

    def lookup(self, issue):
        """例以辅圭：按争点查先例。"""
        import json
        text = issue if isinstance(issue, str) else json.dumps(issue, ensure_ascii=False)
        hits = []
        for p in self.precedents:
            case = p["case"]
            tokens = case.get("tags", []) if isinstance(case, dict) else [case]
            if any(str(t) in text for t in tokens):
                hits.append(p)
        self.events.append({"event": "lookup", "hits": len(hits)})
        return hits
