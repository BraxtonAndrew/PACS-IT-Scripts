### 1. Check VPN Status

#### Using Meraki Dashboard:

1. Open Meraki and navigate to the facility.
2. Go to **Security & SD-WAN** > **VPN Status** (Left Sidebar).
3. Click on **Non-Meraki Peers**.
4. Look for the VPN tunnels:
    - A **green light** should appear next to **NewCloud** and either **Phoenix** or **New York** if the VPN is working properly.

#### Alternative Method: Ping Test

1. Use a device on the network or the firewall to ping the following IP addresses:
    
    **West Coast:**
    
    - `172.17.109.10`
    - `192.168.109.7`
    - _(Optional)_ `192.168.109.4`
    
    **East Coast:**
    
    - `172.18.109.10`
    - `192.168.109.7`
    - _(Optional)_ `192.168.109.4`
2. If you receive a response, the VPN tunnels are up.
    

---

### 2. Restart (Bounce) VPNs

1. In Meraki, go to the facility and navigate to:  
    **Security & SD-WAN** > **Site-to-Site VPN** (Right Sidebar).
2. Locate the **Hub/Spoke Selector** and switch it from **Hub** to **Off**.
3. Save the changes and wait **1-2 minutes**.
4. Switch the setting back to **Hub**, save, and confirm changes.
5. Check the VPN status again.

#### Important Notes:

- It may take **5-10 minutes** for the VPN tunnels to fully restore.