# GPU Reliability / Recovery / RAS

## Summary (stable)
Own detection, diagnosis, containment and recovery of GPU faults, plus production RAS mechanisms. The goal is progressively finer recovery rather than always resetting the whole device.

## Candidate sub-directions
- firmware/GPU heartbeat and watchdog
- job/queue/engine/firmware hang detection
- hang snapshot: registers, rings, queues, contexts, VM/PTE and firmware state
- devcoredump and structured crash reports
- persistent reset reason and fault attribution
- job abort, queue/context kill, engine/partial/full reset
- post-reset state restore and job replay
- firmware crash recovery coordination
- ECC CE/UE, poison, bad-page retirement/remapping
- PCIe AER, error counters and fault injection

## Current entry feature
**Hang snapshot + devcoredump + persistent reset reason + heartbeat/watchdog.**

## Living focus
Evolve from global reset toward context/queue/engine-level fault containment and recovery, while keeping boundaries clear with Firmware Control Plane.
