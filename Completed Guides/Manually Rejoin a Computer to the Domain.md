https://support.pacs.com/a/solutions/articles/21003097726
#### General Requirements

- For Wi-Fi only devices:
    - Ensure the computer is connected to either the Support or PGSECURE Wi-Fi network.
- For Ethernet-connected devices:
    - Disable Wi-Fi to ensure the connection is only through Ethernet.
    - Verify the device/port is on the correct VLAN.
- Verify the computer's IPv4 settings are set to Obtain IP Address Automatically (via DHCP) to avoid DNS issues.

---

### Steps to Join the Domain

1. Open System Properties:
    
    - Search for "System Properties" in the Start menu.
2. Access Domain Settings:
    
    - Under the Computer Name tab, click on Change.
3. Join the Domain:
    
    - Select Domain, and enter: provhc.com.
    - Click OK to proceed and then restart.
4. Handling Existing Domain Selection:
    
    - If provhc.com is already selected:
        1. Switch to Workgroup, type in WORKGROUP, and save (but do not restart yet).
        2. Go back, re-select Domain, and type provhc.com again.
5. Resolve Name Conflicts:
    
    - If an error states that the computer name is already in use:
        - Adjust the name slightly by adding or altering a letter or number.
        - Locate the new computer name in Active Directory (AD) and move it to the correct Organizational Unit (OU).

---

### Troubleshooting Common Errors

- Unable to Contact the Domain:
    
    - Ensure the device is connected to Support Wi-Fi or correctly wired.
    - Double-check that the IPv4 settings are configured to obtain the IP address automatically (DHCP).
- Computer Name Already Taken:
    
    - Modify the name as described above.
    - Confirm that the updated name is present in Active Directory (AD) and assigned to the correct OU.

---

### Final Steps

1. Restart the computer to apply domain settings.
2. Test the setup by logging in with a domain account to confirm successful domain joining.