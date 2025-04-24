## Overview
PyMS is a desktop application that provides a Graphical User Interface (GUI) for managing cycles of batches in the
UCL Oxide Line. Built with Python and the Qt6 UI framework (via PySide6), PyMS offers intuitive control and monitoring
capabilities for laboratory processes.
## Installation
### Windows
Download and run the installer package: [PyMS-installer.exe](./distribution/PyMS-installer.exe)
### Requirements
- Python 3.8+
- PySide6
- Additional dependencies listed in `requirements.txt`

## Application Components

| Component | Description |
| --- | --- |
| `PyMS.pyw` | Main application for controlling batch cycles |
| `NccViewer.pyw` | Utility for viewing NCC values for run samples and generating new NCC files based on line blanks |
| `CycleEditor.pyw` | Editor for cycle steps - add, modify, or delete tasks at specific run times |
| `imagefiler.py` | Lists all open windows (useful for identifying window names when using applications that display camera images) |
| `settings.json` | Configuration file for laser settings, host addresses, and data file locations |
## Documentation
- [User Manual](./manual.pdf) - Complete application usage instructions
- [API Documentation](./docs/readme.md) - Python module documentation
- [Changelog](./changelog.txt) - History of updates and changes

## Features
- Intuitive interface for batch cycle management
- Real-time monitoring of laboratory processes
- NCC value visualization and file generation
- Flexible cycle editing capabilities
- Integration with laboratory imaging systems

## Getting Started
1. Install PyMS using the provided installer
2. Configure your settings in `settings.json`
3. Launch the application using `PyMS.pyw`
4. Refer to the manual for detailed usage instructions

## Support and Contribution
For support, please contact [support email or contact information]
## License
[License information](./LICENSE)
