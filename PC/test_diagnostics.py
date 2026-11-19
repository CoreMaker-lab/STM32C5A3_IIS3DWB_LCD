import unittest,tempfile,json,zlib,struct
from pathlib import Path
from protocol import Parser,encode
from diagnostics import Journal
class DiagnosticsTests(unittest.TestCase):
 def test_corrupt_frame_evidence_and_resync(self):
  first=encode([[1,2,3]]*32,10,26667,320)
  bad=bytearray(encode([[4,5,6]]*32,11,26667,352));bad[40]^=1
  good=encode([[7,8,9]]*32,12,26667,384)
  p=Parser();rows=[]
  for i in range(0,len(first+bad+good),113):
   a,_=p.feed((first+bad+good)[i:i+113]);rows+=a
  self.assertEqual([r[0] for r in rows],[10,12]);self.assertEqual(p.crc_errors,1)
  e=p.diagnostics[0];self.assertEqual(bytes.fromhex(e['wire_hex']),bad)
  self.assertEqual(e['previous']['seq'],10)
  self.assertEqual(e['computed_crc'],zlib.crc32(bad[:-4]))
  self.assertEqual(e['expected_crc'],struct.unpack('<I',bad[-4:])[0])
 def test_bad_header_and_bounded_evidence(self):
  bad=bytearray(encode([[1,2,3]]));bad[4]=99
  p=Parser()
  for i in range(100):p.feed(bad)
  self.assertEqual(p.header_errors,100);self.assertEqual(len(p.diagnostics),64)
 def test_local_journal_rotation(self):
  with tempfile.TemporaryDirectory() as d:
   j=Journal(d);j.handler.maxBytes=512
   for i in range(40):j.write('parser_error',seq=i,wire_hex='00'*100)
   j.close();files=list(Path(d).glob('serial_diagnostics.jsonl*'))
   self.assertLessEqual(len(files),3)
   for f in files:
    for line in f.read_text().splitlines():
     row=json.loads(line);self.assertIn('utc',row);self.assertIn('monotonic',row)
