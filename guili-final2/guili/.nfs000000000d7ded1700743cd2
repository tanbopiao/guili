"""册 · 援引台账官：只增不覆盖的援引流水，何例多用、何例闲置可统计。"""


class Ce:
    """台账官：流水只增，统计只读。闲置统计需接入库中先例全集。"""

    def __init__(self, precedents_provider=None):
        self._entries = []
        self._provider = precedents_provider  # 返回先例 id 全集的可调用，缺省不统计闲置

    def record(self, case_id, issue, outcome="cited"):
        """援引留痕：只增不覆盖。"""
        self._entries.append({"case_id": case_id, "issue": issue, "outcome": outcome})

    def summary(self):
        """台账汇总：何例多用（cited 计数降序）、何例闲置（零援引，需库全集）。"""
        counts = {}
        for e in self._entries:
            if e["case_id"] is not None and e["outcome"] == "cited":
                counts[e["case_id"]] = counts.get(e["case_id"], 0) + 1
        cited = [{"case_id": k, "cited": v} for k, v in sorted(counts.items(), key=lambda x: -x[1])]
        idle = []
        if callable(self._provider):
            known = set(self._provider())
            idle = sorted(known - set(counts))
        return {"cited": cited, "idle": idle, "entries": len(self._entries)}
