import json
import tempfile
import unittest
from pathlib import Path

from scripts.release_versions import load_release, prepare, rollback

V1 = {
    "vault": "1" * 40,
    "atlas": "2" * 40,
    "forge": "3" * 40,
}
V2 = {
    "vault": "4" * 40,
    "atlas": "5" * 40,
    "forge": "6" * 40,
}


class ReleaseVersionsTest(unittest.TestCase):
    def test_initial_release_publishes_images(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runtime = Path(directory)
            prepare(runtime, V1, "all")

            self.assertEqual(load_release(runtime / "release.json"), V1)
            environment = (runtime / "versions.env").read_text(encoding="utf-8")

        self.assertIn(f"VAULT_IMAGE=ghcr.io/mateorc/vaultsh:{V1['vault']}", environment)
        self.assertIn(f"ATLAS_IMAGE=ghcr.io/mateorc/atlas:{V1['atlas']}", environment)

    def test_targeted_release_changes_one_service(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runtime = Path(directory)
            prepare(runtime, V1, "all")
            release = prepare(runtime, V2, "atlas")

            self.assertEqual(release["vault"], V1["vault"])
            self.assertEqual(release["atlas"], V2["atlas"])
            self.assertEqual(release["forge"], V1["forge"])

    def test_rollback_swaps_current_and_previous(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runtime = Path(directory)
            prepare(runtime, V1, "all")
            prepare(runtime, V2, "all")

            self.assertEqual(rollback(runtime), V1)
            self.assertEqual(load_release(runtime / "previous-release.json"), V2)
            self.assertEqual(rollback(runtime), V2)

    def test_non_sha_version_is_rejected(self) -> None:
        invalid = dict(V1, vault="main")
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "full Git SHA"):
                prepare(Path(directory), invalid, "all")

    def test_requested_version_requires_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "targeted service"):
                prepare(Path(directory), V1, "all", "7" * 40)
