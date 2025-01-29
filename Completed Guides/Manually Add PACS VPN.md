https://pacs.freshservice.com/a/solutions/articles/21003508628

#### Step 1: Add the VPN Connection

1. Navigate to:  
    **Settings > Network and Internet > VPN**
2. Click Add VPN and fill in the following details:
    - VPN Provider: Windows (built-in)
    - Connection Name: PACS VPN – 2FA
    - Server Address: **vpn2.provhc.com**
    - VPN Type: **L2TP/IPSec with pre-shared key**
    - Pre-Shared Key: **provvpn**
        
        > **Note: DO NOT SHARE THE KEY.**
        
    - Type of Sign-in Info: Username and Password
        - Leave the username and password fields blank.
3. Click Save.

---

#### Step 2: Edit VPN Properties

1. Select the VPN connection you just created and click **Advanced Options**.
2. Next to More VPN Properties, click Edit.
    
    > Note: If "More VPN Properties" does not appear, follow the alternative method below.
    

  

- > #### Alternative Method: Accessing VPN Properties via Control Panel
    > 
    > 1. Open **Control Panel** and go to: **Network and Sharing Center** and click **Change Adapater properties.**
    > 2. Right-click on the VPN connection and select Properties.
    

---

#### Step 3: Configure Security Settings

1. In the Properties window, go to the **Security** tab.
2. Under **Authentication**, select Allow these protocols and check the box for:
    - **Unencrypted password** (PAP).

---

#### Step 4: Adjust Networking Settings

1. In the Properties window, switch to the **Networking** tab.
2. For both **IPv4** and **IPv6**, do the following:
    - Click Properties.
    - Go to Advanced settings.
    - Ensure Use default gateway on remote network is **UNCHECKED**.

---

#### Step 5: Test the VPN

- The VPN setup is now complete.
- Have the user attempt to sign in to verify functionality.