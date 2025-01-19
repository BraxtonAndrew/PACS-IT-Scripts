# Example:
# Let’s use the domain company.com and an OU path Users > IT > Support:
# $OU = "OU=Support,OU=IT,OU=Users,DC=company,DC=com"
# !!Note!! you have to specify sub directories to pull them

# Define the OU and domain for the search
$OU = "OU=Users,OU=Autumn Wind AL,OU=PACS Facilities,DC=provhc,DC=com"

# Get all users from the specified OU and sort by Name
$Users = Get-ADUser -Filter * -SearchBase $OU -Properties UserPrincipalName | Sort-Object Name

# Output each user's name and UPN
$Users | Select-Object Name, UserPrincipalName | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        UPN  = $_.UserPrincipalName
    }
} | Format-Table -AutoSize