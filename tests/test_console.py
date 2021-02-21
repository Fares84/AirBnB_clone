#!/usr/bin/python3
"""
   TestConsole module
"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand
from models import storage
