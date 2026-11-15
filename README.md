# Python A层标准工程模板

在此目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pip install -e .
python -m pre_commit install
python -m plantops.main
python -m pytest -q
python -m pre_commit run --all-files
```

`src/tests/config/data/docs` 各司其职；CI 配置在 `.github/workflows/ci.yml`。复制到远程仓库根目录，推送后可触发 GitHub Actions。若放在总仓库的子目录，需要给工作流设置对应的 `working-directory`。
