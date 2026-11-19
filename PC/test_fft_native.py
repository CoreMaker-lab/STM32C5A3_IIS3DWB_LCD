import unittest
from telemetry import parse_telemetry
class NativeTelemetryTest(unittest.TestCase):
 def test_real_device_high_frequency_reply(self):
  row='FFT valid=1 hz_x100=1013033,1317725,1304704 amp_mg_x100=272,240,250 windows=662 skip=12 age_ms=2 step_max_ms=2'
  event=parse_telemetry(row)
  self.assertEqual(event[0],'fft');self.assertEqual(event[1]['hz'],[10130.33,13177.25,13047.04])
 def test_out_of_native_band_rejected(self):
  self.assertIsNone(parse_telemetry('FFT valid=1 hz_x100=9999999,0,0 amp_mg_x100=0,0,0 windows=0 skip=0 age_ms=0 step_max_ms=0'))
