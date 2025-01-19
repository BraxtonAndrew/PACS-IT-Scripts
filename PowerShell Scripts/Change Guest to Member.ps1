# Install Graph module if not already installed
Install-Module -Name Microsoft.Graph -Scope CurrentUser

# Connected to Graph with appropriate permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Open Entra and search for the user
# Click on the user and go to the overview tab
# Copy their UserID (Located next to their UPN/Email Address)

# Prompt user for UserID
$userId = Read-Host "Enter the UserID for the user you want to update"
# Update the user account
Update-MgUser -UserId $userId -UserType "Member"

# Confirm the update
Get-MgUser -UserId $userId | Select-Object UserPrincipalName, UserType

