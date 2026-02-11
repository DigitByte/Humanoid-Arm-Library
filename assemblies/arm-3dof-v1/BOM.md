# Arm 3-DOF v1 BOM

Curated bill of materials for the `arm-3dof-v1` reference assembly.

## Scope

This BOM combines:
- Component-library parts (tracked by component ID).
- Initial hardware/electrical placeholders needed for bench bring-up.

## BOM Table

| Line | Type | ID / Spec | Description | Qty | Notes |
|---|---|---|---|---:|---|
| 1 | component | `BAS-PLT-001` | Base Plate v1 | 1 | Main fixture base |
| 2 | component | `LNK-UPR-001` | Upper Limb v1 | 1 | Primary upper arm link |
| 3 | component | `LNK-LWR-001` | Lower Limb v1 | 1 | Primary forearm link |
| 4 | component | `JNT-ELB-001` | Elbow Joint v1 | 1 | Elbow articulation |
| 5 | component | `JNT-WRS-001` | Wrist Joint v1 | 1 | Wrist articulation |
| 6 | component | `ACT-RMDX-001` | RMD-X actuator node | 3 | Assumes 3-axis configuration |
| 7 | component | `GBX-PLN-001` | Planetary gearbox module | 3 | Placeholder until ratio is finalized |
| 8 | hardware | `M5x16_socket_head_cap_screw` | Structural fastener | 24 | Verify by final CAD stackups |
| 9 | hardware | `M5_nyloc_nut` | Fastener nut | 24 | Pair with M5 bolts |
| 10 | hardware | `M5_flat_washer` | Flat washer | 48 | Typical two-per-bolt |
| 11 | hardware | `6703-2RS_bearing` | Bearing support | 6 | Validate after final bearing layout |
| 12 | electrical | `can_bus_harness` | CAN wiring harness | 1 set | Trunk + branch leads |
| 13 | electrical | `24V_to_48V_dc_supply` | Power supply | 1 | Size for peak current |

## Files

- Machine-readable BOM: `assemblies/arm-3dof-v1/BOM.csv`
- Part-to-CAD map: `assemblies/parts-map/parts-map.csv`
