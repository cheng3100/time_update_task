# GPU Power / Performance

## Stable Summary
Own GPU power-state control and performance-management policy from measurement through DVFS, runtime PM, thermal and power budget.

## Living Sub-directions
- busy/idle and per-engine utilization accounting
- runtime PM and suspend/resume
- clock/power gating and idle residency
- DVFS, OPP/performance states and FW PM protocol
- thermal throttling and power cap
- frequency residency and memory-bandwidth utilization
- workload-aware boost/throttle
- PCIe ASPM/link power

## Current Entry Feature
GPU busy/idle + utilization accounting + asynchronous-access quiesce correctness → basic runtime PM/DVFS.

### Near-term feature path
Reliable busy/idle accounting → define all async GPU-register/memory users → quiesce/drain rules → runtime PM correctness → per-engine utilization/frequency telemetry → firmware-controlled DVFS → thermal/power-cap policy.

## Industry Updates
### 2026-09-05 · Weekly #4
1. **Crescent Island PMT v4 makes telemetry/crashlog/FW callbacks explicit runtime-PM users.**
   - Source: https://lwn.net/Articles/1092225/ (2026-09-01)
   - Change: Xe PMT access uses a shared MMIO window with driver callbacks/index selection; crashlog/telemetry access must request the proper power state, telemetry only exists while the device is powered, and firmware-backed discovery uses late binding for FW readiness.
   - KMD impact: the PM-active set must include telemetry/hwmon/crashlog and firmware-backed diagnostic callbacks, not only job/ioctl/IRQ paths. The first runtime-PM quiesce matrix should define whether each diagnostic path holds a PM ref, can wake the device, must wait for FW readiness, or should return unavailable during suspend/recovery.
   - Priority: **Include in the first runtime-PM implementation; complex governor remains later.**

### 2026-08-29 · Weekly #3
1. **Imagination GPU runtime-PM fix shows IRQ/suspend ordering is a first-class PM correctness problem.**
   - Source: https://ubuntu.com/security/CVE-2026-23469
   - Change: runtime suspend could power down the GPU while a threaded IRQ handler on another CPU was still accessing GPU registers, causing SError/panic. The fix synchronizes IRQ handling before suspend and removes ad-hoc IRQ-side runtime-resume logic that could deadlock with the PM lock.
   - KMD impact: PM active lifetime must include IRQ/threaded IRQ, FW callbacks, fault workers, reset workers and other asynchronous contexts that can touch power-gated state, not only job/ioctl references. Suspend needs an explicit quiesce/drain matrix.
   - Priority: **Build the quiesce matrix in the first runtime-PM implementation; complex governor remains later.**

### 2026-08-15 · Weekly #1
1. **No high-value direction-changing mechanism appeared after the previous run; keep measurement/lifetime-first.**
   - Reference: https://docs.kernel.org/next/gpu/xe/xe_pm.html
   - Observation: current Xe Runtime PM documentation continues to emphasize outer-layer PM references around IOCTL, sysfs/debugfs, dma-buf sharing and GPU execution; D3Cold eligibility is also constrained by VRAM and PCI hierarchy state.
   - KMD impact: solve PM-reference lifetime, reclaim/suspend interaction, resource ordering and resume correctness before complex governors. Telemetry remains a shared substrate for both DVFS and profiling.
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **No high-value direction-changing mechanism appeared in this short window; keep measurement/lifetime-first.**
   - Reference: https://docs.kernel.org/gpu/xe/xe_pm.html
   - KMD impact: telemetry should be a reusable substrate shared by DVFS and profiling; runtime PM must first solve active references, resource ordering and resume correctness.
   - Priority: **Now.**

2. **V3D Runtime PM remains a useful current implementation case study.**
   - Source: https://lwn.net/Articles/1059534/
   - Change: the upstream series shows the concrete work needed to disable GPU clocks while idle, including firmware-clock hooks and driver resource ordering.
   - KMD impact: treat first PM enablement as a lifecycle/correctness project, not simply a register programming task.
   - Priority: **Implementation reference now.**

### 2026-08-08 · Test #2
1. **Keep PM telemetry reusable by both policy and profiling.**
   - Source: https://docs.amd.com/r/en-US/57368-uProf-user-guide/7.13.1.-GPU-Profiling
   - Priority: **6–12 months if PMU counters exist.**
2. **Firmware-managed actuation remains the safer architecture boundary.**
   - Priority: **Now for interface design.**

### 2026-08-08 · Test #1
1. **Intel Xe integrates runtime PM with PCI D-states and VRAM constraints.**
2. **Firmware-managed frequency policy remains mainstream.**
3. **Do not start with a complex governor.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
