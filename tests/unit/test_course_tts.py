from pathlib import Path

from scripts.course_tts import DEFAULT_VOICE
from scripts.course_tts import build_say_command
from scripts.course_tts import default_input_file
from scripts.course_tts import markdown_to_speech_text
from scripts.course_tts import recommended_voice_text


def test_markdown_to_speech_text_skips_headings_and_english_section() -> None:
    markdown = """
# Title

## 中文主讲

第一段。
- 第二段。

## English Keywords

- keyword
"""
    assert markdown_to_speech_text(markdown) == "第一段。\n第二段。"


def test_build_say_command_without_output() -> None:
    command = build_say_command("你好", voice=DEFAULT_VOICE, rate=180, output=None)
    assert command == ["say", "-v", DEFAULT_VOICE, "-r", "180", "你好"]


def test_build_say_command_with_output() -> None:
    output = Path("docs/course-intro.aiff")
    command = build_say_command("你好", voice=DEFAULT_VOICE, rate=180, output=output)
    assert command == ["say", "-v", DEFAULT_VOICE, "-r", "180", "-o", str(output), "你好"]


def test_default_input_file_points_to_course_intro_markdown() -> None:
    assert default_input_file().name == "course-intro.md"


def test_recommended_voice_text_contains_tingting() -> None:
    assert "Tingting" in recommended_voice_text()