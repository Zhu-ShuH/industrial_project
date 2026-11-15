# 标准工程职责

src/plantops 存放业务代码，tests 保存回归测试，config 保存非敏感配置，data 保存演示输入，docs 记录设计决策。CI 在每次 push 或 pull request 检查格式、测试、静态评分；本地 pre-commit 在提交前执行同一套规则。
