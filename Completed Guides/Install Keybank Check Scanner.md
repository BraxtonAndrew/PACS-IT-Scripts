https://support.pacs.com/a/solutions/articles/21005218722

**Important Notes**

- **Only one bank’s scanner software can be installed on a computer at a time**. It is now against company policy (from treasury) to have more than one bank's scanner software installed on a computer. It also causes scanner issues, having multiple bank's scanner software programs on the same computer.

---

**Installation Steps for KeyBank Scanner Software**

1. **Initial Setup in Microsoft Edge**
    
    - Open **Microsoft Edge** and have the user log in to KeyBank.
    - Download the scanner software from the site and run the installer as an administrator.
2. **Post-Installation in Edge**
    
    - After installing the software, return to **Edge** and refresh the page.
    - If the page continues prompting to install the Remote Deposit Scanner software, switch to **Google Chrome**.
3. **Switching to Chrome**
    
    - Sign out of KeyBank in **Edge** and sign in using **Chrome**.
    - Continue with the installation and configuration in Chrome.

---

**Common Errors and Troubleshooting**

- **Fatal Scanner Error**
    
    - **Cause:** This error usually indicates that another driver is installed and interfering with communication.
    - **Fix:**
        1. Open the **Control Panel** and locate the conflicting scanner driver. (Often NDC Deposit Service, or a Panini universal driver)
        2. Uninstall the driver.
        3. Restart the computer.
        4. If issues persist, uninstall all scanner-related software, restart the computer, and start the installation process from scratch.
- **Scanner Not Working After Installation**
    
    - Restart the "Remote Deposit Scanner Service" in **Services.msc**. This is a good first step to resolve communication issues.

---

**Additional Considerations**

- **Why Start with Edge?**
    
    - Starting with Chrome isn't recommended because the "thisisunsafe" workaround no longer bypasses the security prompt effectively.
    - Edge allows you to proceed without requiring confirmation of the browser’s security.
- **Why Switch to Chrome?**
    
    - After installation, **Edge** often struggles to communicate with the scanner and its drivers.
    - Chrome typically works more reliably with the scanner.