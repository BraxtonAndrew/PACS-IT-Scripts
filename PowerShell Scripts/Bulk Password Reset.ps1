# Set execution policy for the session
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

# Install and import the ActiveDirectory module if not already installed
if (-not (Get-Module -ListAvailable -Name ActiveDirectory)) {
    Install-Module -Name ActiveDirectory -Force -AllowClobber
}
Import-Module -Name ActiveDirectory

# Path to the CSV file with UPNs
$csvFilePath = "C:\Users\braxton.andrew\OneDrive - PACS\Documents\VS Code\Assets\Bulk Password Reset.csv"

# Import UPNs from CSV file
$users_to_Reset = Import-Csv -Path $csvFilePath

# Loop through each UPN and reset the password
foreach ($user in $users_to_Reset) {
    # Ensure the property is accessed correctly
    $upn = $user.'UPN'

    # Get the user object from Active Directory using the UPN
    $userObject = Get-ADUser -Filter { UserPrincipalName -eq $upn } -Properties UserPrincipalName

    if ($userObject) {
        # Get a simple password from the DinoPass API
        $dinopassAPI = "https://www.dinopass.com/password/simple"
        $dinoPassword = Invoke-RestMethod -Uri $dinopassAPI -Method Get

        # Capitalize the first character of the password
        $Endpassword = $dinoPassword.Substring(0,1).ToUpper() + $dinoPassword.Substring(1)

        # Set the new password for the user account
        Set-ADAccountPassword -Identity $userObject -NewPassword (ConvertTo-SecureString -AsPlainText $Endpassword -Force) -Reset

        # Optionally, you can also force the user to change the password at next logon
        Set-ADUser -Identity $userObject -PasswordNeverExpires $true -ChangePasswordAtLogon $false

        # Output the reset information to the console
        Write-Host "Reset password for $($userObject.UserPrincipalName) to: $Endpassword"
    } else {
        Write-Host "User with UPN $($upn) not found in Active Directory."
    }
}
