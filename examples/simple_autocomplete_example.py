from time import sleep

from salve_ipc import IPC, Response, tokens_from_result

context = IPC()

context.update_file(
    "test",
    open(__file__, "r+").read(),
)

context.request(
    "autocomplete",
    file="test",
    expected_keywords=[],
    current_word="t",
)

sleep(1)

output: Response = context.get_response("autocomplete")  # type: ignore
print(tokens_from_result(output["result"]))  # type: ignore
context.kill_IPC()