https://support.pacs.com/a/solutions/articles/21003421319

### **Important:**  
Ensure you obtain a newly generated install file from EHR. Install files are one-time use and must be brand new for each reinstall.

---

### Steps for Reinstalling the eMAR Backup Agent:

1. Log into the eMAR Account:
    
    1. Or any account with admin privliges such as the local admin or your admin account.
        
2. Uninstall the Current eMAR Backup Agent:
    
    - Navigate to C:\Program Files\EmarBackupAgent\ and run the uninstaller as Administrator.
    - After uninstallation, delete the entire EmarBackupAgent folder.
3. Reboot and Re-login:
    
    - Restart the computer and log back in with the eMAR account.
4. Prepare for New Install:
    
    - Go to C:\Temp and drop the newly zipped install file there.
        - If C:\Temp doesn't exist feel free to create it or use any other directory
    - Unzip the install file, then open Command Prompt (CMD) as Administrator.
5. Install the eMAR Backup Agent:
    
    - In CMD, navigate to the installer’s file path:
        - Copy the installer's path and type cd {paste file path} in CMD (e.g., cd:\Temp\pghc_251_agent_windows_x64) and hit Enter.
    - Run the installer by typing AgentInstall.bat and hitting Enter.
6. UAC Prompt:
    
    - If a UAC prompt appears, click Yes to allow the installer to run.
7. Check the Logs:
    
    - After installation, navigate to C:\Program Files\EmarBackupAgent\agentdata\logs and open the agent.txt file.
    - Look for the message “Connection established with GoAnywhere Server!” to confirm the installation was successful.
    - Also, check to confirm that the "Go Anywhere" service is running under services.msc.

---

### Troubleshooting Common Errors:

- "Not Allowed to Register at This Time" Error:
    
    - This error occurs if the install file is not newly generated. Obtain a brand new install file from EHR and repeat the installation process.
- AMP (Advanced Malware Protection) Interference:
    
    - Cisco Meraki's A.M.P. may prevent the eMAR Backup from connecting to the server.
        - Temporarily disable A.M.P. and run the installer.
        - After installation, re-enable A.M.P..
- Restarting the "Go Anywhere" Service may help resolve issues with it not backing up. Please make sure to check the logs to know the error as well.
- If all else fails, get a new installer.