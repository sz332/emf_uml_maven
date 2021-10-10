import os
import zipfile

def clear_folder(dir):
    if os.path.exists(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                else:
                    clear_folder(file_path)
                    os.rmdir(file_path)
            except Exception as e:
                print(e)

def install_maven(zip_name,root_folder):
    with zipfile.ZipFile(zip_name,'r') as zip_ref:
        zip_ref.extractall(root_folder)

    mvn_command = "mvn install:install-file -Dfile={} -DgroupId={} -DartifactId={} -Dversion={} -Dpackaging={}"    
    mvn_command_sources = "mvn install:install-file -Dfile={} -Dsources={} -DgroupId={} -DartifactId={} -Dversion={} -Dpackaging={}"    

    for file in os.listdir(root_folder + "/plugins"):
        if (file.endswith(".jar")):
            splitted = file.split("_")
       
            if (splitted[0].endswith("source")):
                continue

            filepath = "./{}/plugins/{}".format(root_folder, file)
            group_id = "com.acme.eclipse"
            artifact_id = splitted[0]
            version = splitted[1][:-4]
            packaging = "jar"

            source_file = "./{}/plugins/{}.source_{}.jar".format(root_folder,splitted[0],version)

            if os.path.exists(source_file):
                os.system(mvn_command_sources.format(filepath,source_file,group_id, artifact_id, version, packaging))
            else:
                os.system(mvn_command.format(filepath, group_id, artifact_id, version, packaging))

    clear_folder(root_folder)   

try:
    os.mkdir("extract")
except OSError as error:
    print(error)    

install_maven("EMF-Updates-2.27.zip", "extract")
install_maven("mdt-uml2-Update-5.5.2.zip", "extract")

os.rmdir("extract")

