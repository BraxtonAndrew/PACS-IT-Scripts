https://pacstech.itglue.com/7811197/docs/17908166#documentMode=edit&version=published

This guide is used to help with this error message below. This happens when a device has been setup with an EMAR group tag that is not an EMAR computer

![](https://pacstech.itglue.com/7811197/docs/17908166/images/27477063)

### **For Cloud Join Devices**

1. **Change the Group Tag** in Intune.
2. **Push a Sync** from Intune using the RMM tool.
3. **Remote into the Computer** and go to Backstage.
4. Open **Command Prompt** and type `gpedit.msc`, then press Enter.
5. Navigate to:
    - **Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment > Allow log on locally**.
6. **Remove the EMAR account** from the list.
7. Click **Add User or Group**.
    - Click **Object Types** and ensure **Groups** is selected.
    - Add the following groups:
        - "Administrators"
        - "Backup Operators"
        - "Guest"
        - "Users"
    - Type the names, click **Check Names**, and confirm.
8. Exit Backstage and have the user sign in again.

---

### **For Domain Join Devices**

1. Remove the device from this security group (SG): **PG-GPO-Deny-Logon-eMAR-Computers**.
2. Rename the device.
3. Open **Command Prompt** and run:
    - `gpupdate /force` to update group policies.
    - Once complete, run `gpresult /r /scope:computer`.
    - Verify that **Deny Logon for eMAR Computers** is no longer being applied.
4. Go to **Backstage**.
5. Open **Command Prompt as Administrator** and type `gpedit.msc`, then press Enter.
6. Navigate to:
    - **Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment > Allow log on locally**.
7. Ensure the following groups are re-added:
    - "Administrators"
    - "Backup Operators"
    - "Guest"
    - "Users"
    - To add them:
        - Click **Add User or Group**.
        - Click **Object Types** and ensure **Groups** is selected.
        - Type the group names, click **Check Names**, and confirm.
8. Exit Backstage and have the user sign in again.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

### **Common Issues**

- **Sync Issues**  
    After syncing, the device may remove the local login groups.
    - Solution: Add the device to the **Intune - Default Allow Local Logon** group as a member.