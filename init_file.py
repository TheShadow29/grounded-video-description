import os
import sys
# hack to allow the imports of evaluation repos
_SCRIPTPATH_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_SCRIPTPATH_, 'tools/densevid_eval'))
sys.path.insert(0, os.path.join(
    _SCRIPTPATH_, 'tools/densevid_eval/coco-caption'))
sys.path.insert(0, os.path.join(_SCRIPTPATH_, 'tools/anet_entities/scripts'))
