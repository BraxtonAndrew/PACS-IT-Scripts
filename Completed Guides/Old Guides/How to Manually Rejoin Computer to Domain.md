Manually join a domain:

Windows 11:

1. Make sure the computer is on the Providence or Support wifi
	1. If the computer is using ethernet and wifi, have the user unplug the ethernet cable so it is only using the wifi.
2. Search for system
3. ![A screenshot of a computerDescription automatically generated](https://attachment.freshservice.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEwMzQ0Njk5NTksImRvbWFpbiI6InBhY3MuZnJlc2hzZXJ2aWNlLmNvbSIsInR5cGUiOjF9.FHcAyhFQRUjL8Mrbam7vndeQyYio_vwPzW0v-OfEnFA)
4. Click on ‘Domain or workgroup’
5. ![A screenshot of a computerDescription automatically generated](https://attachment.freshservice.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEwMzQ0Njk5NTcsImRvbWFpbiI6InBhY3MuZnJlc2hzZXJ2aWNlLmNvbSIsInR5cGUiOjF9.iiJ-9-pxKs0qpt9Mescx8UcNVRs_5KBqUM6K6Wiv06o)
6. Click on ‘Change’ under the Computer Name tab
7. ![A computer error screen with red textDescription automatically generated](https://attachment.freshservice.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEwMzQ0Njk5NTYsImRvbWFpbiI6InBhY3MuZnJlc2hzZXJ2aWNlLmNvbSIsInR5cGUiOjF9.FxcxsMkdMc58NS5rKwlTPlDzBnp657owNXFBDQv4qOM)
8. Select ‘Domain’ and type ‘provhc.com’
9. ![A screenshot of a computerDescription automatically generated](https://attachment.freshservice.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEwMzQ0Njk5NTUsImRvbWFpbiI6InBhY3MuZnJlc2hzZXJ2aWNlLmNvbSIsInR5cGUiOjF9.s3Jc0FSu3X34kONiKBOdppYx6hpHnRk5b8iZqjlarJE)
10. If you get an error stating the computer name has already been taken; alter a letter or number at the end of the computer name and try again. (Make sure to find this computer name in AD and put it in the correct OU).

  

Windows 10:

1. Make sure the computer is on the Providence or Support wifi
    1. If the computer is using ethernet and wifi, have the user unplug the ethernet cable so it is only using the wifi.
2. Open settings and select System > About
3. Then click ‘Rename this PC (Advanced)’ on the right side.
4. Then click on change
5. Enter the provhc.com domain and click ok.
6. If you get an error stating the computer name has already been taken; alter a letter or number at the end of the computer name and try again. (Make sure to find this computer name in AD and put it in the correct OU).
7. ![A screenshot of a computerDescription automatically generated](https://attachment.freshservice.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEwMzQ0Njk5NTgsImRvbWFpbiI6InBhY3MuZnJlc2hzZXJ2aWNlLmNvbSIsInR5cGUiOjF9.Cn6E8QhU9mV8DruhrOM0UecXSE7xZxYkBmHCM4MMvoQ)

  

Other errors:

If you get an error stating that the computer is unable to contact the domain after making sure the device is on the support wifi or wired. It may be a DNS issue. Make sure that all of the IPv4 settings are provided via DHCP.