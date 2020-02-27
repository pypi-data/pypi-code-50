version_info = (2, 3, 0, 'final', 0)

_specifier_ = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc', 'final': ''}

spec = '' if version_info[3]=='final' else _specifier_[version_info[3]]+str(version_info[4])
__version__ = f'{version_info[0]}.{version_info[1]}.{version_info[2]}{spec}'
# __version__ = '%s.%s.%s%s'%(version_info[0], version_info[1], version_info[2],
  # '' if version_info[3]=='final' else _specifier_[version_info[3]]+str(version_info[4]))
