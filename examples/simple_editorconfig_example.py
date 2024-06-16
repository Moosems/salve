from time import sleep

from salve_ipc import IPC, Response


def main():
    context = IPC()

    context.update_file("test", "")

    context.request_editorconfig(file_path=__file__)

    sleep(1)
    output: Response | None = context.get_editorconfig_response()
    print(output["result"])  # type: ignore
    context.kill_IPC()


if __name__ == "__main__":
    main()
