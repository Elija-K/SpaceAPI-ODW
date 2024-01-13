# space.api
The [Space API](https://spaceapi.io/) endpoint for the Amman Valley MakerSpace, switched on and off with a big sign that is also a switch.

- You can see a description of how to setup the [MyHackerspace app](#the-app-myhackerspace).
- You can fork this repository to [set up a Raspberry Pi based HackerSpace status for your own space](#setup-for-your-hackerspace).

![current status][status]

[status]: https://spaceapistatusimage.hosted.quelltext.eu/status?url=https%3A%2F%2Fraw.githubusercontent.com%2FAmmanVMS%2Fspace.api%2Fmain%2Fapi.json

## Usage

If the button is on or off, the scripts will upload the current status.
Since the scripts run each minute once, see crontab and
GitHub refreshes the page every 5 minutes, it can take up to 
**6 minutes** until an update arrives on the website.

### The App MyHackerspace

![image](https://user-images.githubusercontent.com/564768/180648397-77bd6525-fc57-4aa6-b241-db8f5fe593f9.png)

To install the app [MyHackerspace][mhs]:

1. Head over to [f-droid.org](https://f-droid.org/).
2. Download the F-Droid app and install it.
3. Search in it for [MyHackerspace][mhs]: "hacker"
4. Install the app. ([Direct Download](https://f-droid.org/repo/ch.fixme.status_21.apk) - not recommended)
5. In Preferences (three dots at the top right), choose `Amman Valley MakerSpace` or add the current Hackerspace API as `https://raw.githubusercontent.com/AmmanVMS/space.api/main/api.json`.
6. If you want the widget:  
    ![image](https://user-images.githubusercontent.com/564768/180646507-8ecbb045-6ed7-4cce-a769-90427883f696.png)
    1. Long-click on the background of your Android Phone
    2. Choose `Widgets`
    3. Choose `MyHackerspace`
    4. Choose the `Amman Valley MakerSpace`
    5. Choose to display the text and the transparent background.
    6. You will see a button but soon it will have refreshed.

[mhs]: https://f-droid.org/en/packages/ch.fixme.status/

### Status Image

The status image for the space can be found here:

[![status image][status]][status]

Please copy the whole URL if you like to embed it:

    https://spaceapistatusimage.hosted.quelltext.eu/status?url=https%3A%2F%2Fraw.githubusercontent.com%2FAmmanVMS%2Fspace.api%2Fmain%2Fapi.json

### Status Badge

If you would like to have a small badge displaying the status of the space, you can use this one:

[![][badge]][badge]

Please copy the whole URL:

    https://spaceapistatusimage.hosted.quelltext.eu/status?url=https%3A%2F%2Fraw.githubusercontent.com%2FAmmanVMS%2Fspace.api%2Fmain%2Fapi.json&open=https%3A%2F%2Fimg.shields.io%2Fbadge%2FMakerSpace-open-lightgreen&closed=https%3A%2F%2Fimg.shields.io%2Fbadge%2FMakerSpace-closed-red

[badge]: https://spaceapistatusimage.hosted.quelltext.eu/status?url=https%3A%2F%2Fraw.githubusercontent.com%2FAmmanVMS%2Fspace.api%2Fmain%2Fapi.json&open=https%3A%2F%2Fimg.shields.io%2Fbadge%2FMakerSpace-open-lightgreen&closed=https%3A%2F%2Fimg.shields.io%2Fbadge%2FMakerSpace-closed-red

The badge and the image were both created with the [SpaceAPIStatusImage generator](https://ammanvms.github.io/SpaceAPIStatusImage/).

## Setup For Your HackerSpace

You can set up your own Raspberry Pi to report the Hackerspace setup.
This should walk you through how to do it.

1. [Fork this repository.](https://github.com/AmmanVMS/space.api/fork)
2. Edit [api.json](api.json) to represent your own space.  
    You can replace the `workshop-closed.jpg` and `workshop-oepn.jpg` images or just leave them out for the start.
    There is loads to customize. have a look at the [documentation](https://spaceapi.io/docs/).
3. Follow the [Server Installation](#server-installation) described below.
4. Decide if you would like to setup GitHub Pages to serve the endpoint: Fork → Settings → GitHub Pages → choose branch → save.
    The endpoint should be avaliable under https://**your_fork**.github.io/space.api/app.json
    That might be faster than the raw representation which caches for a long time.
5. [Check and include](https://spaceapi.io/provide-an-endpoint/) the raw-git/GitHub Pages URL to the `api.json` file for your repository's api.json file. ([Example](https://github.com/SpaceApi/directory/pull/205))

## Server Installation

The Raspberry Pi will update the status JSON automatically and push the current status
to GitHub. GitHub serves as a reliable server for the data.

1. Install git.
2. Create SSH-Key. 
    ```
    ssh-keygen
    ```
3. Add the `~/.ssh/id_rsa.pub` as deploy key to the repo or add it to the GitHub account.
4. Clone the repo
    ```
    git clone git@github.com:AmmanVMS/space.api
    cd space.api
    git config --local user.email "pi@raspi"
    git config --local user.name "pi"
    ```
5. Add a minutely check with `crontab -e`:
    ```
    * * * * * /home/pi/space.api/check_status.job
    ```

Done. Now, the Raspberry Pi checks the status every minute and
uploads it to GitHub.
You can check if it works by reading the created log file.

## Hardware setup

See [Using Switch with Raspberry Pi – Python](https://electrosome.com/using-switch-raspberry-pi/).
You can also adjust the scripts.

![image](https://user-images.githubusercontent.com/564768/179254745-3d816c42-57bd-415f-a971-402d4f052f74.png)

You can edit the script to change whether a pressed switch means open or closed.

In our case, we also have an LED attached to the swicth so you know if it connects.
Pins: `black(5V) free red(GND) free free yellow(GPIO)`

## Checking the Status

To check the status, run the

```
./status.py
```
