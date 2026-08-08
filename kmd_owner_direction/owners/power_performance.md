# GPU Power / Performance

## Summary (stable)
Own GPU power-state control and performance-management policy from utilization measurement through DVFS, runtime PM, thermal and power-budget control.

## Candidate sub-directions
- busy/idle and per-engine utilization accounting
- runtime PM and system suspend/resume
- clock gating, power gating and idle residency
- DVFS, OPP/performance states and firmware PM protocol
- thermal throttling and emergency thermal handling
- power telemetry and power cap
- frequency residency and memory-bandwidth utilization
- utilization-based and workload-aware boost/throttle policy
- PCIe ASPM/link-power integration

## Current entry feature
**GPU busy/idle + utilization accounting → basic DVFS/runtime PM closed loop.**

## Living focus
Track which counters and PM controls are available in hardware/firmware, then expand only when measurement and actuation are both reliable.
