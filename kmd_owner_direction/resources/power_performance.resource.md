# Power / Performance — Learning Resources

## Busy/idle / per-engine utilization
- [Xe GT frequency documentation](https://docs.kernel.org/gpu/xe/xe_gt_freq.html) — Useful for seeing how frequency controls and telemetry are exposed without hiding policy boundaries.

## Runtime PM / system suspend-resume / PCI D-states
- [Xe Power Management](https://docs.kernel.org/gpu/xe/xe_pm.html) — High-value reference for runtime PM references, D3hot/D3cold, VRAM constraints and suspend/resume interaction.

## Clock/power gating / idle residency
- [Xe Power Management](https://docs.kernel.org/gpu/xe/xe_pm.html) — Read together with firmware docs to understand host-vs-firmware ownership of low-power states.

## DVFS / OPP / firmware PM protocol
- [Xe firmware documentation](https://docs.kernel.org/gpu/xe/xe_firmware.html) — GuC/SLPC/PCODE is a strong example of firmware-centric GPU frequency policy.

## Thermal throttling / power cap
- [AMDGPU driver documentation](https://docs.kernel.org/gpu/amdgpu/index.html) — Use the power/SMU sections as a production-driver reference for telemetry, throttling and firmware-mediated control.

## Frequency residency / memory bandwidth telemetry
- [NVIDIA Tegra241 PMU](https://docs.kernel.org/admin-guide/perf/nvidia-tegra241-pmu.html) — Stable example of standard perf PMUs exposing bandwidth, latency and utilization across GPU-adjacent fabrics.

## PCIe ASPM / link power
- [Linux PCI driver documentation](https://docs.kernel.org/PCI/pci.html) — Baseline PCI lifecycle/reference; pair with PCIe spec/platform docs for ASPM details.
