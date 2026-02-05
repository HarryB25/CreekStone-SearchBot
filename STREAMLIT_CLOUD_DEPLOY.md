# Streamlit Community Cloud 部署说明

本项目已支持直接部署到 Streamlit Community Cloud，并读取仓库中的 `data/structured` 数据文件进行展示。

## 1. 部署前检查

- `requirements.txt` 已包含 `streamlit`、`pandas`、`pyarrow`
- 入口文件：`app.py`（内部转到 `webapp/streamlit_app.py`）
- GitHub Actions 会每天更新 `data/` 与 `data/structured/`

## 2. 在 Streamlit Community Cloud 创建应用

1. 打开 https://share.streamlit.io/
2. 用 GitHub 账号登录并授权仓库
3. 点击 **New app**
4. 填写：
   - Repository: `你的用户名/producthunt-daily-hot`
   - Branch: `main`
   - Main file path: `app.py`
5. 点击 **Deploy**

## 3. 可选：设置 Secrets

当前 Web 展示仅读取仓库数据，不强依赖额外 Secrets。  
如果你后续把在线抓取逻辑放进 Streamlit，再到 App Settings -> Secrets 配置。

## 4. 更新机制

- 每天 GitHub Actions 运行后会提交最新数据到仓库
- Streamlit Cloud 检测到新 commit 后会自动重启应用
- 页面会展示最新已提交数据（可用日期筛选查看）

## 5. 常见问题

- 页面没更新：先确认对应 GitHub workflow 成功，并且仓库有新 commit
- 数据有 commit 但页面旧：在 Streamlit Cloud 点击 **Reboot app**
- 启动失败：检查 `requirements.txt` 是否包含所有依赖
