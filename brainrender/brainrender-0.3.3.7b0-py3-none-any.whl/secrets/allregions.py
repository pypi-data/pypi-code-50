import sys
sys.path.append('./')

import random
from tqdm import tqdm

import brainrender
brainrender.SHADER_STYLE = 'cartoon'

from brainrender.scene import Scene



regions = Scene().region_acronyms

for region in tqdm(regions):
    fld = f'/Users/federicoclaudi/Dropbox (UCL - SWC)/Rotation_vte/Anatomy/allregions'

    scene = Scene(screenshot_kwargs={'folder':fld, 'name':region.replace('/', '_')+'_coronal'})

    scene.add_brain_regions([region], use_original_color=True)


    scene.screenshots_name = region.replace('/', '_')+'_top'
    scene.render(interactive=False, camera='top')
    scene.take_screenshot()

    scene.screenshots_name = region.replace('/', '_')+'_coronal'
    scene.render(interactive=False, camera='coronal')
    scene.take_screenshot()

    scene.screenshots_name = region.replace('/', '_')+'_sagittal'
    scene.render(interactive=False, camera='sagittal')
    scene.take_screenshot()

    scene.screenshots_name = region.replace('/', '_')+'_angled'
    scene.render(interactive=False, camera='three_quarters')
    scene.take_screenshot()

 

a = 1