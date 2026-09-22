import markdown
import sys


def markdown_to_html(inputpath, outputpath):
    with open(inputpath, "r") as f:
        contents = f.read()

    html = markdown.markdown(contents)

    with open(outputpath, "w") as f:
        f.write(html)

def validate_args(args):
    if len(args) == 0:
        raise ValueError("コマンドを指定してください")

    command = args[0]

    if command == "markdown":
        if len(args) != 3:
            raise ValueError(
                "markdownにはinputfileとoutputfileが必要です"
            )
    else:
        raise ValueError("存在しないコマンドです")


args = sys.argv[1:]

validate_args(args)

command = args[0]

if command == "markdown":
    markdown_to_html(args[1], args[2])
