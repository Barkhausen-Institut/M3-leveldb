import os

def build(gen, env):
    if env['PLATF'] == 'host':
        return

    env = env.clone()

    env['CPPPATH'] += ['src/libs/leveldb', 'src/libs/leveldb/include']
    # needed for strdup
    env['CPPFLAGS'] += ['-D_GNU_SOURCE']

    # shut off warnings
    env['CXXFLAGS'] += [
        '-Wno-sign-conversion',
        '-Wno-unused-parameter',
        '-Wno-implicit-fallthrough',
        '-Wno-unused-function',
    ]

    # build all files except tests and other envs
    files = env.glob('table/*.cc') + env.glob('db/*.cc') + env.glob('util/*.cc')
    files = [f for f in files
             if not os.path.basename(f).endswith('_test.cc') and
                os.path.basename(f) != 'env_windows.cc' and
                os.path.basename(f) != 'testutil.cc']

    lib = env.static_lib(gen, out = 'libleveldb', ins = files)
    env.install(gen, env['LIBDIR'], lib)
