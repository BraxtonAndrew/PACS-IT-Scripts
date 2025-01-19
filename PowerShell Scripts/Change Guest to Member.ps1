# Install Graph module if not already installed
Install-Module -Name Microsoft.Graph -Scope CurrentUser

# Connected to Graph with appropriate permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Open Entra and search for the user
# Click on the user and go to the overview tab
# Copy their UserID (Located next to their UPN/Email Address)

# Update the user account
Update-MgUser -UserType "Member"
# Paste in the UserID in the terminal when it asks for it
