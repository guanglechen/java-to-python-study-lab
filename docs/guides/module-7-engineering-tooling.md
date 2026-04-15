# 模块 7 学习指引：工程化工具链 | Module 7 Guide

## 这节学什么

这节我们将从“写代码”转向“管项目”。对于 Java 开发者来说，这相当于从写 `.java` 文件转向理解 `pom.xml` 或 `build.gradle` 的自动化生态。

1. **pyproject.toml**：现代 Python 项目的单一配置入口。
2. **Ruff**：极速的 Lint 和代码格式化工具（替代 Black, isort, Flake8 等）。
3. **Mypy**：静态类型检查器，让 Python 拥有接近 Java 的编译期安全感。
4. **依赖管理**：区分生产依赖与开发依赖。

## 对应文件

配置：`pyproject.toml`

## 先建立 3 个核心概念

1. **单一配置文件 (pyproject.toml)**
   - 以前 Python 项目有很多配置文件（setup.py, tox.ini, .flake8）。现在推荐全部合并到 `pyproject.toml`。

2. **Lint vs Format**
   - **Lint** (如 Ruff check)：检查代码逻辑错误（如未引用的变量、死循环）。
   - **Format** (如 Ruff format)：规范代码长相（如引号、缩进、空行）。

3. **静态类型检查 (Mypy)**
   - Python 的类型标注默认在运行时无效。Mypy 会静态扫描代码，如果你在 `int` 类型的参数里传了 `str`，它会像 Java 编译器一样报警。

## 对照 Java 的理解

| Python 工具 | Java 对应物 | 说明 |
| :--- | :--- | :--- |
| `pyproject.toml` | `pom.xml` / `build.gradle` | 定义依赖、版本、项目元数据和工具配置。 |
| `Ruff` | `CheckStyle` / `Spotless` | 强制统一代码风格，比 Java 端的工具快得多。 |
| `Mypy` | `Java Compiler` (类型检查部分) | 将 Python 从动态语言“加固”成准静态语言。 |
| `pip install -e .` | `mvn install` (local) | 将当前项目以“可编辑模式”安装到环境中。 |

## 本节任务你要重点看什么

### 1) `pyproject.toml` 的结构
查看 `[project]`、`[project.optional-dependencies]` 和 `[tool.*]` 块。

### 2) Ruff 的规则配置
查看 `select` 列表。我们开启了 `I` (排序 import) 和 `UP` (升级旧语法)，这能保证代码总是符合最新的 Pythonic 实践。

## 建议命令

在终端中尝试以下命令：

```bash
# 安装依赖（已在 Day 1 完成）
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m pip install -e ".[dev]"

# 运行 Lint 检查并自动修复（i.e., 自动按字母顺序排列导包）
/Users/chenguangyue/Documents/code/python/study/.venv/bin/ruff check --fix .

# 运行代码格式化（i.e., 自动调整空格和换行）
/Users/chenguangyue/Documents/code/python/study/.venv/bin/ruff format .

# 运行类型检查
/Users/chenguangyue/Documents/code/python/study/.venv/bin/mypy src
```

## 常见坑

1. **类型擦除陷阱**：Mypy 提示错误但 Python 运行正常。记住 Mypy 只是“静态检查”，不会影响运行结果。
2. **安装模式**：如果你改了 `src/` 下的项目名，需要重新运行 `pip install -e .`。
3. **第三方库无类型提示**：有些老库没有类型标注，Mypy 会报 `ignore_missing_imports`。

## 自检标准

完成本节后，你应该能回答：

1. 为什么 Python 现在推荐使用 `pyproject.toml` 而不是 `setup.py`？
2. Ruff 相比传统的 Flake8 有什么核心优势？
3. 如果 Mypy 报警，我能不能强行运行 Python 代码？
4. Java 的 `List<String>` 在 Python 开启严格 Mypy 检查后应如何书写？
