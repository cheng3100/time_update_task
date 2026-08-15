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
Hang detection → freeze diagnostic state → structured snapshot → devcoredump → health classification/recovery hint → reset → state restore → progressively finer queue/context/engine recovery.

## Industry Updates
### 2026-08-15 · Weekly #1
1. **Xe GPU Health Indicator / Device Wedging makes the management-facing RAS contract explicit.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_device.html
   - Change: Xe exposes `gpu_health` states (`ok`, `warning`, `critical`) and DRM wedged recovery hints; vendor-specific recovery may direct userspace/admin toward firmware remediation while the default path is rebind/bus-reset.
   - KMD impact: production RAS should separate raw evidence → KMD classification/recovery policy → management-facing health state/recovery hint. Monitoring tools should not need to parse dmesg to infer whether a GPU is usable.
   - Priority: **Snapshot/heartbeat now; health/recovery contract in 6–12 months.**

2. **Snapshot-before-reset remains the hard recovery invariant.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_devcoredump.html
   - KMD impact: versioned crash evidence must be frozen before destructive recovery; offline tooling should consume the artifact independently of the live device state.
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **Production GPU crash tooling is converging on richer structured post-mortem artifacts.**
   - Sources: AMD Radeon GPU Detective hardware crash analysis and NVIDIA Nsight Aftermath.
   - Reference: https://gpuopen.com/learn/radeon-developer-tool-suite-amd-rdna4/
   - KMD impact: coredump schema should evolve beyond register/ring dumps to versioned sections for execution/workload markers, MMU/page-fault state, FW logs and relevant HW state, with offline tooling as a separate consumer.
   - Priority: **Snapshot schema now; richer correlation in 6–12 months.**

2. **Snapshot-before-reset remains the hard recovery invariant.**
   - Source: https://docs.kernel.org/gpu/xe/xe_devcoredump.html
   - KMD impact: destructive recovery must not begin before the only useful crash evidence has been frozen; early boot/probe failure evidence should share the same architecture where possible.
   - Priority: **Now.**

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
