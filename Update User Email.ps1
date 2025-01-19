# Ensure the Active Directory module is imported
Import-Module ActiveDirectory

# Prompt for the current UPN and new UPN
$currentUPN = (Read-Host -Prompt "Enter the current UPN of the user").Trim()
$newUPN = (Read-Host -Prompt "Enter the new UPN for the user").Trim()

# Derive the new primary proxy address from the new UPN
$newPrimaryProxy = "SMTP:" + $newUPN

# Try to find the user object using the current UPN
try {
    $user = Get-ADUser -Filter {UserPrincipalName -eq $currentUPN} -Property ProxyAddresses, EmailAddress

    # Check if the user was found
    if ($user) {
        # Update the UPN
        Set-ADUser -Identity $user -UserPrincipalName $newUPN
        Write-Output "UPN updated to $newUPN"

        # Update the display email address to match the new UPN
        Set-ADUser -Identity $user -EmailAddress $newUPN
        Write-Output "Display email address updated to $newUPN"

        # Retrieve existing proxy addresses
        $proxyAddresses = $user.ProxyAddresses

        # Ensure proxyAddresses is an array of strings
        if ($proxyAddresses -isnot [array]) {
            $proxyAddresses = @($proxyAddresses)
        }

        # Initialize a new array for updated proxy addresses
        $updatedProxyAddresses = @()

        # Iterate through each proxy address
        foreach ($address in $proxyAddresses) {
            if ($address -ieq $newPrimaryProxy) {
                # If the address matches the new primary proxy, keep it unchanged
                $updatedProxyAddresses += $address
            } else {
                # Ask whether to keep or remove the secondary address
                $choice = (Read-Host -Prompt "Do you want to keep the secondary address '$address'? (yes/no)").Trim()
                if ($choice -ieq "yes") {
                    # Convert to lowercase and keep the address
                    $updatedProxyAddresses += $address.ToLower()
                }
            }
        }

        # Add the new primary proxy address if it's not already present
        if (-not $updatedProxyAddresses.Contains($newPrimaryProxy)) {
            $updatedProxyAddresses += $newPrimaryProxy
        }

        # Update the user's proxy addresses
        Set-ADUser -Identity $user -Replace @{ProxyAddresses = $updatedProxyAddresses}
        Write-Output "Proxy addresses updated"
    } else {
        Write-Output "User with UPN $currentUPN not found"
    }
}
catch {
    Write-Output "An error occurred: $_"
}

# Clean up variables
Clear-Variable -Name currentUPN, newUPN, proxyAddresses, newPrimaryProxy, updatedProxyAddresses, user
$currentUPN = $null
$newUPN = $null
#$proxyAddresses = $null
$newPrimaryProxy = $null
#$updatedProxyAddresses = $null
$user = $null



