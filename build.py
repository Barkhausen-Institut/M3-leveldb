import os


def build(gen, env):
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
        '-Wno-psabi',
    ]

    # build all files except tests and other envs
    files = env.glob(gen, 'table/*.cc') + env.glob(gen, 'db/*.cc') + env.glob(gen, 'util/*.cc')
    files = [f for f in files
             if not os.path.basename(f).endswith('_test.cc') and
             os.path.basename(f) != 'env_windows.cc' and
             os.path.basename(f) != 'testutil.cc']

    lib = env.static_lib(gen, out='leveldb', ins=files)
    env.install(gen, env['LIBDIR'], lib)
