https://support.pacs.com/a/solutions/articles/21003048587

### **Primary Solution (Clear App Cache Using Windows Run Dialog):**

1. **Open the Windows Run Dialog:**
    
    - Press **Windows key + R** to open the **Run** dialog box.
2. **Clear the App Cache:**
    
    - In the Run dialog, type the following command and press **Enter**: `rundll32 dfshim CleanOnlineAppCache   `
    - This will clear the app cache for NetHealth.

> **Note:** If the problem persists, proceed to the next step (Delete the Folder).

---

### **Secondary Solution (Delete the Folder):**

1. **Remote into the User’s Computer:**
    
    - Sign the user out of their account and sign into an **admin account**.
2. **Navigate to the Folder:**
    
    - Go to `C:\Users\{user account}\AppData\Local\Apps\`
3. **Delete the 2.0 Folder:**
    
    - Remove the entire **2.0** folder.
4. **Restart the Computer:**
    
    - After deleting the folder, restart the computer.
    - Have the user log back into **NetHealth**.

> **Note:** If the problem persists, proceed to the next step (Nuking the Account).

---

### **Last Resort: Steps to Nuke the Account**

If clearing the cache and deleting the folder do not resolve the issue, proceed with nuking the account.

#### **Before Proceeding:**

1. **Check for Important Data:**
    
    - Ensure there is no important data stored locally on the account. If any exists, save it to **OneDrive** or **SharePoint** to prevent data loss.
2. **Export Browser Bookmarks:**
    
    - Export the bookmarks from the browser and store them in **OneDrive**.

---

#### **Steps to Nuke the Account:**

1. **Sign Out and Restart:**
    
    - Sign out of the user account.
    - Restart the computer.
2. **Log into the Local Admin Account:**
    
    - Once the computer has restarted, log in using the **Local Admin Account**.
3. **Open Advanced System Settings:**
    
    - Press the **Windows key**, type **“View Advanced System Settings”** into the search bar, and select it.
4. **Access User Profiles Settings:**
    
    - In the **System Properties** window, click on **Settings** under the **User Profiles** section.
5. **Delete the User Account:**
    
    - From the list of profiles, select the user account (usually the facility’s generic therapy account) and click **Delete**.
6. **Re-log into the User Account:**
    
    - Log back into the user account after the deletion process is complete.
7. **Open NetHealth:**
    
    - Open **Microsoft Edge** and navigate to **NetHealth**.
    - Enter the **facility code** (typically **PLMHG**) and click **Run** to open NetHealth.

---

### **Troubleshooting:**

If **NetHealth** still doesn’t load correctly after following the steps above:

1. Try opening it in an **Incognito** window in **Microsoft Edge**.
2. If the issue persists, recheck the settings or escalate for further assistance.

---

### **Other Information:**

- **NetHealth Login URL:**  
    [https://login.therapy.nethealth.com/](https://login.therapy.nethealth.com/)
    
- **Login Code:**  
    **PLMHG**