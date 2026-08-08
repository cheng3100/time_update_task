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
### 2026-08-08

1. **Xe devcoredump reinforces “snapshot at hang, read later” as the right recovery boundary.**
   - Source: Linux Xe Device Coredump: https://www.kernel.org/doc/html/latest/gpu/xe/xe_devcoredump.html
   - Change: Xe captures HW/driver state at hang time because recovery/reset can alter state before userspace reads the dump. It also prioritizes the first failure and ties snapshot collection to serialized reset flow.
   - KMD impact: diagnostic capture must happen before destructive recovery. Build a frozen snapshot object rather than generating debug output lazily from live registers after reset.
   - Priority: **Now**.

2. **Standard devcoredump infrastructure is preferable to a vendor-only error-state channel.**
   - Source: Xe merge/RFC documentation and current devcoredump implementation.
   - Change: Xe intentionally aligned with common `dev_coredump` rather than inventing a Xe-only error-state interface.
   - KMD impact: use standard Linux crash-delivery mechanisms where possible, while keeping GPU-specific binary/structured sections inside the dump payload.
   - Priority: **Now**.

3. **Production RAS should evolve beyond global reset.**
   - Industry signal: modern GPU drivers expose error attribution, CE/UE handling, bad-page retirement, reset reason and fault injection as separate mechanisms.
   - KMD impact: after snapshot infrastructure lands, define a recovery ladder: job abort → queue kill → context kill → engine reset → partial/full GPU reset, with clear criteria and post-reset state restoration.
   - Priority: **6–12 months** after baseline hang capture.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
