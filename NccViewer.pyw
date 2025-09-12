
"""
NCC Viewer Application - Noble Gas Isotope Ratio Analysis Tool

A Python Qt-based application that provides a graphical interface for calculating
and viewing NCC (Nano Cubic Centimetres) values from helium isotope
mass spectrometer data. This application processes data files from Stanford SRS
RGA mass spectrometers to determine 3He/4He ratios and calculate nucleogenic
corrections for noble gas samples.

The application provides functionality for:
- Loading and processing helium isotope data files
- Calculating blank corrections from line blank measurements
- Computing NCC values based on depletion factors and pipette calibrations
- Visualizing isotope ratio data and trends
- Generating NCC analysis reports

Usage:
    Run this file directly to start the NCC Viewer application:
    python NccViewer.pyw

Author: Gary Twinn
"""
import sys
from PySide6.QtWidgets import QApplication
from logmanager import logger
from app_control import VERSION
from ui.ncc_calc_form import NccCalcUI

logger.info('****** Ncc Viewer version %s started ******', VERSION)
app = QApplication(sys.argv)
mainform = NccCalcUI()
mainform.show()

sys.exit(app.exec())
