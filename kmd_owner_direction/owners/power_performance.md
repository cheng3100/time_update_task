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
### 2026-08-08

1. **Intel Xe keeps runtime PM integrated with PCI D-states and VRAM constraints.**
   - Source: Linux Xe Runtime Power Management: https://www.kernel.org/doc/html/latest/gpu/xe/xe_pm.html
   - Change: Xe models system suspend and opportunistic D3hot/D3cold runtime suspend, and can gate D3cold based on runtime conditions such as VRAM usage. The docs also emphasize taking PM references at outer call paths such as ioctl, dma-buf and GPU execution.
   - KMD impact: PM is not just clock programming; it needs clear lifetime/refcount boundaries around MM, execution and PCI state transitions.
   - Priority: **Now** for architecture, after utilization accounting is trustworthy.

2. **Firmware-managed frequency policy remains a mainstream GPU architecture.**
   - Source: Xe GuC firmware / GT frequency documentation: https://www.kernel.org/doc/html/next/gpu/xe/xe_firmware.html and https://www.kernel.org/doc/html/latest/gpu/xe/xe_gt_freq.html
   - Change: GuC SLPC handles connected power-conservation features while PCODE remains the final frequency decision maker; host KMD exposes min/max and telemetry instead of implementing every control loop itself.
   - KMD impact: define a clean KMD↔FW PM protocol and keep policy ownership explicit; this also intersects the Firmware/Control Plane owner.
   - Priority: **6–12 months** if FW frequency control is available.

3. **Do not start with a complex governor.**
   - Industry implication: upstream designs reinforce a layered sequence: measurement first, then bounded host policy, then firmware/hardware actuation.
   - KMD impact: first deliver reproducible busy/idle/utilization and frequency residency metrics so DVFS decisions can be validated.
   - Priority: **Now**.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
