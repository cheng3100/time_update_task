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
GPU busy/idle + utilization accounting → basic DVFS/runtime PM.

### Near-term feature path
Reliable busy/idle accounting → per-engine utilization → frequency/residency telemetry → basic firmware-controlled DVFS → runtime PM → thermal/power-cap policy.

## Industry Updates
### 2026-08-08 · Test #2
1. **Keep PM telemetry reusable by both policy and profiling.**
   - Source: AMD uProf 5.3 GPU Profiling (2026-06-17): https://docs.amd.com/r/en-US/57368-uProf-user-guide/7.13.1.-GPU-Profiling
   - Change: production profiling stacks consume GPU hardware events and derived metrics through ROCm/rocprofiler.
   - KMD impact: utilization/performance counters should not be hard-wired only into DVFS; expose a clean counter/telemetry layer reusable by Observability/Profiling.
   - Priority: **6–12 months if PMU counters exist.**

2. **Firmware-managed actuation remains the safer architecture boundary.**
   - Sources: Linux Xe firmware/GT-frequency docs and Nova architecture.
   - KMD impact: host KMD should own measurement, constraints and policy contract while FW/HW can own low-level actuation where appropriate.
   - Priority: **Now for interface design.**

### 2026-08-08 · Test #1
1. **Intel Xe integrates runtime PM with PCI D-states and VRAM constraints.**
   - Priority: **Now** for architecture.
2. **Firmware-managed frequency policy remains mainstream.**
   - Priority: **6–12 months** if FW frequency control is available.
3. **Do not start with a complex governor.**
   - Priority: **Now** — measurement first.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
