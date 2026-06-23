import sys
import subprocess

#
# todo: refactor this script


def start_server(port=8000):
    subprocess.run(
        ["gunicorn", "-b", f"127.0.0.1:{port}", "main:application"],
        check=True,
    )


def parse_args() -> tuple[str, int]:
    args = sys.argv[1:]

    default_port = 8000

    # run with default settings
    if not args:
        return ('run', default_port)

    command = args[0] or ''

    # different port
    if command == 'run':
        port = int(args[1]) if len(args) > 1 else default_port
        return ('run', port)

    # no command
    return (command, default_port)


def main() -> None:
    command, port = parse_args()

    if command == 'run':
        start_server(port)
    else:
        print(f'Uknown command: {command}')


if __name__ == '__main__':
    main()