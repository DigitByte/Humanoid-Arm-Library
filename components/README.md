# Components Library

This folder is the reusable component catalog for humanoid arm development.

## Categories
- `actuators/`: motor + actuator module references.
- `gearboxes/`: transmission modules and reduction options.
- `joints/`: joint-level mechanical modules.
- `links/`: structural arm links.
- `base/`: root/base structures and fixtures.

Each component should include:
- `README.md` with design intent and interfaces.
- `component.yaml` with standardized metadata.
- Links to CAD, firmware, and control examples.

## Catalog Generation
- Run `../scripts/generate_components_catalog.sh` from this directory (or `./scripts/generate_components_catalog.sh` from repo root) to rebuild `CATALOG.md`.
