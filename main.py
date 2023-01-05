import os
import subprocess
import shutil
import json

VERSION = "1.19.3"
ZIP = "C:/Program Files/7-Zip/7z.exe"
MINECRAFT_LOC = os.getenv("APPDATA").replace("\\", "/") + "/.minecraft"
MINECRAFT_JAR = "%s/versions/%s/%s.jar" % (MINECRAFT_LOC, VERSION, VERSION)
CWD = os.getcwd().replace("\\", "/")
ASSETS_TARGET = CWD + "/vanilla"

if not os.path.exists(ASSETS_TARGET):
    print("Vanilla assets are not extracted, extracting now..")
    
    # os.system and subprocess.run make me Genuinely angry
    # The auto escape stuff is fucking terrible and means I cannot execute the correct command
    # I am literally writing and executing a batch file as a workaround
    
    cmd = "\"" + ZIP + "\" x \"" + MINECRAFT_JAR + "\" -r -o\"" + ASSETS_TARGET + "\" data/*.*"
    file = open("extract.bat", "w+")
    file.write(cmd)
    file.close()
    os.system("extract.bat")

# api for feature scripts to use
class Pack(object):
    
    def __init__(self):
        self.path = CWD + "/output/"
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
        
    def write_json(self, data, target):
        target = self.path + target
        dir = os.path.dirname(target)
        if not os.path.exists(dir):
            os.makedirs(dir)
        file = open(target, "w+")
        file.write(json.dumps(data))
        file.close()
        
    def write_feature_file(self, relative_path, target):
        target = self.path + target
        dir = os.path.dirname(target)
        if not os.path.exists(dir):
            os.makedirs(dir)
        shutil.copy(CWD + "/features/" + self.feature_folder + relative_path, target)
        
    def write_file(self, raw_path, target):
        target = self.path + target
        dir = os.path.dirname(target)
        if not os.path.exists(dir):
            os.makedirs(dir)
        shutil.copy(raw_path, target)
        
    def get_json(self, target):
        if os.path.exists(self.path + target):
              target = self.path + target
              print("using already modified data:", target)
        else: target = CWD + "/vanilla/" + target
        file = open(target)
        data = file.read()
        file.close()
        return json.loads(data)
        
    def scan_files(self, target):
        return [ f.path for f in os.scandir(CWD + "/vanilla/" + target) if not f.is_dir() and f.path.endswith(".json") ]
        
    def scan_feature_files(self):
        return [ f.path for f in os.scandir(CWD + "/features/" + self.feature_folder) if not f.is_dir() and f.path.endswith(".json") ]
        
pack = Pack()
print(".. compiling datapack")
        
# dynamically import and run all feature scripts
for feature_folder in [ f.path for f in os.scandir(CWD + "/features/") if f.is_dir() ]:
    for file in [ f.path for f in os.scandir(feature_folder) if not f.is_dir() and f.path.endswith(".py") ]:
        feature = os.path.basename(feature_folder)
        script = os.path.basename(file)
        print(">> " + feature)
        exec("from features.%s.%s import main" % (feature, script.replace(".py", "")))
        pack.feature_folder = feature  + "/"
        main(pack)
        
print("!! complete!")
