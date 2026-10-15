"""Check that browsable Markdown documents retain working local links."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


CONTENT = Path(__file__).resolve().parents[1] / "content"
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)


def heading_id(text):
    return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", text.lower()).strip())


class ContentLinksTest(unittest.TestCase):
    def test_consolidated_entry_points(self):
        self.assertTrue((CONTENT / "docs/projects/overview.md").is_file())
        self.assertTrue((CONTENT / "cv/experience.md").is_file())
        self.assertFalse((CONTENT / "cv/experience").exists())

    def test_projects_are_grouped_with_their_documents(self):
        for project in ("atlas", "forge", "oracle", "sentinel", "vaultsh"):
            for document in ("overview.md", "roadmap.md", "architecture.md"):
                self.assertTrue(
                    (CONTENT / "docs/projects" / project / document).is_file(),
                    f"missing docs/projects/{project}/{document}",
                )

    def test_legacy_document_folders_are_gone(self):
        self.assertFalse((CONTENT / "projects").exists())
        self.assertFalse((CONTENT / "docs/architecture").exists())
        self.assertFalse((CONTENT / "docs/roadmaps").exists())

    def test_local_markdown_links(self):
        for source in CONTENT.rglob("*.md"):
            text = source.read_text(encoding="utf-8")
            for href in LINK.findall(text):
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    continue
                target = (CONTENT / unquote(url.path).lstrip("/")) if url.path.startswith("/") else (source.parent / unquote(url.path))
                target = target.resolve()
                with self.subTest(source=source.relative_to(CONTENT), href=href):
                    self.assertTrue(target.is_relative_to(CONTENT.resolve()))
                    self.assertTrue(target.exists(), f"missing target: {target}")
                    if url.fragment and target.is_file():
                        ids = {heading_id(heading) for heading in HEADING.findall(target.read_text(encoding="utf-8"))}
                        self.assertIn(unquote(url.fragment), ids)


if __name__ == "__main__":
    unittest.main()
