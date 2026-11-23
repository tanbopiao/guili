"""圭例库（GUILI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_add_precedent_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.add_precedent(None)

    def test_lookup_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.lookup(None)


if __name__ == "__main__":
    unittest.main()
