import os
def rename_files():
    file_list=os.listdir(r"E:\z.access\prank")
    saved_path=os.getcwd()
    print("Current Working Directory is"+saved_path)
    os.chdir(r"E:\z.access\prank")
    for file_name in file_list:
     res=file_name.translate("0123456789")
     ser=''.join(i for i in res if not i.isdigit())
     os.rename(res,ser)
     print(ser)
    os.chdir(saved_path)
rename_files()

