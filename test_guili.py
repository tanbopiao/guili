"""圭例库（GUILI）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from guili import Guili


class TestGuili(unittest.TestCase):
    def setUp(self):
        self.op = Guili()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "guili")
        self.assertEqual(d["code"], "GUILI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_add_lookup(self):
        cid = self.op.add_precedent({"tags": ["原子性"], "ruling": "两步写须同务"})
        self.assertTrue(cid.startswith("GL-"))
        hits = self.op.lookup("跨库写原子性缺口")
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["case_id"], cid)


if __name__ == "__main__":
    unittest.main()
