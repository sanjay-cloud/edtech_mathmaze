# edtech_mathmaze

1. Install Minecraft 1.19.2 (Java Edition). In the Official Minecraft Launcher, go to Installations
→ New Installation → Version → Release 1.19.2. Before you go to the next step, press
Play, otherwise it won’t download. Note that we of course discourage third-party launchers,
such as TLauncher, that allow you to download the official client from the official minecraft
website, without owning an account.

2. Install Forge for Minecraft 1.19.2: https://files.minecraftforge.net/net/minecraftforge/
forge/index_1.19.2.html. Note that you might need an up-to-date Java version to install
Forge. To our knowledge openjdk version 17+ suffices.

3. Install the GDMC HTTP interface mod (v1.0.0): https://github.com/Niels-NTG/gdmc_
http_interface/releases/tag/v1.0.0. The release contains a .jar file that you need to
install as a Forge mod2.

4. Install GDPC (the Python package you will be using). You need to clone https://github.
com/avdstaaij/gdpc and install the package by running pip install . in the root of
the cloned repository. Alternatively, you can install it using
pip install git+https://github.com/avdstaaij/gdpc . Do not use “pip install
gdpc”, as that will give you an outdated version.

5.Open Minecraft with the Forge 1.19.2 profile selected. Open a world, set a build area3, and
try to run maze.py. If this works, you should now be ready.
