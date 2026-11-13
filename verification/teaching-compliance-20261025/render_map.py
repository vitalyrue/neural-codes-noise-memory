from pathlib import Path
import importlib.util,sys,json,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sys.path.insert(0,str(ROOT/'verification/illustrations'))
import figure_style
figure_style.OUT=OUT/'map-candidate'
source=OUT/'proposed/verification/illustrations/draw_orientation.py'
spec=importlib.util.spec_from_file_location('corrected_map',source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
result=module.draw();assert result['status']=='pass',result
candidate=OUT/'map-candidate/V01';destination=OUT/'proposed/assets/approved/visuals';destination.mkdir(parents=True,exist_ok=True)
for extension in ['svg','png']:(destination/f'foundations-paper-map.{extension}').write_bytes((candidate/f'figure.{extension}').read_bytes())
from PIL import Image,ImageChops
old=Image.open(ROOT/'assets/approved/visuals/foundations-paper-map.png').convert('RGB');new=Image.open(candidate/'figure.png').convert('RGB')
assert old.size==new.size,(old.size,new.size)
diff=ImageChops.difference(old,new);bbox=diff.getbbox()
# All three changed labels lie to the right of the plotted scientific content.
left_changed=diff.crop((0,0,1200,old.height)).getbbox()
report={'png_size':list(new.size),'changed_pixel_bounds':bbox,'scientific_drawing_left_of_x1200_unchanged':left_changed is None,'qa':result}
(OUT/'map-repair-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
assert left_changed is None,report
print(json.dumps({'qa_status':result['status'],'size':list(new.size),'changed_pixel_bounds':bbox,'scientific_drawing_unchanged':left_changed is None}))
