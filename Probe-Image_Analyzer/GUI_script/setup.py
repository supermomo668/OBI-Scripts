
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

application_title = "RNA&Image_Analyzer" #what you want to application to be called
main_python_file = "RNAProbe_BatchAnalyzer.py" #the name of the python file you use to run the program

import cx_Freeze
import sys
import os
import scipy
scipy_path = os.path.dirname(scipy.__file__)

#from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("RNAProbe_BatchAnalyzer_fromui.py", base=base, icon="OB_icon.ico")]

os.environ['TCL_LIBRARY'] = r'C:\ProgramData\Anaconda3\pkgs\tk-8.6.8-hfa6e2cd_0\Library\lib\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\ProgramData\Anaconda3\pkgs\tk-8.6.8-hfa6e2cd_0\Library\lib\tk8.6'

cx_Freeze.setup(
        name=application_title,
        version="0.1",
        description="cx_Freeze PyQt5 script",
        options={"build_exe": {"packages": ["PyQt5", "matplotlib", "numpy", "PIL",
                                            "skimage", "pandas", "seaborn", "time",
                                            "datetime", "mahotas", "subprocess"],
                               "includes": [scipy_path, "scipy.sparse.csgraph._validation"
                                            ]}},
        author='Matt Mo',
        executables=executables)