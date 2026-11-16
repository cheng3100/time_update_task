# AGENTS.md

Repository instructions for automated agents and scheduled tasks.

## Mandatory instruction order

Before modifying this repository, an agent must read and follow:

1. The target task's local rules, for GPU KMD: `kmd_owner_direction/UPDATE_RULES.md`.
2. The target task's local README, for GPU KMD: `kmd_owner_direction/README.md`.
3. The current Jekyll/source-of-truth files relevant to the requested change, such as `_data/`, `pages/`, `_layouts/`, generators, and workflow files.

Task-local rules are authoritative for that task. Do not assume rules from one scheduled task apply to another task.

## GPU KMD Weekly

For the GPU KMD Weekly task, the current confirmed chat-output and depth-selection rules are defined in:

- `kmd_owner_direction/UPDATE_RULES.md` → **Section 11. Confirmed chat-output depth and structure rules**

Important current constraints:
- Memory/UVM topics default to L4.
- DMA-BUF / P2P / virtualization-memory and similarly coupled topics default to L3.
- Other topics default to L1 radar depth.
- No more than 3 L3/L4 deep dives per weekly chat report.
- Current chat skeleton: 本期重点 → A 方向变化 → B Deep Dive → C 其他方向 Radar → 总结回顾.
- Do not reintroduce the retired A–P chat structure unless explicitly requested.
- Use 2026-11-07 Weekly #13 as the current redesign reference sample.
- The weekly automation is intentionally paused during redesign and must not be resumed unless the user explicitly asks.

## Raw-report invariant

A scheduled run must use one canonical report body for both the ChatGPT conversation output and its `*.raw.md` archive. Never independently summarize, translate, or reconstruct canonical raw content.

## Jekyll / Pages

Treat canonical archives and presentation as separate layers:
- archive/data sources are source-of-truth;
- Jekyll layouts/pages/data generate presentation;
- do not recreate a parallel static HTML site;
- preserve stable public permalinks where practical.
