# Tricks and Tips for getting .NET iOS apps acceptable to the AppStore
While development for iOS using .NET is generally understood and productive, the steps required to get an app
into a form accepted by Transporter, and then the AppStore, are not. This repo contains a fork of a problematic sample,
which uses the Avalonia framework, fixed to be acceptable.

## Goals
Create an .ipa for an iOS app that
- Is accepted by Transporter (and hence the AppStore)
- Has an icon
- Has a launch screen
  
## Setup
This assumes you are using Terminal on MacOS. I also use Jetbrains Rider as my IDE to build and debug. 
I am using Xcode 27.0 (which is technically too new for net10-ios hence the override in the csproj file).

To run the iOS app on the emulator, nothing special is required: use the Debug / AnyCPU target.
To run the iOS app on a device, you will need to go through Developer certificate hell and set up a provisioning profile for your device(s).
This is too painful for me to recount here but reasonably documented elsewhere. 
To create an .ipa file to submit using Transporter you will need a Store Distribution certificate and another (AppStore) provisioning profile.

You will need to create a `LocalOverrides.props` file containing the names of your certificates and profiles, like this:

```xml
<Project>
<PropertyGroup>
    <CodesignKey>iPhone Developer: Your Name (DevTeamName)</CodesignKey>
    <CodesignProvision>iOS Dev Prov Profile</CodesignProvision>
    <ApplicationId>com.cexample.ReproApp</ApplicationId>
</PropertyGroup>

<PropertyGroup Condition="'$(Configuration)'=='Store Release'">
    <CodesignKey>Apple Distribution: Your Name (TeamName)</CodesignKey>
    <CodesignProvision>iOS Store Prov Profile</CodesignProvision>
</PropertyGroup>  
</Project>
```

## Creating the .ipa file
You will need an environment variable containing the name of your AppStore distribution certificate, something like

`export APPLE_DIST="Apple Distribution: Your Name (TeamName)"`

You will need a `StoreEntitlements.plist` file, created from your actual store provisioning profile.
then

`./build_store.sh`

which will create `bin/extracted/$APP_NAME-fixed.ipa`
This script fixes the .ipa that the .NET build system creates and re-signs the ipa, making it suitable for submission via Transporter.

## Notes
My focus has been on the .iOS sub-project. I have done similar work to get MacOS apps to the Store, but that is not yet represented in this repo.
I know little about iOS, there may be better ways of doing this. Please open Issues if you think it can be improved.


