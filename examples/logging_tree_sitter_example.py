from logging import INFO, Logger, basicConfig, getLogger
from time import sleep

from salve_dependency_hub import langauge_mappings, language_functions

from salve import HIGHLIGHT_TREE_SITTER, IPC, Response

basicConfig(
    level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger: Logger = getLogger("Main")


def main():
    context = IPC()

    context.update_file(
        "test",
        open(__file__, "r+").read(),
    )

    context.request(
        HIGHLIGHT_TREE_SITTER,
        file="test",
        language="python",
        text_range=(1, 30),
        tree_sitter_language=language_functions["python"],
        mapping=langauge_mappings["python"],
    )

    sleep(1)
    output: Response | None = context.get_response(HIGHLIGHT_TREE_SITTER)
    print(output)
    context.kill_IPC()


if __name__ == "__main__":
    main()