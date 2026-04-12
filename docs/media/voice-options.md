# 课程语音选项 | Voice Options

## 推荐语音

下面这些是你这类课程介绍更适合的声音：

1. `Tingting`
中文女声，标准、清楚，适合默认课程讲解。

2. `Reed (中文（中国大陆）)`
中文男声，更稳一些。如果你觉得默认女声太尖，可以优先试这个。

3. `Eddy (中文（中国大陆）)`
中文男声，偏自然口语。

4. `Sandy (中文（中国大陆）)`
中文女声，偏柔和。

5. `Shelley (中文（中国大陆）)`
中文女声，发音清晰。

## 直接试听命令

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --voice "Reed (中文（中国大陆）)" --speak
```

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --voice "Eddy (中文（中国大陆）)" --speak
```

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --voice "Sandy (中文（中国大陆）)" --speak
```

## 列出本机可用中文语音

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --list-voices
```

## 输出推荐语音

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --recommended-voices
```

## 导出音频文件

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --voice "Reed (中文（中国大陆）)" --output docs/course-intro-reed.aiff
```

建议改为：

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --voice "Reed (中文（中国大陆）)" --output docs/media/course-intro-reed.aiff
```