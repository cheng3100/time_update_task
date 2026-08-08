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
**Versioned KMD-Firmware Async Control Protocol + Capability Negotiation.**

Deliver protocol version, capability query, command/event IDs, sequence number, async completion, standard errors/timeouts, unsupported-feature handling, firmware restart detection, re-handshake and state resynchronization.

### Near-term feature path
Versioned message contract → capability negotiation → async request/completion → timeout/error semantics → FW generation/restart detection → re-handshake → state reconciliation → resource ownership → HW-management offload.

## Industry Updates
### 2026-08-08

1. **Linux Nova is making firmware abstraction a first-class driver architecture.**
   - Source: Linux Nova documentation: https://docs.kernel.org/gpu/nova/index.html
   - Change: `nova-core` is a first-level driver around GPU hardware and GSP firmware, intended to provide a common base to upper drivers such as DRM and VFIO/vGPU.
   - KMD impact: a self-developed GPU should treat FW protocol/version/resource ownership as an architectural layer, not scattered mailbox helpers inside each feature.
   - Priority: **Now**.

2. **GSP firmware API instability is explicitly recognized as a core design problem.**
   - Source: Nova task list: https://docs.kernel.org/gpu/nova/core/todo.html
   - Change: Nova documentation explicitly notes that GSP-RM firmware API structures and semantics can incompatibly change between versions, motivating a firmware abstraction layer.
   - KMD impact: use protocol version + capability negotiation and keep firmware-version-specific translation below a stable KMD-facing API. Avoid widespread `if (fw_version >= X)` checks.
   - Priority: **Now**.

3. **Firmware is also becoming a power/performance control authority.**
   - Source: Intel Xe firmware documentation: https://www.kernel.org/doc/html/next/gpu/xe/xe_firmware.html
   - Change: GuC Power Conservation/SLPC handles frequency and Render-C-state policy through a host programming interface.
   - KMD impact: control-plane design should support multiple service classes (PM, reset, scheduling, telemetry) with consistent async/error/version semantics rather than feature-specific protocols.
   - Priority: **6–12 months**, after the base protocol lands.

## Living focus
Expand toward firmware lifecycle, resource ownership, HW-management offload and firmware-centric KMD architecture. Reliability owns system-level failure containment/recovery policy; this owner owns firmware communication/lifecycle/state mechanisms.
