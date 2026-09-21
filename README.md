# industrial_project

P1.2 标准 Python 工程模板（A层）。

## 项目结构

```text
industrial_project/
├── src/
├── tests/
├── config/
├── data/
├── docs/
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── .flake8
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

macOS / Linux：

```bash
source venv/bin/activate
```

## 安装依赖

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 运行测试

```bash
pytest -v
```

## 代码规范检查

```bash
black --check src tests
flake8 src tests
pylint src --fail-under=9.0
```

## pre-commit

```bash
pre-commit install
pre-commit run --all-files
```
