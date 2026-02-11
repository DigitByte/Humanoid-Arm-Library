# Humanoid Robotic Arms

**Click on the links below for detailed information**

## Software & Control

| Control Examples | Motion Planning | Communication Protocols | System Architecture |
|------------------|-----------------|-------------------------|---------------------|
| [![Control Examples](docs/images/placeholder_control_examples.jpg)](#control-examples) | [![Motion Planning](docs/images/placeholder_motion_planning.jpg)](#motion-planning) | [![Communication](docs/images/placeholder_communication.jpg)](#communication-protocols) | [![Architecture](docs/images/placeholder_architecture.jpg)](#system-architecture) |

## Mechanical Systems

| 3-DOF Arm Assembly | 5-DOF Arm Assembly | 7-DOF Full Arm | Gripper Integration |
|--------------------|--------------------|-----------------|--------------------|
| [![3-DOF Arm](docs/images/placeholder_3dof_arm.jpg)](#3-dof-arm-assembly) | [![5-DOF Arm](docs/images/placeholder_5dof_arm.jpg)](#5-dof-arm-assembly) | [![7-DOF Arm](docs/images/placeholder_7dof_arm.jpg)](#7-dof-full-arm) | [![Gripper](docs/images/placeholder_gripper.jpg)](#gripper-integration) |

| Actuator Module | Joint Assemblies | Transmission System | Structural Components |
|-----------------|------------------|---------------------|----------------------|
| [![Actuator Module](docs/images/placeholder_actuator_module.jpg)](#actuator-module) | [![Joint Assemblies](docs/images/placeholder_joint_assemblies.jpg)](#joint-assemblies) | [![Transmission](docs/images/placeholder_transmission.jpg)](#transmission-system) | [![Structural](docs/images/placeholder_structural.jpg)](#structural-components) |

## Electronics & Wiring

| CAN Bus Configuration | Power Distribution | Sensor Integration | Wiring Harness |
|----------------------|--------------------|--------------------|----------------|
| [![CAN Bus](docs/images/placeholder_can_bus.jpg)](#can-bus-configuration) | [![Power](docs/images/placeholder_power.jpg)](#power-distribution) | [![Sensors](docs/images/placeholder_sensors.jpg)](#sensor-integration) | [![Wiring](docs/images/placeholder_wiring.jpg)](#wiring-harness) |

## Assembly & Testing

| Actuator Preparation | Module Assembly | System Integration | Performance Testing |
|---------------------|-----------------|--------------------|--------------------|
| [![Actuator Prep](docs/images/placeholder_actuator_prep.jpg)](#actuator-preparation) | [![Module Assembly](docs/images/placeholder_module_assembly.jpg)](#module-assembly) | [![Integration](docs/images/placeholder_integration.jpg)](#system-integration) | [![Testing](docs/images/placeholder_testing.jpg)](#performance-testing) |

## Tools & Resources

| Mechanical Tools | Electronics Tools | 3D Printed Parts | Machined Components |
|------------------|-------------------|------------------|---------------------|
| [![Mechanical Tools](docs/images/placeholder_mech_tools.jpg)](#mechanical-tools) | [![Electronics Tools](docs/images/placeholder_elec_tools.jpg)](#electronics-tools) | [![3D Prints](docs/images/placeholder_3d_prints.jpg)](#3d-printed-parts) | [![Machined Parts](docs/images/placeholder_machined.jpg)](#machined-components) |

## Documentation

| Hardware Setup | Software Setup | Calibration | Troubleshooting |
|----------------|----------------|-------------|-----------------|
| [![Hardware Setup](docs/images/placeholder_hw_setup.jpg)](#hardware-setup) | [![Software Setup](docs/images/placeholder_sw_setup.jpg)](#software-setup) | [![Calibration](docs/images/placeholder_calibration.jpg)](#calibration) | [![Troubleshooting](docs/images/placeholder_troubleshooting.jpg)](#troubleshooting) |

---

## Project Overview

This repository contains comprehensive documentation, control software, and mechanical designs for humanoid robotic arms built using MyActuator RMD series actuators. The project emphasizes:

- **Modularity**: Scalable from 2-DOF to 7-DOF configurations
- **Open Development**: Complete documentation and example code
- **Real-time Control**: CAN bus communication at up to 1 kHz
- **Tested Solutions**: All examples verified on physical hardware

### System Specifications

**Actuators**: MyActuator RMD-X series
**Communication**: CAN 2.0B @ 1 Mbps
**Control Software**: Python-based (myactuator_rmd_py)
**Real-time Performance**: 100-500 Hz control loops
**Supported Platforms**: Linux (Raspberry Pi, x86)

---

## Getting Started

### Quick Start Guide

1. **Hardware Prerequisites**
   - MyActuator RMD actuators (tested with RMD-X6, RMD-X8)
   - CAN interface adapter
   - 24V-48V power supply
   - Linux system with CAN support

2. **Software Installation**
   ```bash
   pip install myactuator-rmd-py numpy
   ```

3. **CAN Interface Setup**
   ```bash
   sudo ip link set can0 type can bitrate 1000000
   sudo ip link set up can0
   ```

4. **Run Your First Example**
   ```bash
   python examples/basic_position_control.py
   ```

### Repository Structure

```
humanoid-robotic-arms/
├── docs/                    # Detailed documentation
│   ├── hardware/           # Mechanical and electrical docs
│   ├── software/           # Control and programming guides
│   ├── assembly/           # Step-by-step assembly instructions
│   └── images/             # Documentation images
├── examples/               # Working code examples
│   ├── basic/             # Simple single-actuator examples
│   ├── multi_joint/       # Multi-DOF coordination
│   └── advanced/          # Complex motion patterns
├── src/                   # Reusable libraries (future)
├── cad/                   # Mechanical design files (future)
│   ├── step/             # STEP files
│   └── stl/              # STL files for 3D printing
└── tests/                # Validation and test scripts

```

---

## More Information

[Project Website](#) (Coming Soon)
[Video Demonstrations](#) (Coming Soon)
[Community Forum](#) (Coming Soon)
[Research Papers](#) (Coming Soon)
[Hardware Documentation](docs/hardware/)
[Software Documentation](docs/software/)

---

## Contributing

We welcome contributions! This project is designed to grow over time as an encyclopedia of humanoid arm development. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- 📝 **Documentation**: Improve or expand existing docs
- 💻 **Code Examples**: Share your control implementations
- 🔧 **Hardware Designs**: Contribute mechanical or electrical designs
- 🐛 **Bug Reports**: Help us identify and fix issues
- 💡 **Feature Requests**: Suggest new capabilities

---

## Authors

Damien Delgado

## License

BSD 3-Clause License - See [LICENSE](LICENSE) for details

## Copyright

Copyright (c) 2026, Damien Delgado

---

## Acknowledgments

- MyActuator for actuator hardware and documentation
- Open Dynamic Robot Initiative for inspiration and design patterns
- The open-source robotics community

---

**Status**: 🟢 Active Development
**Version**: 0.1.0
**Last Updated**: January 2026

---

## Safety Notice

⚠️ **Important**: Robotic systems can be dangerous. Always:
- Implement emergency stops
- Test in controlled environments
- Follow proper power-down procedures
- Keep clear of moving parts during operation
- Read all documentation before operation

---

## Contact

For questions, collaboration, or support:
- Open an [Issue](../../issues)
- Join our [Discussions](../../discussions)
- Email: drdelgado9@outlook.com