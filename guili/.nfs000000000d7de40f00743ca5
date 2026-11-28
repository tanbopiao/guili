"""引 · 援引官：给定争点匹配最适先例，给出裁决建议与依据链。"""

from .ce import Ce


class Yin:
    """援引官：手里持册，援引必留痕。"""

    def __init__(self, guili, ledger=None):
        self._g = guili
        self._ce = ledger or Ce()

    def cite(self, issue):
        """援引：按争点匹配先例，给裁决建议与依据链；无例可援则明示无据。"""
        import json
        text = issue if isinstance(issue, str) else json.dumps(issue, ensure_ascii=False)
        hits = self._g.lookup(text)
        if not hits:
            self._ce.record(None, issue, outcome="no_precedent")
            return {
                "issue": text,
                "verdict": None,
                "advice": "无先例可援，此判无据——宜先立例再裁",
                "basis": [],
            }
        best = hits[0]["case"]
        cited_ids = [h["case_id"] for h in hits]
        for cid in cited_ids:
            self._ce.record(cid, issue, outcome="cited")
        return {
            "issue": text,
            "verdict": best.get("ruling") if isinstance(best, dict) else best,
            "advice": "例以辅圭：循先例裁之，依据如下",
            "basis": cited_ids,
        }
