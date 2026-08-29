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
Hang snapshot + devcoredump + persistent reset reason + heartbeat/watchdog + reset gate/generation.

### Near-term feature path
Hang detection → freeze diagnostic state → structured snapshot → health classification → close admission/drain → reset-generation transition → reset → state restore → reopen admission → progressively finer recovery.

## Industry Updates
### 2026-08-29 · Weekly #3
1. **UALink connection reset exposes a future multi-device generation boundary.**
   - Source: https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html
   - Change: the AMDGPU UALink design includes peer connection state/reset together with remote interrupt/TLB and export/import state cleanup.
   - KMD impact: future multi-GPU RAS should not collapse local GPU reset, firmware restart, fabric/peer connection reset and remote-memory mapping revocation into one generation counter. Define ownership and dependency between these lifetimes so stale peer channels/handles/completions cannot survive a partial recovery.
   - Priority: **Define generation boundaries now; implement when fabric hardware is real.**

2. **Reset gate/generation remains the current production-RAS priority.**
   - Reference: https://lwn.net/Articles/1088747/
   - KMD impact: snapshot-before-reset → close admission → drain → generation transition → recover/restore → reopen remains the active implementation path.
   - Priority: **Now.**

### 2026-08-22 · Weekly #2
1. **Tyr GPU reset v4 makes reset admission/concurrency an explicit KMD subsystem.**
   - Source: https://lwn.net/Articles/1088747/
   - KMD impact: normal GPU operations need explicit admission/drain rules around reset; duplicate reset requests coalesce and post-reset state publication advances generation before normal admission resumes.
   - Priority: **Design now; implement with the first production reset/recovery path.**

2. **Linux 7.2 shipped after late DRM scheduling reverts, reinforcing staged recovery/scheduler changes.**
   - Source: https://lwn.net/Articles/1089033/
   - Priority: **Engineering discipline now.**

### 2026-08-15 · Weekly #1
1. **Xe GPU Health Indicator / Device Wedging makes the management-facing RAS contract explicit.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_device.html
   - KMD impact: separate raw evidence → KMD classification/recovery policy → management-facing health state/recovery hint.
   - Priority: **Snapshot/heartbeat now; health/recovery contract in 6–12 months.**
2. **Snapshot-before-reset remains the hard recovery invariant.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_devcoredump.html
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **Production GPU crash tooling is converging on richer structured post-mortem artifacts.**
   - Reference: https://gpuopen.com/learn/radeon-developer-tool-suite-amd-rdna4/
   - Priority: **Snapshot schema now; richer correlation in 6–12 months.**
2. **Snapshot-before-reset remains the hard recovery invariant.**
   - Priority: **Now.**

### 2026-08-08 · Test #2
1. **Firmware log retention should be part of crash infrastructure, including probe/boot failures.**
   - Source: https://docs.kernel.org/gpu/nova/core/todo.html
2. **Snapshot-before-reset remains unchanged.**

### 2026-08-08 · Test #1
1. **Xe devcoredump reinforces snapshot-at-hang/read-later.**
2. **Standard devcoredump infrastructure is preferable to vendor-only channels.**
3. **Production RAS should evolve beyond global reset.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
