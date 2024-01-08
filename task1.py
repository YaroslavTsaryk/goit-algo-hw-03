import os
import sys
import shutil

dest_folders={}

def process_folder(folder_name,dest_folder):
    for obj in os.scandir(folder_name):
        if obj.is_dir():
            process_folder(folder_name+"/"+obj.name,dest_folder)
        if obj.is_file():
            file_ext=obj.name.split(".")[-1]
            if file_ext not in dest_folders.keys():
                os.makedirs(dest_folder+"/"+file_ext,exist_ok = True)    
                dest_folders[file_ext]=dest_folder+"/"+file_ext
            try:
                shutil.copyfile(folder_name+"/"+obj.name,dest_folders[file_ext]+"/"+obj.name)
            except OSError as e:
                print("Unable to copy file. %s" % e)
        

    

def main(argv, argc):
    args = argv[1:]
    source=""
    dest=""
    if argc==1 or argc>3:
        print(f"execute program.py source_path <dest_path>")   
        exit()
    if argc>1:
        source=args[0]        
    else:
        source="e:/tmp/goit-algo-hw-03/source"
    if argc>2:
        dest=args[1]        
    else:    
        dest="/".join((source.split("/")[0:-1]))+"/dist"      
    
    print(f"{source = }")
    print(f"{dest = }")
    process_folder(source,dest)
    print("Task completed")
    
    
if __name__ == '__main__':
    main(sys.argv, len(sys.argv))