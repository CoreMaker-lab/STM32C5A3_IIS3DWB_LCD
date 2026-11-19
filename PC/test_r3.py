import unittest
class R2Diagnostics(unittest.TestCase):
 def test_old_caps_disabled_with_evidence(self):
  from PySide6 import QtWidgets
  from app import Window,Receiver
  q=QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
  win=Window();win.timer.stop();w=Receiver('TEST',6000000);w.connected=True;w.is_alive=lambda:True;win.worker=w
  w.log('RATE current=26667 supported=26667');win.update_data()
  self.assertIn('CRC定位 R6',win.windowTitle());self.assertEqual(win.rate_combo.count(),4)
  self.assertIn('supported=26667',win.rate_status.text())
  for i in range(1,4):self.assertFalse(win.rate_combo.model().item(i).isEnabled())
  self.assertFalse(win.rate_apply.isEnabled())
  w.log('FW IIS3DWB_PERF_R5 native=26667 stages=0,1,2,3')
  w.log('RATE current=26667 supported=26667,13333,6667,3333');win.update_data()
  self.assertIn('IIS3DWB_PERF_R5',win.build_label.text())
  for i in range(4):self.assertTrue(win.rate_combo.model().item(i).isEnabled())
  self.assertTrue(win.rate_apply.isEnabled())
  win.worker=None;win.close();q.processEvents()
