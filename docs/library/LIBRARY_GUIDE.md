# Humanoid Arm Library Guide

## Goal
Maintain this repository as a reusable component library for humanoid arm development, with traceable parts, interfaces, and validation code.

## Library Rules
1. Every component gets a unique `id` in `component.yaml`.
2. Every component README includes interfaces and linked artifacts.
3. Assemblies reference component IDs, not only raw filenames.
4. Control scripts should map to assembly-level validation steps.

## Adding a New Component
1. Create `components/<category>/<component-name>/`.
2. Add `component.yaml` and `README.md`.
3. Add CAD/electronics/software links.
4. Register mapping in `assemblies/parts-map/parts-map.csv` if used in an assembly.
