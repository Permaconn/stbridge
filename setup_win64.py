from distutils.core import setup
from distutils.extension import Extension

ext = Extension(
    'stbridge',
    sources=['stbridge.cpp', 'libs/src/bridge/bridge.cpp', 'libs/src/common/criticalsectionlock.cpp',
    	'libs/src/common/stlink_device.cpp', 'libs/src/common/stlink_interface.cpp', 'libs/src/error/ErrLog.cpp'],
    library_dirs=['C:/local/boost_1_80_0/lib64-msvc-14.3'],
    #libraries=['boost_python310-vc143-mt-x64-1_80'],	# This is automatically determined by boost (assuming a pragma comment lib)

    extra_compile_args=['/std:c++20', '-DWIN32', '-Ilibs/src/bridge', '-Ilibs/src/common', '-Ilibs/src/error', '-I../libraries/libusb-1.0.26/', '-IC:/local/boost_1_80_0'],
)

setup(
    name='stbridge',
    version='0.1',
    ext_modules=[ext])
