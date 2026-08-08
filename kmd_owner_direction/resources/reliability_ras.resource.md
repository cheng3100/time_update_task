# Reliability / Recovery / RAS — Learning Resources

## Heartbeat / watchdog / hang detection
- [Xe Device Coredump](https://docs.kernel.org/gpu/xe/xe_devcoredump.html) — Start here for the recovery boundary between detecting a hang, freezing diagnostic state and performing reset.

## Hang snapshot / register-ring-context-VM-FW dump
- [Xe Device Coredump](https://docs.kernel.org/gpu/xe/xe_devcoredump.html) — Canonical current example of snapshot-at-failure rather than lazy post-reset collection.
- [Nova task list — GSP log buffers](https://docs.kernel.org/gpu/nova/core/todo.html) — Useful reminder that FW logs and even probe/boot failures belong in production diagnostics.

## devcoredump / structured crash report / reset reason
- [Device coredump framework](https://docs.kernel.org/driver-api/infrastructure.html) — Kernel infrastructure behind standard device crash-dump delivery; useful before designing a vendor-private channel.

## Job / queue / context / engine / full-device recovery
- [DRM GPU scheduler](https://docs.kernel.org/gpu/drm-mm.html) — Read scheduler timeout/recovery concepts together with driver-specific recovery code to understand what state can be isolated before global reset.

## Post-reset restore / replay
- [Xe driver documentation](https://docs.kernel.org/gpu/xe/index.html) — Broad production-driver reference for reset, VM, execution and state reconstruction interactions.

## ECC CE/UE / bad-page retirement / fault injection
- [AMDGPU RAS](https://docs.kernel.org/gpu/amdgpu/ras.html) — Strong production reference for block-level CE/UE reporting, bad pages, poison handling and fault injection.

## PCIe AER
- [PCIe AER HOWTO](https://docs.kernel.org/PCI/pcieaer-howto.html) — Canonical Linux reference for PCIe error reporting/recovery and driver participation.
