from pathlib import Path
import sys
import shutil

types = {
    "Executables" : [".exe", ".bat", ".msi"],
    "Notes" : [".txt", ".md"],
    "Docs" : [".docx", ".pdf", ".doc"],
    "Music" : [".mp3", ".wav"],
    "Video" : [".webm", ".mp4"],
    "Pictures" : [".png", ".jpg", ".jpeg"],
    "Python" : [".py"], 
    "CPP" : [".cpp", ".h", ".hpp"],
    "Archives" : [".7z", ".zip", ".rar"],
    "Android" : [".apk"],
    "Torrent" : [".torrent"],
    "Java" : [".jar"],
    "Excel" : [".xlsx", ".xls"],
    "JSON_XML" : [".json", ".xml"]
}

def create_folder(folder_path : Path) -> Path:
    if folder_path.is_dir():
        #print("folder exists")
        return folder_path
    else:
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
        except FileNotFoundError:
            print("Could not find a directory.")
            return Path()
        print(f"created a folder {folder_path}")
        return folder_path

def move_files(folder_path : Path) -> bool:
    file_folder = None
    
    for f in folder_path.iterdir():
        if f.is_file(follow_symlinks=False):
            try:
                for sortType, extentions in types.items():
                    #print(sortType, extentions)
                    for extention in extentions:
                        if extention == f.suffix:
                            
                            if sortType == "CPP":
                                if f.name != "main.cpp" and extention != ".cpp":
                                    file_folder = folder_path / sortType / "includes"
                                elif f.name != "main.cpp":
                                    file_folder = folder_path / sortType / "src"
                                else:
                                    file_folder = folder_path / sortType
                            else:
                                file_folder = folder_path / sortType
                                
                            #print(f"Found a file type! {extention}")
                            break
                        
                if file_folder is None:
                    #print(f"Found no similar extention for file {f}")
                    file_folder = folder_path / "Other"
                    
                shutil.move(str(f), create_folder(file_folder))
                
            except Exception as e:
                print(f"Something went wrong. {e}")
                return False
    return True
            

if __name__ == "__main__":
    
    try:
        folder = Path(sys.argv[1])
        if folder.is_dir():
            move_files(folder)
        else:
            print("Could not find a folder.")
        sorted(folder.iterdir())
    except IndexError:
        print("No path was passed.")
        
            