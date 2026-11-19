import os
os.environ.setdefault('QT_QPA_PLATFORM','offscreen')
import unittest
import numpy as np
from protocol import Parser,encode,spectrum
from calibration import parse_calibration
from telemetry import parse_rate
class IIS3DWBTests(unittest.TestCase):
 def test_native_calibration(self):
  self.assertIsNotNone(parse_calibration('OK CAL FACE Z+ samples=133335'))
  self.assertIsNotNone(parse_calibration('CAL STATUS session=1 mask=0 face=4 samples=133334 target=133335 solved=0 pending=0'))
  self.assertIsNone(parse_calibration('OK CAL FACE Z+ samples=9999999'))
  self.assertIsNone(parse_calibration('CAL STATUS session=1 mask=0 face=4 samples=0 target=9999999 solved=0 pending=0'))
  self.assertEqual(parse_rate('RATE current=26667 supported=26667')[1]['supported'],(26667,))
 def test_fragmentation_and_scaling(self):
  raw=np.array([[10526,-10526,0]]*32);wire=encode(raw,0,26667,0)
  p=Parser();packets=[]
  for b in wire:
   rows,_=p.feed(bytes([b]));packets+=rows
  self.assertEqual(p.errors,0);self.assertEqual(packets[0][1],26667)
  self.assertAlmostEqual(packets[0][4][0,0]*.095,999.97,places=2)
 def test_native_fft(self):
  t=np.arange(1024);y=np.column_stack([100*np.sin(2*np.pi*40*t/1024)]*3)
  f,a=spectrum(y,26667);self.assertAlmostEqual(f[np.argmax(a[:,0])],26667*40/1024)
  self.assertAlmostEqual(a[:,0].max(),100,places=2)
 def test_gap_clears_old_plot(self):
  from PySide6 import QtWidgets
  from app import Window,Receiver
  q=QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
  win=Window();win.timer.stop();win.nfft.setCurrentText('1024');w=Receiver('TEST',2000000);w.connected=True;w.is_alive=lambda:True;win.worker=w;win.fs=26667
  w.log('RATE current=26667 supported=26667');win.update_data()
  self.assertFalse(win.rate_apply.isEnabled());self.assertEqual(win.rate_combo.currentData(),26667)
  raw=np.ones((2048,3),dtype=np.int32)
  w.packets.put((0,26667,0,0,raw));win.update_data()
  self.assertTrue(len(win.spectra[0].getData()[0]))
  w.packets.put((2,26667,4096,1,raw[:1]));win.update_data()
  self.assertEqual(len(win.data),1);self.assertIsNone(win.spectra[0].getData()[0]);self.assertIsNone(win.curves[0].getData()[0])
  self.assertIn('不足',win.link_note.text());self.assertEqual(win.gaps,1)
  win.worker=None;win.close();q.processEvents()
