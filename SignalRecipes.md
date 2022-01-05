# Signal Recipes for success in thought crimes

## Run more than one signal dekstop account off the same installation in linux
In Debian based, distros Signal Desktop is stored in opt. You can specify a secondary userdata dir 
using the --user-data-dir parameter. It will launch another copy of the app with a new data directory
which will allow you to link another device. Command semantics are below:

/opt/{Signal_dir}/signal-desktop --no-sandbox --user-data-dir=/home/$USER/.config/Signal_dup %U
