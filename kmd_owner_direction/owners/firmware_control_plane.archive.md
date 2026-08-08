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
### 2026-08-08 · Test #2
1. **Firmware-version isolation should be an explicit architectural invariant.**
   - Source: Nova task list: https://docs.kernel.org/gpu/nova/core/todo.html
   - Change: the GSP-RM API is explicitly described as unstable across firmware versions in both structures and semantics.
   - KMD impact: centralize version translation/capability negotiation below a stable KMD-facing service API; prohibit scattered feature-level firmware-version conditionals.
   - Priority: **Now.**

2. **Firmware log export belongs in the control-plane contract, not only in ad-hoc debug code.**
   - Source: Nova task list, GSP log-buffer export item.
   - KMD impact: define a standard FW health/log service usable during normal runtime, crash recovery and probe failure; Reliability consumes it for crash evidence.
   - Priority: **6–12 months, after the base async protocol.**

3. **`nova-core` continues to validate a reusable lower control layer for DRM and VFIO/vGPU clients.**
   - Source: https://docs.kernel.org/gpu/nova/index.html
   - KMD impact: keep resource ownership and FW lifecycle beneath client/uAPI layers so future virtualization or alternate upper drivers reuse the same control plane.
   - Priority: **Now for architecture.**

### 2026-08-08 · Test #1
1. **Linux Nova makes firmware abstraction a first-class driver architecture.**
2. **GSP firmware API instability is recognized as a core design problem.**
3. **Firmware is becoming a power/performance control authority.**

## Living focus
Expand toward firmware lifecycle, resource ownership, HW-management offload and firmware-centric KMD architecture. Reliability owns system-level failure containment/recovery policy; this owner owns firmware communication/lifecycle/state mechanisms.
