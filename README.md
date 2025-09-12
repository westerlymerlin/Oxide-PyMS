## Overview
PyMS is a desktop application that provides a Graphical User Interface (GUI) for managing cycles of batches in an 
Oxide Helium Extraction Line. Built with Python and the Qt6 UI framework (via PySide6), PyMS offers intuitive control and monitoring
capabilities for laboratory processes.

## 🚀 Features

- Intuitive graphical interface for batch cycle management
- Real-time monitoring of cycle processes
- NCC value viewing and generation
- Cycle step editing capabilities

### Requirements
- Python 3.8+
- PySide6
- Additional dependencies listed in `requirements.txt`

## 📋 Application Components

| Component | Description |
| --- | --- |
| `PyMS.pyw` | Main application for controlling batch cycles |
| `NccViewer.pyw` | Utility for viewing NCC values for run samples and generating new NCC files based on line blanks |
| `CycleEditor.pyw` | Editor for cycle steps - add, modify, or delete tasks at specific run times |
| `imagefiler.py` | Lists all open windows (useful for identifying window names when using applications that display camera images) |
| `settings.json` | Configuration file for laser settings, host addresses, and data file locations |

## 📖 Documentation
- [User Manual](./manual.pdf) - Complete application usage instructions
- [API Documentation](./docs/readme.md) - Python module documentation
- [Changelog](./changelog.txt) - History of updates and changes

## 📖 Features
- Intuitive interface for batch cycle management
- Real-time monitoring of laboratory processes
- NCC value visualization and file generation
- Flexible cycle editing capabilities
- Integration with laboratory imaging systems

# 🔧 Installation

A windows installer is found in the [distribution](./distribution) folder.  
Download the file and run it (requires Windows 10 or higher)

## 🔧 Building a new version

To create a new version of PyMS, first clone the repo from Github using the command below:  
`git clone https://github.com/westerlymerlin/Oxide-PyMS.git`  
you will need to have Python 3.12 installed with all the dependencies listed in [requirements.txt](./requirements.txt).  
`pip install -r requirements.txt`  

In order to package the code into a windows application, you will need the latest version of **pyinstaller** and **pyinstaller_versionfile** and installed.  
`pip install pyinstaller pyinstaller_versionfile` 
You will need InstallForge installed to create the windows installer file - download and install from [**InstallForge.net**](https://installforge.net/download/ )

Please create a new branch in git for your edits. 
`git branch -b my-new-feature`    
Make your changes to the code in your favorite IDE and test them, once you are happy with the results you are ready to package the new version:  
1. Update the version number in the module app_control.py  
2. Add a new line to the `changelog.txt`  
3. Run the following command to package the application:  
`python -m ./packager/make.py`  
   The makefile will create the new packaged files and start sourceforge, you will need to click the build button to create the new installed into the ./distribution folder.

Please commit the changes you have made to git and push to the repository to git for version control.  
`git add .`  
`git commit -m "My commit message"`  
`git push origin my-new-feature`

There is a workflow that will update the docs files and create a pull request for the code owner to review and merge to the main branch.


--------------

#### Copyright (C) 2025 Gary Twinn

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program. If not, see <https://www.gnu.org/licenses/>.


## Author
**Dr Gary Twinn**  
GitHub: [github.com/westerlymerlin](https://github.com/westerlymerlin)

-------------
