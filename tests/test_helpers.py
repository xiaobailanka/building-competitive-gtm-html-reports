"""Regressions for misleading completion and offline dependency checks."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_report.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / "nested/report.html"
        self.golden = (ROOT / "assets/golden-example-oppo-find-x10-vs-xiaomi18.html").read_text(encoding="utf-8")

    def check_html(self, text):
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.output.write_text(text, encoding="utf-8")
        return validator.validate(self.output)[0]

    def test_golden_structurally_valid(self):
        self.assertEqual(self.check_html(self.golden), [])

    def test_draft_not_accepted_as_complete_and_title_escaped(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/scaffold_report.py"), str(self.output),
            "--title", '<script>alert("bad")</script>', "--analysis-date", "2026-10-05"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        raw = self.output.read_text(encoding="utf-8")
        self.assertIn("&lt;script&gt;", raw)
        self.assertNotIn('<script>alert("bad")</script>', raw)
        self.assertIn("2026-10-05", raw)
        self.assertTrue(validator.validate(self.output)[0])
        self.assertEqual(validator.validate(self.output, allow_scaffold=True)[0], [])
        second = subprocess.run([sys.executable, str(ROOT / "scripts/scaffold_report.py"), str(self.output)], capture_output=True)
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(raw, self.output.read_text(encoding="utf-8"))

    def test_local_and_remote_dependencies_rejected(self):
        for snippet in ('<script src="local.js"></script>', '<script src="//cdn.example/test.js"></script>',
            '<link href="local.css" rel="stylesheet">', '<img src="photo.png">',
            '<style>@import "https://example.com/a.css";</style>', '<style>.hero{background:url(bg.png)}</style>'):
            with self.subTest(snippet=snippet):
                self.assertTrue(self.check_html(self.golden.replace('</head>', snippet + '</head>')))

    def test_source_hyperlinks_and_embedded_images_allowed(self):
        self.assertEqual(self.check_html(self.golden.replace('</body>',
            '<img src="data:image/png;base64,abc" alt="embedded"></body>')), [])

    def test_broken_anchor_and_duplicate_id_rejected(self):
        for snippet in ('<a href="#missing-section">broken</a>', '<div id="sources"></div>'):
            with self.subTest(snippet=snippet):
                self.assertTrue(self.check_html(self.golden.replace('</body>', snippet + '</body>')))

    def test_chinese_unfinished_content_rejected(self):
        self.assertTrue(self.check_html(self.golden.replace('</body>', '<p>补充真实内容。</p></body>')))

    def test_invalid_utf8_and_missing_file_report_errors(self):
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.output.write_bytes(b'\xff\xfeinvalid')
        self.assertTrue(validator.validate(self.output)[0])
        self.assertTrue(validator.validate(self.output.with_name('absent.html'))[0])


if __name__ == "__main__":
    unittest.main()
