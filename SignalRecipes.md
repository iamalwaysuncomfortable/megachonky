# Signal Recipes for success in thought crimes

## Run more than one signal dekstop account off the same installation in linux
In Debian based, distros Signal Desktop is stored in opt. You can specify a secondary userdata dir 
using the --user-data-dir parameter. It will launch another copy of the app with a new data directory
which will allow you to link another device. Command semantics are below:

/opt/{Signal_dir}/signal-desktop --no-sandbox --user-data-dir={a duplicate directory you create} %U

## Building & Sideloading The Latest Signal Android Apps
### Pre-requisities: 
Git, Docker, Android Studio installed/configured

### Clone the Signal Android source repository
git clone https://github.com/signalapp/Signal-Android.git && cd Signal-Android

### Check out the release tag for the version you'd like to compare
git checkout v[the version number]

### Build the Docker image
cd reproducible-builds
docker build -t signal-android .

### Go back up to the root of the project
cd ..

### Build using the Docker environment
docker run --rm -v $(pwd):/project -w /project signal-android ./gradlew clean assemblePlayProdRelease

The resulting builds will be at: $YOU_SIGNAL_ANDROID_DIR/Signal-Android/app/build/outputs/apk/playProd/release

### Get the android build tools
Properly you need keytool, zipalign, and apksigner. On most debian distros this is at /home/$USER/Android/Sdk/build-tools/ 

### Sign your APK (android won't install unsigned apps)
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias

zipalign -v -p 4 my-app-unsigned.apk my-app-unsigned-aligned.apk

apksigner sign --ks my-release-key.jks --out my-app-release.apk my-app-unsigned-aligned.apk
