# GPU Firmware / Control Plane Architecture

## Summary (stable)
Own the long-term KMD↔GPU system-firmware control plane. This is not basic firmware loading/bring-up; it is the protocol, lifecycle, capability and ownership architecture that lets KMD and firmware evolve independently.

## Candidate sub-directions
- versioned firmware ABI/protocol
- command/event namespace and shared-memory/ring/mailbox transport
- sequence IDs, async request/completion, timeout/cancellation and error model
- capability negotiation and backward/forward compatibility
- boot/handshake/version check, upgrade/rollback, hot restart/live recovery
- KMD↔FW resource ownership model
- state synchronization and reconciliation after restart
- firmware-centric initialization and engine management
- PM interface, reset orchestration and hardware-scheduler interface
- firmware health/heartbeat/crash dump
- firmware authentication and measurement mechanisms

## Current entry feature
**Versioned KMD-Firmware Async Control Protocol + Capability Negotiation + Boot/Reset Generation + Raw-ABI Translation/Validation.**

Deliver protocol version, capability query, command/event IDs, sequence number, async completion, standard errors/timeouts, unsupported-feature handling, explicit parser/validation and translation boundaries, firmware boot/reset phases, restart detection, generation isolation, re-handshake and state resynchronization.

### Near-term feature path
Versioned raw message contract → parser/validation → capability/translation → stable internal service API → async request/completion → timeout/error semantics → explicit boot/reset phases → FW generation/restart detection → state reconciliation → resource ownership → HW-management offload.

## Industry Updates
### 2026-08-29 · Weekly #3
1. **Nova r000 GSP ABI v2 makes a real firmware major-ABI transition visible.**
   - Source: https://lkml.iu.edu/2608.2/11372.html (2026-08-21)
   - Change: nova-core moves from the release-specific 570.144 GSP firmware toward an r000 ABI intended to stay stable across releases. The switch changes MCTP/NVDM transport, msgq v2 queue/doorbell semantics, load-and-execute events, GSP_INIT boot handshake, ucodes/state-monitor buffers and transport validation as a grouped protocol transition.
   - KMD impact: stable upper KMD services must not depend directly on raw firmware structs. Make the boundary explicit: raw FW ABI → parser/validator → version/capability translation → stable service model. Validate incoming version/vendor/length/sequence rather than assuming firmware correctness.
   - Priority: **Build the translation/validation boundary into the first protocol version.**

2. **The r000 series reinforces generation-aware boot/lifecycle design.**
   - Source: https://lkml.iu.edu/2608.2/05341.html
   - KMD impact: a major firmware generation can change queue pointers, boot events, init requests and memory reservations together. Treat firmware generation as a lifecycle boundary; old sequence/request/resource state must not survive a major transition implicitly.
   - Priority: **Now for architecture.**

### 2026-08-22 · Weekly #2
1. **Nova is starting to expose lower-layer GPU parameters to nova-drm through an explicit core interface.**
   - Source: https://lwn.net/Articles/1088246/ (v4, 2026-08-11)
   - Change: the series exports basic GPU properties from nova-core to nova-drm and builds a new GPU-info ioctl on top of a higher-ranked lifetime/private-data mechanism.
   - KMD impact: this is a concrete example of the next step after defining a firmware-independent lower layer: upper DRM/uAPI code should consume typed/stable capabilities and properties from the core rather than reach into FW/HW internals. For a self-developed KMD, capability negotiation should therefore feed a stable internal capability/property object that is the only input to upper feature layers.
   - Priority: **Design now.**

2. **Nova PRAMIN support demonstrates typed MMIO/window services as lower-layer ownership.**
   - Source: https://lwn.net/Articles/1087343/ (2026-08-05)
   - KMD impact: shared low-level address-window/MMIO services should have one owner and typed lifetime rules so upper modules cannot race window reprogramming or duplicate register semantics.
   - Priority: **Architecture reference.**

### 2026-08-15 · Weekly #1
1. **Nova devinit makes reset-time firmware phase boundaries concrete.**
   - Source: https://docs.kernel.org/next/gpu/nova/core/devinit.html
   - KMD impact: model RESET → SECURE_FW → DEVINIT → GFW_BOOT/FW_BOOT_COMPLETE → KMD_HANDSHAKE → SERVICE_READY rather than a single `fw_ready` bit; reset/restart advances generation.
   - Priority: **Design now.**

2. **nova-core continues to define a firmware-version-independent lower API for second-level drivers.**
   - Sources: https://docs.kernel.org/next/gpu/nova/index.html and https://docs.kernel.org/next/gpu/nova/core/guidelines.html
   - KMD impact: keep version translation, capabilities and firmware lifecycle below DRM/VFIO/other client layers.
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **Nova continues to make firmware-version-independent lower APIs an explicit architectural invariant.**
   - Source: https://docs.kernel.org/next/gpu/nova/core/guidelines.html
   - KMD impact: centralize translation/capability below a stable service API.
   - Priority: **Now.**

2. **A current source walkthrough makes Nova's two-layer control architecture easier to study.**
   - Source: https://hectorzelaya.dev/posts/nova-driver/part1-architecture-initialization-hardware-discovery/
   - Priority: **Learning/reference now.**

### 2026-08-08 · Test #2
1. **Firmware-version isolation should be an explicit architectural invariant.**
   - Source: https://docs.kernel.org/gpu/nova/core/todo.html
   - Priority: **Now.**
2. **Firmware log export belongs in the control-plane contract.**
   - Priority: **6–12 months after the base async protocol.**
3. **nova-core validates a reusable lower control layer.**
   - Priority: **Now.**

### 2026-08-08 · Test #1
1. **Linux Nova makes firmware abstraction a first-class driver architecture.**
2. **GSP firmware API instability is recognized as a core design problem.**
3. **Firmware is becoming a power/performance control authority.**

## Living focus
Expand toward firmware lifecycle, raw-ABI translation/validation, resource ownership, HW-management offload and firmware-centric KMD architecture. Reliability owns system-level failure containment/recovery policy; this owner owns firmware communication/lifecycle/state mechanisms.
