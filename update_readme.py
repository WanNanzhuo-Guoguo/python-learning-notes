from pathlib import Path
import re


ROOT = Path(__file__).parent
README = ROOT / "README.md"


def get_chapters():
    """获取所有以 数字- 开头的学习目录"""

    chapters = []

    for path in ROOT.iterdir():

        if not path.is_dir():
            continue

        match = re.match(r"^(\d+)-(.+)$", path.name)

        if match:
            number = int(match.group(1))
            topic = match.group(2)

            chapters.append(
                {
                    "number": number,
                    "folder": path.name,
                    "topic": topic,
                }
            )

    chapters.sort(key=lambda x: x["number"])

    return chapters


def generate_roadmap(chapters):
    """生成 Learning Roadmap"""

    lines = [
        "| Chapter | Topic | Status |",
        "| :---: | --- | :---: |",
    ]

    for chapter in chapters:

        number = f"{chapter['number']:02d}"
        topic = chapter["topic"]
        folder = chapter["folder"]

        lines.append(
            f"| {number} | [{topic}](./{folder}/) | ✅ |"
        )

    lines.append("| ... | 持续学习中 | 🚧 |")

    return "\n".join(lines)


def generate_structure(chapters):
    """生成 Repository Structure"""

    lines = [
        "```text",
        "python-learning-notes/",
        "│",
    ]

    for chapter in chapters:

        folder = ROOT / chapter["folder"]

        lines.append(f"├── {chapter['folder']}/")

        files = sorted(
            [
                file.name
                for file in folder.iterdir()
                if file.is_file()
            ]
        )

        for index, filename in enumerate(files):

            if index == len(files) - 1:
                prefix = "│   └──"
            else:
                prefix = "│   ├──"

            lines.append(f"{prefix} {filename}")

        lines.append("│")

    lines.append("├── update_readme.py")
    lines.append("└── README.md")
    lines.append("```")

    return "\n".join(lines)


def replace_section(text, start_marker, end_marker, content):
    """替换 README 中指定区域"""

    pattern = (
        re.escape(start_marker)
        + r".*?"
        + re.escape(end_marker)
    )

    replacement = (
        start_marker
        + "\n"
        + content
        + "\n"
        + end_marker
    )

    return re.sub(
        pattern,
        replacement,
        text,
        flags=re.DOTALL,
    )


def main():

    chapters = get_chapters()

    text = README.read_text(encoding="utf-8")

    roadmap = generate_roadmap(chapters)
    structure = generate_structure(chapters)

    text = replace_section(
        text,
        "<!-- ROADMAP_START -->",
        "<!-- ROADMAP_END -->",
        roadmap,
    )

    text = replace_section(
        text,
        "<!-- STRUCTURE_START -->",
        "<!-- STRUCTURE_END -->",
        structure,
    )

    README.write_text(text, encoding="utf-8")

    print("README.md 更新完成！")


if __name__ == "__main__":
    main()