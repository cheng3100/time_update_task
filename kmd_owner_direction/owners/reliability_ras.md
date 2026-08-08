# GPU Reliability / Recovery / RAS

## Stable Summary
Own detection, diagnosis, containment and recovery of GPU faults plus production RAS, with progressively finer recovery granularity.

## Living Sub-directions
- heartbeat/watchdog and hang detection
- register/ring/queue/context/VM/FW hang snapshots
- devcoredump, structured crash report, reset reason
- job abort, queue/context kill, engine/partial/full reset
- post-reset restore and job replay
- firmware crash recovery coordination
- ECC CE/UE, bad-page retirement/remap, PCIe AER
- fault injection and per-context fault attribution

## Current Entry Feature
Hang snapshot + devcoredump + persistent reset reason + heartbeat/watchdog.

## Industry Updates
### 2026-08-08
- Intel Xe uses devcoredump to capture hang state before reset, while AMD RAS demonstrates production block-level CE/UE, bad-page and fault-injection models.
- Follow-up: **Now** — build snapshot/devcoredump first, then evolve toward fine-grained recovery.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
