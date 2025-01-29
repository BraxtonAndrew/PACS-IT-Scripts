https://support.pacs.com/a/solutions/articles/21005044360
1. **Power On the Printer**
    
    - Turn on the Kyocera MA4000 printer and wait for it to fully boot up.
2. **Access the System Menu**
    
    - Press the **Menu** button on the printer panel and navigate to the **System/Network Settings** section.
3. **Enter Administrative Credentials**
    
    - When prompted, enter the username and password:
        - **Username**: `4000`
        - **Password**: `4000`
4. **Enable Wi-Fi**
    
    - Within the **Network Settings**, select the **Network** option.
    - Locate and select **Wi-Fi**, then ensure that Wi-Fi is turned **ON**.
5. **Set Up Wi-Fi**
    
    - Go back one page in the menu and select **Setup**.
    - Choose **Wi-Fi Settings** (typically the 4th option down in the list).
    - Select **Quick Setup**.
6. **Search for Available Networks**
    
    - Allow the printer to scan for available Wi-Fi networks.
    - If no networks appear after 10-15 seconds:
        - Restart the printer.
        - Repeat the steps to navigate back to **Wi-Fi Settings > Quick Setup**.
7. **Connect to Your Network**
    
    - Select your network's **SSID** from the list.
    - Enter the Wi-Fi password (this password can often be found in **Meraki**).
8. **Verify Connection**
    
    - Once connected, the printer will display a confirmation.
    - Return to the **Network Settings** menu by going back two pages.
9. **Check TCP/IP Settings**
    
    - Navigate to **TCP/IP Settings** (typically the 4th option in the list).
    - Select **IPv4**.
10. **Note the IP Address**
    
    - Choose **IP Address** and write down the displayed IP address.
    - This will be needed for setting up the printer in management software like **PrinterLogic**.
11. **Finalize Setup**
    
    - Use the recorded IP address to add the printer to **PrinterLogic**

  

  

**Additional Notes**

- The Web UI Password is usually the serial number which can be found on the Web UI by going to the Device Info > Configuration tab.
- The username is always **Admin**.