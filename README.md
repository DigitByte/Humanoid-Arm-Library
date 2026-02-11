# Humanoid Arm Library

Humanoid robotic arm component library built on modular actuator and gearbox architecture.

## Library Objective

This repository is the humanoid-arm extension of the Hazebatronics actuator ecosystem.
It is structured to let you reuse and scale components across designs (single-joint tests, 3-DOF modules, and larger arm assemblies).

## What This Library Contains

- Component catalog for actuators, gearboxes, joints, links, and base modules.
- Assembly definitions that reference reusable component IDs.
- Mechanical CAD assets for arm structures and joints.
- Python control scripts for motion bring-up and validation.

## Repository Structure

```text
humanoid-robot-arm/
├── components/
│   ├── actuators/
│   ├── gearboxes/
│   ├── joints/
│   ├── links/
│   └── base/
├── assemblies/
│   ├── arm-3dof-v1/
│   └── parts-map/
├── mechanical/
│   └── cad/
│       └── model/
├── software/
│   └── python/
│       └── code/
├── electronics/
│   ├── firmware/
│   └── hardware/
└── docs/
    ├── library/
    ├── overview.md
    └── repository-map.md
```

## Core Library Artifacts

### Component Definitions
- `components/*/*/component.yaml`: machine-readable component metadata.
- `components/*/*/README.md`: human-readable intent, interfaces, and usage notes.

### Assembly Definitions
- `assemblies/arm-3dof-v1/README.md`: reference 3-DOF composition.
- `assemblies/parts-map/parts-map.csv`: mapping from CAD part names to component IDs.

### CAD + Control Assets
- `mechanical/cad/model/`: STL geometry for links, joints, and base parts.
- `software/python/code/`: control examples (`sine-wave.py`, `curl.py`, `three-actuators.py`).

## Component Index

- `components/CATALOG.md`
- Regenerate with: `./scripts/generate_components_catalog.sh`

## Assembly BOM

- `assemblies/arm-3dof-v1/BOM.md`
- `assemblies/arm-3dof-v1/BOM.csv`
