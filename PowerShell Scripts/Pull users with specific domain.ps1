# Import the Active Directory module (if not already imported)
Import-Module ActiveDirectory

# Define the domain to filter by
$domain = "@pineridgepa.com"

# Retrieve all users from AD and filter by the specified domain
$users = Get-ADUser -Filter * -Properties UserPrincipalName

# Check each user's UPN and print it if it matches the domain
$matchedUsers = $users | Where-Object { $_.UserPrincipalName -like "*$domain" }

if ($matchedUsers) {
    $matchedUsers | Sort-Object Name | Select-Object Name, UserPrincipalName | Format-Table -AutoSize
} else {
    Write-Output "No users found with UPN ending in '$domain'"
}
