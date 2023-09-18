import os



def GetAbsScriptPath():
    AbsScriptPath = os.path.abspath( __file__ )
    AbsFolder_path = os.path.dirname(AbsScriptPath)

    AbsScriptPath_no_extension = AbsScriptPath.rpartition('.')[0]
    if not AbsScriptPath_no_extension:
        AbsScriptPath_no_extension = AbsScriptPath
    return (AbsScriptPath, AbsScriptPath_no_extension, AbsFolder_path)
