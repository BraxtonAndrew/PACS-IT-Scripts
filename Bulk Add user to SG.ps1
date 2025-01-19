# Import the Azure AD module
if (!(Get-Module -ListAvailable -Name AzureAD)) {
    Install-Module -Name AzureAD -Force
}
Import-Module AzureAD

# Connect to Azure AD
Write-Host "Connecting to Azure AD..." -ForegroundColor Cyan
Connect-AzureAD

# Path to the CSV file
$csvPath = "C:\Users\braxton.andrew\OneDrive - PACS\Documents\VS Code\Assets\upn_list.csv"

# Name of the Security Group
$groupName = "Microsoft 365 F1 Licensing"

# Load the CSV file
try {
    $users = Import-Csv -Path $csvPath
    Write-Host "Successfully loaded CSV file: $csvPath" -ForegroundColor Green
} catch {
    Write-Host "Failed to load CSV file. Ensure the file exists and is formatted correctly." -ForegroundColor Red
    exit
}

# Get the group object
$group = Get-AzureADGroup -Filter "DisplayName eq '$groupName'"

if (!$group) {
    Write-Host "Security group '$groupName' not found in Azure AD. Please check the group name." -ForegroundColor Red
    exit
}

Write-Host "Adding users to group: $groupName" -ForegroundColor Cyan

# List to store successfully added users and users not found
$addedUsers = @()
$usersNotFound = @()

# Iterate through each user in the CSV and add them to the group
foreach ($User in $Users) {
    $UPN = $User.UPN
    if (-not $UPN -or $UPN -eq "") {
        Write-Output "Empty UPN found in row: $($User | Out-String)"
        continue
    }

    # Get the user object
    $aadUser = Get-AzureADUser -Filter "UserPrincipalName eq '$upn'"

    if ($aadUser) {
        try {
            Add-AzureADGroupMember -ObjectId $group.ObjectId -RefObjectId $aadUser.ObjectId
            Write-Host "Successfully added user: $upn" -ForegroundColor Green
            # Add the user to the addedUsers list
            $addedUsers += $upn
        } catch {
            Write-Host "Failed to add user: $upn. Error: $_" -ForegroundColor Red
        }
    } else {
        Write-Host "User not found in Azure AD: $upn" -ForegroundColor Yellow
        # Add the user to the usersNotFound list
        $usersNotFound += $upn
    }
}

# Output the list of added users
if ($addedUsers.Count -gt 0) {
    Write-Host "The following users were successfully added to the group:" -ForegroundColor Cyan
    $addedUsers | ForEach-Object { Write-Host $_ -ForegroundColor Green }
} else {
    Write-Host "No users were added to the group." -ForegroundColor Yellow
}

# Output the list of users not found
if ($usersNotFound.Count -gt 0) {
    Write-Host "The following users were not found in Azure AD:" -ForegroundColor Cyan
    $usersNotFound | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }
} else {
    Write-Host "All users were found and processed." -ForegroundColor Green
}

Write-Host "Script completed." -ForegroundColor Cyan
