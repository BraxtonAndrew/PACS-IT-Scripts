https://pacs.freshservice.com/a/solutions/articles/21003429154

#### mportant Notes

- Only one bank’s scanner software can be installed on a computer at a time.
    - Example: You **cannot** have both KeyBank and RFMS software on the same computer. Doing so will cause scanner errors.

---

### For Digital Check CX30:

1. Download the Software:
    
    - Copy and paste this address into your browser:  
        https://www.rfmsonline.com/downloads/RDCDrivers/Digitalv2.zip
    - Download and extract the ZIP file.
2. Install the Files (In This Order):
    
    - NDC Deposit Service:
        - Run the setup.exe file only.
    - TellerScanDriver
    - ScanLite
3. Test the Installation:
    
    - Have the user open RFMS and scan a check to confirm functionality.

---

### For Panini Vision X:

1. Temporarily Add the User to Administrators:
    
    - Open Command Prompt (CMD) as an administrator.
    - Enter the following command (replace {firstname.lastname} with the user’s username): net localgroup administrators provhc\{firstname.lastname} /add && shutdown -l  
        Note: Warn the user that this will log them out, and they should save their work before proceeding.
2. Download the Software:
    
    - After the user logs back in, copy and paste this address into your browser:  
        https://www.rfmsonline.com/downloads/RDCDrivers/paniniunisoft.zip
    - Download and extract the ZIP file.
3. Install the Files (In This Order):
    
    - NDC Deposit Service
    - Panini Universal Driver: Run this as an administrator.
4. Test the Installation:
    
    - Have the user open RFMS and scan a check to confirm functionality.
5. Remove the User from Administrators:
    
    - Open Command Prompt (CMD) again.
    - Enter the following command (replace {firstname.lastname} with the user’s username): net localgroup administrators provhc\{firstname.lastname} /delete && shutdown -l  
        Note: This will log the user out again.

---

#### Alternative Method for Panini Installation

- Extract the ZIP file contents.
- Run the setup.exe files for each component as an administrator.
- This method is faster and easier but has not been fully tested.

---

### Final Steps for Both Scanners:

- After installation, verify that RFMS can successfully scan a check.
- If issues persist, ensure no conflicting scanner software is installed on the computer.