"""鉴 · 勘验官：先例冲突与过时检测，标记相抵先例对。"""


class Jian:
    """勘验官：不裁决，只指出哪里靠不住。"""

    def __init__(self, guili):
        self._g = guili

    def audit(self):
        """勘验全库：同标签下 ruling 相抵的先例对记为冲突；标注缺失勘验字段的疑似过时项。"""
        conflicts = []
        stale = []
        by_tag = {}
        for p in self._g.precedents:
            case = p["case"]
            if not isinstance(case, dict):
                stale.append({"case_id": p["case_id"], "reason": "非结构化案卷，缺勘验字段"})
                continue
            ruling = str(case.get("ruling", ""))
            for tag in case.get("tags", []):
                bucket = by_tag.setdefault(tag, [])
                for other_id, other_ruling in bucket:
                    if other_ruling != ruling:
                        conflicts.append({
                            "a": other_id,
                            "b": p["case_id"],
                            "tag": tag,
                            "note": "同争点两判相抵，援引前须勘验孰是",
                        })
                bucket.append((p["case_id"], ruling))
            if "superseded_by" in case and case.get("superseded_by"):
                stale.append({"case_id": p["case_id"], "reason": "已有新例顶替，疑似过时"})
        return {"conflicts": conflicts, "stale": stale, "audited": len(self._g.precedents)}
