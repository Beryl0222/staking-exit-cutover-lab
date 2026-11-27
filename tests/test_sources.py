"""检查离线资料的格式、引用和业务时点。"""
from pathlib import Path
import unittest

from inspect_inputs import read_table


DATA = Path(__file__).resolve().parents[1] / "data"
FIELDS = {
    'slices': ['slice', 'owner', 'validator', 'from_epoch', 'shares', 'assets'],
    'operations': ['op', 'epoch', 'sequence', 'kind', 'owner', 'from', 'to', 'amount', 'ref'],
    'validator_policy': ['validator', 'unbind_epochs', 'safety_epochs', 'scale'],
    'chain_statements': ['event', 'known_epoch', 'kind', 'validator', 'risk_epoch', 'amount', 'ref'],
    'payment_updates': ['id', 'epoch', 'kind', 'instruction', 'request', 'units'],
}


class InputBundleTest(unittest.TestCase):
    def test_csv_contract(self):
        self.assertEqual({p.stem for p in DATA.glob("*.csv")}, set(FIELDS))
        for name, expected in FIELDS.items():
            with self.subTest(table=name):
                fields, rows = read_table(DATA, name)
                self.assertEqual(fields, expected)
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))

    def test_related_source_records(self):
        _, records = read_table(DATA, 'chain_statements')
        slashes = {row['event']: row for row in records}
        _, records = read_table(DATA, 'operations')
        ops = {row['op']: row for row in records}
        _, records = read_table(DATA, 'payment_updates')
        pay = {row['id']: row for row in records}
        self.assertLess(int(slashes['C2']['risk_epoch']), int(ops['D1']['epoch']))
        self.assertGreater(int(slashes['C2']['known_epoch']), int(ops['X1']['epoch']))
        self.assertGreater(int(slashes['C9']['known_epoch']), int(pay['P2']['epoch']))


if __name__ == "__main__":
    unittest.main()
