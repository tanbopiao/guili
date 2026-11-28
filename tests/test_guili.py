"""圭例库（GUILI）算子测试：三算子＋门面＋legacy 兼容＋边界。"""
import unittest

from guili import Guili, Yin, Jian, Ce


class TestLegacyCompat(unittest.TestCase):
    """骨架原 API 行为不变。"""

    def setUp(self):
        self.op = Guili()

    def test_describe_unchanged(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "guili")
        self.assertEqual(d["code"], "GUILI")
        self.assertEqual(d["cn"], "圭例库")
        self.assertEqual(d["duty"], "勘判先例库")
        self.assertEqual(d["mingwen"], "例以辅圭，判有所依")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))

    def test_add_precedent_behavior(self):
        cid = self.op.add_precedent({"tags": ["原子性"], "ruling": "两步写须同务"})
        self.assertTrue(cid.startswith("GL-0001"))
        self.assertEqual(len(self.op.precedents), 1)

    def test_lookup_behavior(self):
        self.op.add_precedent({"tags": ["原子性"], "ruling": "两步写须同务"})
        hits = self.op.lookup("跨库写原子性缺口")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["case_id"], "GL-0001")

    def test_lookup_non_dict_case(self):
        self.op.add_precedent("纯文本先例")
        hits = self.op.lookup("含纯文本先例的争点")
        self.assertEqual(len(hits), 1)

    def test_seq_monotonic(self):
        a = self.op.add_precedent({"tags": ["t"], "ruling": "r1"})
        b = self.op.add_precedent({"tags": ["t"], "ruling": "r2"})
        self.assertLess(a, b)


class TestYin(unittest.TestCase):
    def setUp(self):
        self.g = Guili()

    def test_cite_with_precedent(self):
        self.g.add_precedent({"tags": ["幂等"], "ruling": "重试须幂等键"})
        r = self.g.cite("重试引发幂等问题")
        self.assertEqual(r["verdict"], "重试须幂等键")
        self.assertEqual(r["basis"], ["GL-0001"])
        self.assertIn("例以辅圭", r["advice"])

    def test_cite_empty_library(self):
        r = self.g.cite("无例可援的争点")
        self.assertIsNone(r["verdict"])
        self.assertEqual(r["basis"], [])
        self.assertIn("无先例可援", r["advice"])

    def test_cite_records_ledger(self):
        self.g.add_precedent({"tags": ["缓存"], "ruling": "失效须广播"})
        self.g.cite("缓存失效风暴")
        s = self.g.ledger()
        self.assertEqual(s["entries"], 1)
        self.assertEqual(s["cited"][0]["case_id"], "GL-0001")


class TestJian(unittest.TestCase):
    def setUp(self):
        self.g = Guili()

    def test_conflict_detection(self):
        self.g.add_precedent({"tags": ["锁"], "ruling": "先到先得"})
        self.g.add_precedent({"tags": ["锁"], "ruling": "后到让先"})
        r = self.g.audit()
        self.assertEqual(len(r["conflicts"]), 1)
        self.assertEqual(r["conflicts"][0]["tag"], "锁")

    def test_no_conflict_same_ruling(self):
        self.g.add_precedent({"tags": ["锁"], "ruling": "先到先得"})
        self.g.add_precedent({"tags": ["锁"], "ruling": "先到先得"})
        self.assertEqual(self.g.audit()["conflicts"], [])

    def test_stale_detection(self):
        self.g.add_precedent({"tags": ["t"], "ruling": "r", "superseded_by": "GL-9999"})
        r = self.g.audit()
        self.assertEqual(len(r["stale"]), 1)
        self.assertIn("疑似过时", r["stale"][0]["reason"])

    def test_audit_count(self):
        self.g.add_precedent({"tags": ["t"], "ruling": "r"})
        self.assertEqual(self.g.audit()["audited"], 1)


class TestCe(unittest.TestCase):
    def test_ledger_idle(self):
        g = Guili()
        g.add_precedent({"tags": ["a"], "ruling": "ra"})
        g.add_precedent({"tags": ["b"], "ruling": "rb"})
        g.cite("用 a 例的争点a")
        s = g.ledger()
        self.assertEqual(s["cited"][0]["case_id"], "GL-0001")
        self.assertEqual(s["idle"], ["GL-0002"])

    def test_ledger_no_precedent_outcome_not_counted(self):
        g = Guili()
        g.cite("空库援引")
        s = g.ledger()
        self.assertEqual(s["entries"], 1)
        self.assertEqual(s["cited"], [])


if __name__ == "__main__":
    unittest.main()
