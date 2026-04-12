"""Play or export the course introduction with macOS text-to-speech."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_VOICE = "Tingting"
DEFAULT_RATE = 185

RECOMMENDED_VOICES = {
    "Tingting": "中文女声，比较标准，适合课程讲解",
    "Reed (中文（中国大陆）)": "中文男声，更沉稳，适合长段讲解",
    "Eddy (中文（中国大陆）)": "中文男声，偏自然口语",
    "Flo (中文（中国大陆）)": "中文女声，语速感较轻快",
    "Sandy (中文（中国大陆）)": "中文女声，较柔和",
    "Shelley (中文（中国大陆）)": "中文女声，比较清晰",
    "Sinji": "粤语女声，如果你想听粤语可用",
    "Meijia": "繁体中文女声，适合台湾口音场景",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def default_input_file() -> Path:
    return repo_root() / "docs" / "media" / "course-intro.md"


def markdown_to_speech_text(markdown: str) -> str:
    lines: list[str] = []
    in_english_section = False

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("## English Keywords"):
            in_english_section = True
            continue
        if in_english_section:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        lines.append(line)

    return "\n".join(lines)


def build_say_command(text: str, voice: str, rate: int, output: Path | None) -> list[str]:
    command = ["say", "-v", voice, "-r", str(rate)]
    if output is not None:
        command.extend(["-o", str(output)])
    command.append(text)
    return command


def available_voice_lines() -> list[str]:
    try:
        result = subprocess.run(
            ["say", "-v", "?"],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return []
    except subprocess.CalledProcessError:
        return []

    return [line for line in result.stdout.splitlines() if line.strip()]


def chinese_voice_lines() -> list[str]:
    voices = []
    for line in available_voice_lines():
        lowered = line.lower()
        if "zh_" in lowered or "中文" in line or "tingting" in lowered or "sinji" in lowered or "meijia" in lowered:
            voices.append(line)
    return voices


def recommended_voice_text() -> str:
    lines = ["推荐语音："]
    for voice, description in RECOMMENDED_VOICES.items():
        lines.append(f"- {voice}: {description}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Play or export the course introduction with macOS text-to-speech.",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=default_input_file(),
        help="Markdown file to read. Default: docs/media/course-intro.md",
    )
    parser.add_argument(
        "--voice",
        default=DEFAULT_VOICE,
        help="macOS voice name. Default: Tingting",
    )
    parser.add_argument(
        "--rate",
        type=int,
        default=DEFAULT_RATE,
        help="Speech rate for the say command. Default: 185",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output audio file path, for example docs/media/course-intro.aiff",
    )
    parser.add_argument(
        "--print-text",
        action="store_true",
        help="Print the extracted speech text instead of playing it.",
    )
    parser.add_argument(
        "--speak",
        action="store_true",
        help="Speak the course introduction immediately.",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="List detected Chinese-capable macOS voices.",
    )
    parser.add_argument(
        "--recommended-voices",
        action="store_true",
        help="Print recommended voices for this course.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list_voices:
        lines = chinese_voice_lines()
        if not lines:
            print("No Chinese-capable macOS voices were detected.", file=sys.stderr)
            return 1
        print("\n".join(lines))
        return 0

    if args.recommended_voices:
        print(recommended_voice_text())
        return 0

    if not args.file.exists():
        print(f"Input file not found: {args.file}", file=sys.stderr)
        return 1

    speech_text = markdown_to_speech_text(args.file.read_text(encoding="utf-8"))

    if args.print_text:
        print(speech_text)
        return 0

    if not args.speak and args.output is None:
        print("Use --speak to play audio or --output to export a file.", file=sys.stderr)
        return 1

    command = build_say_command(
        text=speech_text,
        voice=args.voice,
        rate=args.rate,
        output=args.output,
    )

    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("The macOS 'say' command is not available on this machine.", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"Voice playback failed with exit code {exc.returncode}.", file=sys.stderr)
        return exc.returncode

    if args.output is not None:
        print(f"Audio exported to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
