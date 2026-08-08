# KMD Long-term Learning Resource Library

长期学习资料与每期 Industry Updates 分离维护。

## Structure

```text
resources/
├── memory/<sub-direction>.md
├── virt/<sub-direction>.md
├── power/<sub-direction>.md
├── ras/<sub-direction>.md
├── multi/<sub-direction>.md
├── obs/<sub-direction>.md
└── fw/<sub-direction>.md
```

规则：
- 每个长期子方向一个独立 Markdown source-of-truth；
- Pages 为每个子方向提供唯一 URL，并直接读取对应 Markdown；
- 文档稳定增长，新资料默认追加；
- 每条资料必须写：**是什么 / 价值点 / 学习重点 / 学习注意 / 原始链接**；
- 仅在资源失效、被明显更权威资料替代或子方向边界明确变化时修改已有条目；
- Industry Updates 不放入这些文档，仍在一级 Owner Living 区域按期维护。
