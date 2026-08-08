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

## Industry Updates
### 2026-08-08
- Upstream GPU drivers such as Intel Xe combine runtime PM, low-power residency and firmware-managed frequency policy into a complete PM architecture, reinforcing the measurement → policy → FW/HW-control model.
- Follow-up: **Now** — establish verifiable utilization accounting before introducing complex governors.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
