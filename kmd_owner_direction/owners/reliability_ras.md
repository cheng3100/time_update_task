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

### Near-term feature path
Hang detection → freeze diagnostic state → structured snapshot → devcoredump → reset → state restore → progressively finer queue/context/engine recovery.

## Industry Updates
### 2026-08-08 · Test #2
1. **Firmware log retention should be part of crash infrastructure, including probe/boot failures.**
   - Source: Nova task list: https://docs.kernel.org/gpu/nova/core/todo.html
   - Change: Nova explicitly tracks exporting GSP-RM log buffers through debugfs even when driver probe fails.
   - KMD impact: hang/devcoredump design should include FW logs and early-init state, not only runtime rings/registers.
   - Priority: **Now / 6–12 months.**

2. **Snapshot-before-reset remains unchanged and should be treated as the hard recovery invariant.**
   - Source: Linux Xe devcoredump documentation.
   - KMD impact: recovery code must never destroy the only useful evidence before snapshot collection completes.
   - Priority: **Now.**

### 2026-08-08 · Test #1
1. **Xe devcoredump reinforces “snapshot at hang, read later”.**
   - Priority: **Now**.
2. **Standard devcoredump infrastructure is preferable to a vendor-only channel.**
   - Priority: **Now**.
3. **Production RAS should evolve beyond global reset.**
   - Priority: **6–12 months** after baseline hang capture.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
