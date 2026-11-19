import os
os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
import unittest
from calibration import parse_calibration
from telemetry import parse_rate
class OutputRatesTest(unittest.TestCase):
 def test_calibration_targets(self):
  for fs in (26667,13333,6667,3333):
   target=fs*5
   self.assertIsNotNone(parse_calibration(f'OK CAL FACE X+ samples={target}'))
   self.assertIsNotNone(parse_calibration(f'CAL STATUS session=1 mask=0 face=0 samples=0 target={target} solved=0 pending=0'))
 def test_dropdown_commands_and_ack(self):
  from PySide6 import QtWidgets
  from app import Window,Receiver
  q=QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
  win=Window();win.timer.stop();w=Receiver('TEST',2000000);w.connected=True;w.is_alive=lambda:True;win.worker=w
  w.log('RATE current=26667 supported=26667,13333,6667,3333');win.update_data()
  self.assertEqual(win.rate_combo.count(),4)
  for i,rate in enumerate((26667,13333,6667,3333)):
   self.assertEqual(win.rate_combo.itemData(i),rate)
  self.assertIn('滤波降采样',win.rate_combo.itemText(1));self.assertTrue(win.rate_apply.isEnabled())
  win.rate_combo.setCurrentIndex(1);win.apply_rate()
  sent=[]
  while not w.commands.empty():sent.append(w.commands.get_nowait()[0])
  self.assertIn('RATE 13333',sent)
  w.log('OK RATE fs=13333');win.update_data()
  self.assertEqual(win.fs,13333);self.assertIsNone(win.rate_pending)
  win.worker=None;win.close();q.processEvents()
