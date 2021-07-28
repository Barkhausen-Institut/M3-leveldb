import os

Import('env')

myenv = env.Clone()

myenv.Append(CPPPATH = ['.', 'include'])

myenv['CXXFLAGS'] = [
    # use the same flags as for M³
    '-std=c++14',
    '-fno-strict-aliasing',
    '-fno-omit-frame-pointer',
    '-fno-threadsafe-statics',
    '-fno-stack-protector',
    '-O2',
    '-DNDEBUG',
    '-flto',
    '-U_FORTIFY_SOURCE',
    '-D_GNU_SOURCE',

    # use POSIX platform
    '-DLEVELDB_PLATFORM_POSIX',

    # silence warnings
    '-Wno-sign-conversion',
    '-Wno-unused-parameter',
    '-Wno-implicit-fallthrough',
    '-Wno-unused-function',
]
if myenv['ARCH'] == 'riscv64':
    myenv['CXXFLAGS'] += [
       '-march=rv64imafdc',
       '-mabi=lp64',
    ]

# build all files except tests and other envs
files = myenv.Glob('table/*.cc') + myenv.Glob('db/*.cc') + myenv.Glob('util/*.cc')
files = [f for f in files
         if not os.path.basename(str(f)).endswith('_test.cc') and
            os.path.basename(str(f)) != 'env_windows.cc' and
            os.path.basename(str(f)) != 'testutil.cc']

myenv.LxLibrary(myenv, target = 'leveldb', source = files)
