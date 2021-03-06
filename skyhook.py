import skyhookPreCheck, os, sys, skyhookDb, skyhookUpDown

usage = """
    skyhook clear history   -   Delete everything from history
    skyhook list history    -   List all entries in history
    
    skyhook search [file name/hash]  -   Search history for entries matching [file name/hash]
    skyhook delete [file name/hash]  -   Delete entries specified by [file name/hash] from history
    skyhook save [file name/hash]    -   Save history entries specified by [file name/hash] to the current directory to export.pod
    skyhook add [name:hash:key]      -   Manually add an entry to history specified by colon-separated values of [name:hash:key]
    
    skyhook import [path]   -   Import history from a location specified by [path]
    skyhook export history  -   Export entire history to the current directory to export.pod
    
    skyhook upload [file name]  -   Upload a file specified by [file name] from the current directory to the IPFS network
    skyhook download [hash]     -   Download a file specified by [hash] from the IPFS network to the current directory

    It is possible to specify multiple values in a form of a comma-separated list for search,delete,save,import,upload,download and add functions.
"""

def main(command, target):
    if command == "list" and target == "history":
        res = skyhookDb.listDb()
        if res == 1:
            print("[!] History is empty")
            
    elif command == "clear" and target == "history":
        skyhookDb.clearDb()
        
    elif command == "search":
        res = skyhookDb.searchDb(target)
        if res == 1:
            print("[!] Could not find {} in history".format(target))
            
    elif command == "add":
        for tar in target.split(','):
            name, hash, key = tar.split(':')
            res = skyhookDb.addEntry(name, hash, key)
            if res == 1:
                print("[!] Error adding entry to history")
            elif res == 2:
                print("[!] Invalid hash")
            elif res == 3:
                print("[!] Unacceptable key length")
            else:
                print("[+] Successfully added {} to history".format(name))
                
    elif command == "export" and target == "history":
        res = skyhookDb.exportDb(target)
        if res == 1:
            print("[!] Error exporting history")
        else:
            print("[+] Successfully exported history to export.pod")
            
    elif command == "save":
        for tar in target.split(','):
            res = skyhookDb.saveOne(tar)
            if res == 1:
                print("[!] Could not find {} in history".format(tar))
            elif res == 2:
                print("[!] Error saving {} to export.pod".format(tar))
            else:
                print("[+] Successfully saved {} to export.pod".format(tar))
                
    elif command == "import":
        for tar in target.split(','):
            res = skyhookDb.importDb(tar)
            if res == 1:
                print("[!] Could not read {}".format(tar))
            elif res == 2:
                print("[!] Could not import {}".format(tar))
            elif res == 3:
                print("[!] No entries in {}".format(tar))
            else:
                print("[+] Successfully imported {}".format(tar))
                
    elif command == "delete":
        for tar in target.split(','):
            res = skyhookDb.deleteItem(tar)
            if res == 1:
                print("[!] Could not find {} in history".format(tar))
            elif res == 2:
                print("[!] Could not delete {} from history".format(tar))
            else:
                print("[+] Successfully deleted {} from history".format(tar))
                
    elif command == "upload":
        for tar in target.split(','):
            res = skyhookUpDown.uploadFile(tar)
            if res == 1:
                print("[!] Could not find {} in the local directory".format(tar))
            elif res == 2:
                print("[!] Could not encrypt {}".format(tar))
            elif res == 3:
                print("[!] Could not upload {}".format(tar))
            elif res == 4:
                print("[!] Could not add an entry for {}".format(tar))
            else:
                print("[+] Successfully uploaded {}".format(tar))
                
    elif command == "download":
        for tar in target.split(','):
            res = skyhookUpDown.downloadFile(tar)
            if res == 1:
                print("[!] Could not retrieve {} from history".format(tar))
            elif res == 2:
                print("[!] Could not download {}".format(tar))
            elif res == 3:
                print("[!] Could not decrypt {}".format(tar))
            else:
                print("[+] Successfully downloaded {}".format(res))
                
    else:
        print(usage)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print(usage)
        exit()
        
    command = str(sys.argv[1])
    target = str(sys.argv[2])
    
    main(command, target)
