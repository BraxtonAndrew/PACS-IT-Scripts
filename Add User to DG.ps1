# Import Exchange Online Management
Import-Module ExchangeOnlineManagement

# Connect to Exchange Online
Connect-ExchangeOnline

# Specify the CSV file path (replace with your actual path)
$csvFilePath = "C:\Users\braxton.andrew\OneDrive - PACS\Documents\VS Code\Assets\Add User to DG.csv"

# Specify DG Name
$distributionGroup = "administrators.bluegrass@pacs.com"

# Import Users from CSV file (assuming the header is "UPN")
$users = Import-Csv -path $csvFilePath -Header "UPN"

# Loop through each user in the CSV file
foreach ($user in $users) {
    $userPrincipalName = $user.UPN
  
    # Add user with error handling because $user.UPN is flagged even tho it works fine. It's just annoying to see errors that aren't important.
    Add-DistributionGroupMember -Identity $distributionGroup -Member $userPrincipalName -ErrorAction SilentlyContinue
  
    # Display confirmation message only if successful
    if (!$?) {
      Write-Warning "Failed to add user $userPrincipalName to $distributionGroup."
    } else {
      Write-Host "Added user $userPrincipalName to $distributionGroup."
    }
}