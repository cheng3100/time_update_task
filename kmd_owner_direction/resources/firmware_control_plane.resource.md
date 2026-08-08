# Firmware / Control Plane — Learning Resources

## Versioned FW ABI / command-event namespace
- [Nova core guidelines](https://docs.kernel.org/next/gpu/nova/core/guidelines.html) — Excellent durable reference for one key principle: upper drivers should not see firmware-version-specific structures or semantics.

## Ring / mailbox / shared-memory transport / async completion
- [Nouveau GSP support documentation](https://docs.kernel.org/gpu/nouveau.html) — Useful production reference for GSP command/status queues and lower-level firmware communication concepts.

## Capability negotiation / compatibility / version translation
- [Nova core task list — GSP firmware abstraction](https://docs.kernel.org/gpu/nova/core/todo.html) — Explicitly explains why unstable GSP-RM APIs require a firmware-version abstraction layer.

## Boot / handshake / restart / upgrade / rollback
- [Nova VBIOS](https://docs.kernel.org/gpu/nova/core/vbios.html) — Deep reference for GPU boot-chain structure and how kernel driver startup depends on ROM and firmware images.

## Firmware security / authentication / measurement
- [Nova FWSEC](https://docs.kernel.org/gpu/nova/core/fwsec.html) — Strong reference for GPU secure-boot sequencing, firmware verification and privileged firmware roles.

## Resource ownership / state reconciliation
- [Nova core architecture](https://docs.kernel.org/gpu/nova/index.html) — Read the nova-core vs second-level-driver split to understand why resource ownership and FW lifecycle belong below DRM/VFIO clients.

## PM / reset / HW-scheduler services
- [Xe firmware documentation](https://docs.kernel.org/gpu/xe/xe_firmware.html) — Production reference for firmware-managed control services such as GuC scheduling and power management.

## Firmware health / logs / crash diagnostics
- [Nova core task list — GSP log buffers](https://docs.kernel.org/gpu/nova/core/todo.html) — Useful stable reminder that FW logs should survive probe failure and be part of driver diagnostics.
