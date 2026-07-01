list_type = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
    }
input_string = input('Filename:').strip().lower().split('.')[-1]
#print(list_type[input_string] if input_string in list_type else 'application/octet-stream')
print(list_type.get(input_string, 'application/octet-stream'))
