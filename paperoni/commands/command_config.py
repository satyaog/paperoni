from coleo import default, tooled, Argument as Arg

from ..config import get_config, write_config
from ..utils import T


@tooled
def command_config():
    cfg = get_config() or {}
    orig_cfg = dict(cfg)

    key: Arg & str = default(None)

    if key is None:
        print(
            T.bold("Note:"),
            "You need a Microsoft Academic Search API key in order to use this program.",
            "Free tier API keys will afford you 5000 to 10000 queries",
            "per month which is more than enough for personal use.",
            "You can get one by subscribing here:"
        )
        print()
        print(
            "  https://msr-apis.portal.azure-api.net/products/project-academic-knowledge"
        )
        print()
        print("Once you have an API key, paste it below:")
        print()
        key = get_config("key")
        key = input(T.cyan(f"Enter MS Academic API key [{key}]: ")) or key

    cfg["key"] = key
    if cfg != orig_cfg:
        write_config(cfg)
