from pathlib import Path
from tempfile import TemporaryDirectory

import gifnoc
from pytest import fixture


@fixture(scope="session", autouse=True)
def set_config():
    with TemporaryDirectory() as tmpdir:
        with gifnoc.use(
            Path(__file__).parent / "test-config.yaml",
            {"paperoni.data_path": str(Path(tmpdir) / "data")},
        ):
            yield
